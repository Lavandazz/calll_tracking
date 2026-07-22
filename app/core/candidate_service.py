from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QMessageBox
from app.windows.create_windiws.candidate_dialog import CandidateEditDialog
from sqlalchemy.orm import sessionmaker

from app.db.candidate_db import CandidateDB


class CandidateService:
    def __init__(self, table_widget: QTableWidget, parent_widget, session_maker: sessionmaker):
        self.table = table_widget
        self.parent = parent_widget
        self.session_maker = session_maker

        self.setup_table()

    def setup_table(self):
        """Настройка внешнего вида таблицы кандидатов"""
        table = self.table
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels([
            "ID", "ФИО", "Телефон", "Email", "Статус", "Комментарий", "Резюме"
        ])
        table.setEditTriggers(QTableWidget.NoEditTriggers)  # type: ignore
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        table.setColumnWidth(0, 50)
        for col in range(1, 7):
            header.setSectionResizeMode(col, QHeaderView.ResizeMode.Stretch)

        self.load_data()

    def load_data(self):
        """Загружает список кандидатов из БД и заполняет таблицу"""
        with self.session_maker() as session:
            candidate_db = CandidateDB(session)
            candidates = candidate_db.get_all_candidates()

            data = []
            for cand in candidates:
                data.append((
                    cand.id,
                    cand.name_candidate,
                    cand.phone or "",
                    cand.email or "",
                    cand.status or "",
                    cand.comment or "",
                    cand.link_resume or "",
                ))

        self._populate_table(data)

    def _populate_table(self, data):
        table = self.table
        table.setRowCount(len(data))
        for row, record in enumerate(data):
            for col, value in enumerate(record):
                item = QTableWidgetItem(str(value) if value is not None else "")
                table.setItem(row, col, item)

    def add_candidate(self):
        """Открыть диалог добавления нового кандидата"""
        dialog = CandidateEditDialog(parent=self.parent, session_maker=self.session_maker)
        if dialog.exec() == QDialog.Accepted:
            data = dialog.result_data
            with self.session_maker() as session:
                candidate_db = CandidateDB(session)
                candidate_db.create_candidate(data)
            self.load_data()

    def edit_candidate(self):
        """Открыть диалог редактирования выбранного кандидата"""
        table = self.table
        selected_row = table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self.parent, "Ошибка", "Выберите кандидата для редактирования")
            return

        candidate_id = int(table.item(selected_row, 0).text())

        with self.session_maker() as session:
            candidate_db = CandidateDB(session)
            candidate = candidate_db.get_candidate_by_id(candidate_id)
            if not candidate:
                QMessageBox.warning(self.parent, "Ошибка", "Кандидат не найден")
                return

            current_data = {
                "name_candidate": candidate.name_candidate,
                "phone": candidate.phone,
                "email": candidate.email,
                "link_resume": candidate.link_resume,
                "status": candidate.status,
                "comment": candidate.comment,
            }

        dialog = CandidateEditDialog(current_data, parent=self.parent, session_maker=self.session_maker)
        if dialog.exec() == QDialog.Accepted:
            new_data = dialog.result_data
            with self.session_maker() as session:
                candidate_db = CandidateDB(session)
                candidate_db.update_candidate(candidate_id, new_data)
            self.load_data()

    def delete_candidate(self):
        """Удалить выбранного кандидата"""
        table = self.table
        selected_row = table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self.parent, "Ошибка", "Выберите кандидата для удаления")
            return

        candidate_id = int(table.item(selected_row, 0).text())

        reply = QMessageBox.question(
            self.parent,
            "Подтверждение удаления",
            f"Вы действительно хотите удалить кандидата с ID {candidate_id}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            with self.session_maker() as session:
                candidate_db = CandidateDB(session)
                candidate_db.delete_candidate(candidate_id)
            self.load_data()