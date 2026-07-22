from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QMessageBox
from app.windows.create_windiws.call_dialog import CallEditDialog
from sqlalchemy.orm import sessionmaker

from app.db.call_db import CallDB
from app.db.candidate_db import CandidateDB
from app.db.vacancy_db import VacancyDB
from app.db.user_db import UserDB


class CallService:
    def __init__(self, table_widget: QTableWidget, parent_widget, session_maker: sessionmaker):
        self.table = table_widget
        self.parent = parent_widget
        self.session_maker = session_maker

        self.setup_table()

    def setup_table(self):
        table = self.table
        # Столбцы: ID, Дата/время, Кандидат, Результат (статус), Длительность, Комментарий, Действия
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels([
            "ID", "Дата/время", "Кандидат", "Результат",
            "Длительность (мин)", "Комментарий", "Действия"
        ])
        table.setEditTriggers(QTableWidget.NoEditTriggers)  # type: ignore
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        table.setColumnWidth(0, 20)

        self.load_data()

    def load_data(self, user_id=None):
        """Загружает звонки из БД и заполняет таблицу.
           Если user_id не указан, загружаются все звонки (для админа).
           Можно передать текущего пользователя.
        """
        with self.session_maker() as session:
            call_db = CallDB(session)
            if user_id is not None:
                calls = call_db.get_calls_by_user(user_id)
            else:
                calls = call_db.get_all_calls()

            data = []
            for call in calls:
                # Получаем имя кандидата (если есть)
                candidate_name = call.candidate.name_candidate if call.candidate else "—"
                # Можно также показать вакансию или пользователя, но в таблице их нет.
                # При желании можно добавить столбец "Вакансия" или "Пользователь"
                data.append((
                    call.id,
                    call.date_call.strftime("%Y-%m-%d %H:%M") if call.date_call else "",
                    candidate_name,
                    call.status or "",
                    str(call.duration_minutes) if call.duration_minutes is not None else "",
                    call.comment or "",
                    ""  # Действия (пока пусто)
                ))

        self._populate_table(data)

    def _populate_table(self, data):
        table = self.table
        table.setRowCount(len(data))
        for row, record in enumerate(data):
            for col, value in enumerate(record):
                item = QTableWidgetItem(str(value) if value is not None else "")
                table.setItem(row, col, item)

    def add_call(self):
        """Открыть диалог добавления нового звонка"""
        dialog = CallEditDialog(parent=self.parent, session_maker=self.session_maker)
        if dialog.exec() == QDialog.Accepted:
            data = dialog.result_data
            # Обязательные поля: id_user (можно задать текущего пользователя), id_candidate, id_vacancy,
            # но они могут быть None. Если хотите сделать обязательными, проверьте.
            # Для простоты сохраняем как есть.
            with self.session_maker() as session:
                call_db = CallDB(session)
                # Метод add_call требует все поля, кроме id и date_create (они генерируются)
                # Но в data у нас все ключи соответствуют полям модели, кроме id.
                # Создадим объект Call напрямую через словарь, чтобы не завязываться на сигнатуру метода add_call.
                # Можно использовать универсальный метод create из репозитория, но у нас его нет.
                # Самый простой способ: создать объект и добавить.
                new_call = call_db.add_call(
                    user_id=data.get("id_user"),
                    candidate_id=data.get("id_candidate"),
                    vacancy_id=data.get("id_vacancy"),
                    status=data.get("status"),
                    source=data.get("source"),
                    comment=data.get("comment"),
                    duration_minutes=data.get("duration_minutes"),
                    date_call=data.get("date_call"),
                    link_resume=data.get("link_resume")
                )
            self.load_data()  # обновить таблицу

    def edit_call(self):
        table = self.table
        selected_row = table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self.parent, "Ошибка", "Выберите звонок для редактирования")
            return

        call_id = int(table.item(selected_row, 0).text())

        with self.session_maker() as session:
            call_db = CallDB(session)
            call = call_db.get_call_by_id(call_id)
            if not call:
                QMessageBox.warning(self.parent, "Ошибка", "Звонок не найден")
                return

            current_data = {
                "id_candidate": call.id_candidate,
                "id_vacancy": call.id_vacancy,
                "id_user": call.id_user,
                "status": call.status,
                "source": call.source,
                "comment": call.comment,
                "duration_minutes": call.duration_minutes,
                "date_call": call.date_call,
                "link_resume": call.link_resume,
            }

        dialog = CallEditDialog(current_data, parent=self.parent, session_maker=self.session_maker)
        if dialog.exec() == QDialog.Accepted:
            new_data = dialog.result_data
            with self.session_maker() as session:
                call_db = CallDB(session)
                call_db.update_call(call_id, new_data)
            self.load_data()

    def delete_call(self):
        table = self.table
        selected_row = table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self.parent, "Ошибка", "Выберите звонок для удаления")
            return

        call_id = int(table.item(selected_row, 0).text())

        reply = QMessageBox.question(
            self.parent,
            "Подтверждение удаления",
            f"Вы действительно хотите удалить звонок с ID {call_id}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            with self.session_maker() as session:
                call_db = CallDB(session)
                call_db.delete_call(call_id)
            self.load_data()