from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QMessageBox
from app.windows.create_windiws.call_dialog import CallEditDialog
from sqlalchemy.orm import sessionmaker

from app.db.call_db import CallDB
from app.core.context import AppContext


class CallService:
    def __init__(self, table_widget: QTableWidget, parent_widget, session_maker: sessionmaker):
        self.table = table_widget
        self.parent = parent_widget
        self.session_maker = session_maker
        self.context = AppContext()

        self.setup_table()

    def setup_table(self):
        table = self.table
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels([
            "ID", "Дата/время", "Кандидат", "Результат",
            "Длительность (мин)", "Комментарий", "Действия"
        ])
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        table.setColumnWidth(0, 20)

        self.load_data()

    def load_data(self):
        """Загружает звонки только текущего пользователя (или все для админа)"""
        user_id = self.context.current_user_id
        if user_id is None:
            QMessageBox.warning(self.parent, "Ошибка", "Пользователь не авторизован")
            return

        with self.session_maker() as session:
            call_db = CallDB(session)
            if self.context.is_admin():
                calls = call_db.get_all_calls()
            else:
                calls = call_db.get_calls_by_user(user_id)

            data = []
            for call in calls:
                candidate_name = call.candidate.name_candidate if call.candidate else "—"
                data.append((
                    call.id,
                    call.date_call.strftime("%Y-%m-%d %H:%M") if call.date_call else "",
                    candidate_name,
                    call.status or "",
                    str(call.duration_minutes) if call.duration_minutes is not None else "",
                    call.comment or "",
                    ""
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
        dialog = CallEditDialog(parent=self.parent, session_maker=self.session_maker)
        if dialog.exec() == QDialog.Accepted:
            data = dialog.result_data
            with self.session_maker() as session:
                call_db = CallDB(session)
                # В data уже есть id_user из контекста
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
            self.load_data()

    def edit_call(self):
        table = self.table
        selected_row = table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self.parent, "Ошибка", "Выберите звонок для редактирования")
            return

        call_id = int(table.item(selected_row, 0).text())
        user_id = self.context.current_user_id

        with self.session_maker() as session:
            call_db = CallDB(session)
            call = call_db.get_call_by_id(call_id)
            if not call:
                QMessageBox.warning(self.parent, "Ошибка", "Звонок не найден")
                return

            # Проверяем, принадлежит ли звонок текущему пользователю (или админ)
            if not self.context.is_admin() and call.id_user != user_id:
                QMessageBox.warning(self.parent, "Ошибка", "Вы не можете редактировать этот звонок")
                return

            current_data = {
                "id_candidate": call.id_candidate,
                "id_vacancy": call.id_vacancy,
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
            # Из результата удаляем id_user, чтобы случайно не перезаписать его,
            # либо оставляем – но в любом случае мы хотим сохранить автора
            # Правильнее – не передавать id_user для обновления
            new_data.pop("id_user", None)
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
        user_id = self.context.current_user_id

        with self.session_maker() as session:
            call_db = CallDB(session)
            call = call_db.get_call_by_id(call_id)
            if not call:
                QMessageBox.warning(self.parent, "Ошибка", "Звонок не найден")
                return
            if not self.context.is_admin() and call.id_user != user_id:
                QMessageBox.warning(self.parent, "Ошибка", "Вы не можете удалить этот звонок")
                return

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