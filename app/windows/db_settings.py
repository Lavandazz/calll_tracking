from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox
)
from sqlalchemy import text  
from PySide6.QtCore import QSettings
from config.settings import build_settings_from_dict, create_sessionmaker_from_settings

import base64

COMPANY = "YourCompany"
APP_NAME = "YourApp"

class DbSettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Настройки подключения к базе данных")
        self.setModal(True)
        self.resize(400, 300)

        layout = QVBoxLayout(self)

        form = QFormLayout()
        self.host_edit = QLineEdit()
        self.port_edit = QLineEdit("5432")
        self.dbname_edit = QLineEdit()
        self.user_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        form.addRow("Сервер (хост):", self.host_edit)
        form.addRow("Порт:", self.port_edit)
        form.addRow("Имя БД:", self.dbname_edit)
        form.addRow("Пользователь:", self.user_edit)
        form.addRow("Пароль:", self.password_edit)

        layout.addLayout(form)

        # Кнопки
        btn_test = QPushButton("Проверить подключение")
        btn_save = QPushButton("Сохранить")
        btn_cancel = QPushButton("Отмена")

        layout.addWidget(btn_test)
        layout.addWidget(btn_save)
        layout.addWidget(btn_cancel)

        btn_test.clicked.connect(self.test_connection)
        btn_save.clicked.connect(self.save_and_accept)
        btn_cancel.clicked.connect(self.reject)

        # Загружаем сохранённые значения (кроме пароля)
        self.load_existing()

    def load_existing(self):
        qs = QSettings(COMPANY, APP_NAME)
        self.host_edit.setText(qs.value("db/host", ""))
        self.port_edit.setText(str(qs.value("db/port", 5432)))
        self.dbname_edit.setText(qs.value("db/dbname", ""))
        self.user_edit.setText(qs.value("db/user", ""))
        # Пароль не загружаем — пользователь введёт заново

    def get_values(self):
        host = self.host_edit.text().strip()
        try:
            port = int(self.port_edit.text().strip())
        except ValueError:
            port = 5432
        dbname = self.dbname_edit.text().strip()
        user = self.user_edit.text().strip()
        password = self.password_edit.text().strip()
        return host, port, dbname, user, password

    def test_connection(self):
        host, port, dbname, user, password = self.get_values()
        if not all([host, dbname, user, password]):
            QMessageBox.warning(self, "Ошибка", "Заполните все поля.")
            return
        try:
            # Временно создаём объект Settings
            temp_settings = build_settings_from_dict({
                'POSTGRES_HOST': host,
                'POSTGRES_PORT': port,
                'POSTGRES_DB': dbname,
                'POSTGRES_USER': user,
                'POSTGRES_PASSWORD': password,
            })
            session_maker = create_sessionmaker_from_settings(temp_settings)
            with session_maker() as session:
                session.execute(text("SELECT 1")) 
            QMessageBox.information(self, "Успех", "Подключение к БД успешно!")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось подключиться:\n{str(e)}")

    def save_and_accept(self):
        host, port, dbname, user, password = self.get_values()
        if not all([host, dbname, user, password]):
            QMessageBox.warning(self, "Ошибка", "Заполните все поля.")
            return
        # Сохраняем в QSettings
        qs = QSettings(COMPANY, APP_NAME)
        qs.setValue("db/host", host)
        qs.setValue("db/port", port)
        qs.setValue("db/dbname", dbname)
        qs.setValue("db/user", user)
        # Шифруем пароль (base64)
        encrypted = base64.b64encode(password.encode()).decode()
        qs.setValue("db/password", encrypted)
        self.accept()