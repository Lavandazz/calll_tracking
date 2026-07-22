from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QTextEdit, QComboBox, QPushButton, QMessageBox
)
from PySide6.QtCore import Qt
from sqlalchemy.orm import sessionmaker
from app.db.company_db import CompanyDB
from app.db.vacancy_db import VacancyDB


class VacancyEditDialog(QDialog):
    def __init__(self, data=None, parent=None, session_maker: sessionmaker = None):
        super().__init__(parent)
        self.session_maker = session_maker
        self.data = data or {}
        self.setWindowTitle("Редактирование вакансии" if data else "Новая вакансия")
        self.setModal(True)

        # Поля ввода
        self.name_edit = QLineEdit()
        self.requirements_edit = QTextEdit()
        self.contact_person_edit = QLineEdit()
        self.contact_phone_edit = QLineEdit()
        self.contact_email_edit = QLineEdit()
        self.link_vacancy_edit = QLineEdit()
        self.company_combo = QComboBox()

        # Заполняем список компаний
        self.load_companies()

        # Заполняем поля данными (если редактирование)
        self.load_data()

        # Собираем форму
        layout = QVBoxLayout(self)
        form = QFormLayout()
        form.addRow("Название вакансии:", self.name_edit)
        form.addRow("Требования:", self.requirements_edit)
        form.addRow("Контактное лицо:", self.contact_person_edit)
        form.addRow("Контактный телефон:", self.contact_phone_edit)
        form.addRow("Контактный email:", self.contact_email_edit)
        form.addRow("Ссылка на вакансию:", self.link_vacancy_edit)
        form.addRow("Компания:", self.company_combo)
        layout.addLayout(form)

        # Кнопки
        btn_box = QHBoxLayout()
        ok_btn = QPushButton("Сохранить")
        cancel_btn = QPushButton("Отмена")
        ok_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        btn_box.addWidget(ok_btn)
        btn_box.addWidget(cancel_btn)
        layout.addLayout(btn_box)

        self.setLayout(layout)

    def load_companies(self):
        """Загружает список компаний из БД и заполняет QComboBox"""
        self.company_combo.clear()
        self.company_combo.addItem("Без компании", None)  # опция для пустого значения

        if not self.session_maker:
            return

        try:
            with self.session_maker() as session:
                company_db = CompanyDB(session)
                companies = company_db.get_all_companies()
                for comp in companies:
                    self.company_combo.addItem(comp.name_company, comp.id)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить компании:\n{str(e)}")

    def load_data(self):
        """Заполняет поля из переданного словаря data"""
        if not self.data:
            return

        self.name_edit.setText(self.data.get("name_vacancy", ""))
        self.requirements_edit.setPlainText(self.data.get("requirements", ""))
        self.contact_person_edit.setText(self.data.get("contact_person", ""))
        self.contact_phone_edit.setText(self.data.get("contact_phone", ""))
        self.contact_email_edit.setText(self.data.get("contact_email", ""))
        self.link_vacancy_edit.setText(self.data.get("link_vacancy", ""))

        # Устанавливаем выбранную компанию по id_company
        company_id = self.data.get("id_company")
        if company_id is not None:
            index = self.company_combo.findData(company_id)
            if index >= 0:
                self.company_combo.setCurrentIndex(index)

    @property
    def result_data(self):
        """Возвращает словарь с данными из полей"""
        return {
            "name_vacancy": self.name_edit.text().strip(),
            "requirements": self.requirements_edit.toPlainText().strip(),
            "contact_person": self.contact_person_edit.text().strip(),
            "contact_phone": self.contact_phone_edit.text().strip(),
            "contact_email": self.contact_email_edit.text().strip(),
            "link_vacancy": self.link_vacancy_edit.text().strip(),
            "id_company": self.company_combo.currentData(),  # None, если не выбрано
        }