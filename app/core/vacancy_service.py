from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QMessageBox
from app.windows.create_windiws.vacancy_dialog import VacancyEditDialog
from sqlalchemy.orm import sessionmaker
from app.db.vacancy_db import VacancyDB
from app.db.company_db import CompanyDB


class VacancyService:
    def __init__(self, table_widget: QTableWidget, parent_widget, session_maker: sessionmaker):
        self.table = table_widget
        self.parent = parent_widget
        self.session_maker = session_maker

        self.setup_table()

    def setup_table(self):
        """Настройка внешнего вида таблицы вакансий"""
        table = self.table
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels([
            "ID", "Название", "Требования", "Контактное лицо",
            "Телефон", "Компания", "Ссылка"
        ])
        table.setEditTriggers(QTableWidget.NoEditTriggers)  # type: ignore
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        table.setColumnWidth(0, 20)

        self.load_data()

    def load_data(self):
        """Загружает список вакансий из БД и заполняет таблицу"""
        with self.session_maker() as session:
            vacancy_db = VacancyDB(session)
            vacancies = vacancy_db.get_all_vacancies()  # список объектов Vacancy

            # Для получения названия компании используем связь company
            data = []
            for vac in vacancies:
                company_name = vac.company.name_company if vac.company else "—"
                data.append((
                    vac.id,
                    vac.name_vacancy,
                    vac.requirements or "",
                    vac.contact_person or "",
                    vac.contact_phone or "",
                    company_name,
                    vac.link_vacancy or "",
                ))

        self._populate_table(data)

    def _populate_table(self, data):
        """Заполняет таблицу переданным списком кортежей"""
        table = self.table
        table.setRowCount(len(data))
        for row, record in enumerate(data):
            for col, value in enumerate(record):
                item = QTableWidgetItem(str(value) if value is not None else "")
                table.setItem(row, col, item)

    def add_vacancy(self):
        """Открыть диалог добавления новой вакансии"""
        dialog = VacancyEditDialog(parent=self.parent, session_maker=self.session_maker)
        if dialog.exec() == QDialog.Accepted:
            data = dialog.result_data   # словарь с полями
            with self.session_maker() as session:
                vacancy_db = VacancyDB(session)
                vacancy_db.create_vacancy(data)
            self.load_data()

    def edit_vacancy(self):
        """Открыть диалог редактирования выбранной вакансии"""
        table = self.table
        selected_row = table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self.parent, "Ошибка", "Выберите вакансию для редактирования")
            return

        vacancy_id = int(table.item(selected_row, 0).text())

        with self.session_maker() as session:
            vacancy_db = VacancyDB(session)
            vacancy = vacancy_db.get_vacancy_by_id(vacancy_id)
            if not vacancy:
                QMessageBox.warning(self.parent, "Ошибка", "Вакансия не найдена в БД")
                return

            current_data = {
                "name_vacancy": vacancy.name_vacancy,
                "requirements": vacancy.requirements,
                "contact_person": vacancy.contact_person,
                "contact_phone": vacancy.contact_phone,
                "contact_email": vacancy.contact_email,
                "link_vacancy": vacancy.link_vacancy,
                "id_company": vacancy.id_company,   # для заполнения выпадающего списка компаний
            }

        dialog = VacancyEditDialog(current_data, parent=self.parent, session_maker=self.session_maker)
        if dialog.exec() == QDialog.Accepted:
            new_data = dialog.result_data
            with self.session_maker() as session:
                vacancy_db = VacancyDB(session)
                vacancy_db.update_vacancy(vacancy_id, new_data)
            self.load_data()

    def delete_vacancy(self):
        """Удалить выбранную вакансию"""
        table = self.table
        selected_row = table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self.parent, "Ошибка", "Выберите вакансию для удаления")
            return

        vacancy_id = int(table.item(selected_row, 0).text())

        reply = QMessageBox.question(
            self.parent,
            "Подтверждение удаления",
            f"Вы действительно хотите удалить вакансию с ID {vacancy_id}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            with self.session_maker() as session:
                vacancy_db = VacancyDB(session)
                vacancy_db.delete_vacancy(vacancy_id)
            self.load_data()