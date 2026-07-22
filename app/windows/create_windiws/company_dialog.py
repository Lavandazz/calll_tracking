from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QPushButton, QMessageBox
)
from PySide6.QtCore import Qt

class CompanyEditDialog(QDialog):
    def __init__(self, company_data=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавление компании" if company_data is None else "Редактирование компании")
        self.setModal(True)
        self.setMinimumWidth(450)

        # Устанавливаем фон (градиент, как вы указали)
        self.setStyleSheet("""
            QDialog {
                background-color: qlineargradient(
                    spread:pad, x1:1, y1:0, x2:0, y2:0,
                    stop:0 rgba(90, 174, 190, 78),
                    stop:0.353234 rgba(0, 0, 0, 218)
                );
            }
            QLabel {
                color: white;
            }
            QLineEdit, QPushButton {
                background-color: rgba(255, 255, 255, 200);
                border-radius: 4px;
                padding: 5px;
                color: black;
            }
            QPushButton {
                background-color: rgba(218, 255, 255, 230);
                color: black;
                border: 1px solid rgb(205, 239, 255);
                border-radius: 7px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: white;
            }
        """)

        # Хранилище результата
        self.result_data = None

        # Поля
        self.name_edit = QLineEdit()
        self.contact_edit = QLineEdit()
        self.address_edit = QLineEdit()
        self.phone_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.website_edit = QLineEdit()

        # Если переданы данные – заполняем
        if company_data:
            self.name_edit.setText(company_data.get("name_company", ""))
            self.contact_edit.setText(company_data.get("contact_person", ""))
            self.address_edit.setText(company_data.get("address", ""))
            self.phone_edit.setText(company_data.get("phone", ""))
            self.email_edit.setText(company_data.get("email", ""))
            self.website_edit.setText(company_data.get("website", ""))

        # Основной layout
        layout = QVBoxLayout(self)

        # Форма
        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignRight)
        form.addRow("Название компании:", self.name_edit)
        form.addRow("Контактное лицо:", self.contact_edit)
        form.addRow("Адрес:", self.address_edit)
        form.addRow("Телефон:", self.phone_edit)
        form.addRow("Email:", self.email_edit)
        form.addRow("Сайт:", self.website_edit)
        layout.addLayout(form)

        # Кнопки
        btn_layout = QHBoxLayout()
        save_btn = QPushButton("Сохранить")
        cancel_btn = QPushButton("Отмена")
        save_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addStretch()
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)

    def accept(self):
        data = {
            "name_company": self.name_edit.text().strip(),
            "contact_person": self.contact_edit.text().strip(),
            "address": self.address_edit.text().strip(),
            "phone": self.phone_edit.text().strip(),
            "email": self.email_edit.text().strip(),
            "website": self.website_edit.text().strip(),
        }
        if not data["name_company"]:
            QMessageBox.warning(self, "Ошибка", "Название компании обязательно")
            return
        self.result_data = data
        super().accept()