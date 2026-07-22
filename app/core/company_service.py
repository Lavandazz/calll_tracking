from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QMessageBox
from sqlalchemy.orm import sessionmaker
from app.windows.create_windiws.company_dialog import CompanyEditDialog
from app.db.company_db import CompanyDB   # предположим, что CompanyDB лежит в app.db


class CompanyService:
    def __init__(self, table_widget: QTableWidget, parent_widget, session_maker: sessionmaker):
        self.table = table_widget
        self.parent = parent_widget
        self.session_maker = session_maker

        self.setup_table()

    def setup_table(self):
        """Настройка внешнего вида таблицы"""
        table = self.table
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels([
            "ID", "Название", "Контактное лицо", "Телефон", "Email", "Адрес", "Сайт"
        ])
        table.setEditTriggers(QTableWidget.NoEditTriggers)  # type: ignore
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        table.setColumnWidth(0, 20)

        # Загружаем данные из БД
        self.load_data()

    def load_data(self):
        """Загружает список компаний из БД и заполняет таблицу"""
        with self.session_maker() as session:
            company_db = CompanyDB(session)
            companies = company_db.get_all_companies()  # список объектов Company из SQLAlchemy

        # Преобразуем объекты в кортежи для отображения
        data = []
        for comp in companies:
            data.append((
                comp.id,
                comp.name_company,
                comp.contact_person,
                comp.phone,
                comp.email,
                comp.address,      # если поле есть
                comp.website,
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

    def add_company(self):
        """Открыть диалог добавления новой компании"""
        dialog = CompanyEditDialog(parent=self.parent)
        if dialog.exec() == QDialog.Accepted:
            data = dialog.result_data  # словарь с полями

            with self.session_maker() as session:
                company_db = CompanyDB(session)
                company_db.add_company(data)  # CompanyDB сам делает commit

            self.load_data()  # обновить таблицу

    def edit_company(self):
        """Открыть диалог редактирования выбранной компании"""
        table = self.table
        selected_row = table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self.parent, "Ошибка", "Выберите компанию для редактирования")
            return

        # Получаем ID компании из первого столбца
        company_id = int(table.item(selected_row, 0).text())

        # Загружаем данные из БД по ID
        with self.session_maker() as session:
            company_db = CompanyDB(session)
            company = company_db.get_company_by_id(company_id)
            if not company:
                QMessageBox.warning(self.parent, "Ошибка", "Компания не найдена в БД")
                return

            current_data = {
                "name_company": company.name_company,
                "contact_person": company.contact_person,
                "phone": company.phone,
                "email": company.email,
                "address": company.address,
                "website": company.website,
            }

        dialog = CompanyEditDialog(current_data, parent=self.parent)
        if dialog.exec() == QDialog.Accepted:
            new_data = dialog.result_data
            with self.session_maker() as session:
                company_db = CompanyDB(session)
                # Обновляем только переданные поля
                company_db.update_company(
                    company_id,
                    name_company=new_data.get("name_company"),
                    contact_person=new_data.get("contact_person"),
                    phone=new_data.get("phone"),
                    email=new_data.get("email"),
                    website=new_data.get("website"),
                    # если есть address, добавьте
                )
            self.load_data()

    def delete_company(self):
        """Удалить выбранную компанию"""
        table = self.table
        selected_row = table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self.parent, "Ошибка", "Выберите компанию для удаления")
            return

        company_id = int(table.item(selected_row, 0).text())

        reply = QMessageBox.question(
            self.parent,
            "Подтверждение удаления",
            f"Вы действительно хотите удалить компанию с ID {company_id}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            with self.session_maker() as session:
                company_db = CompanyDB(session)
                company_db.delete_company(company_id)
            self.load_data()