from pathlib import Path
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QLineEdit, QMessageBox
from app.utils.folder_path import PathFolder
from app.windows.main_app import MainWindow


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 400)
        self.setWindowTitle("Вход в систему")

        # 1. Фон
        self.background_label = QLabel(self)
        image_path = PathFolder.images / "1.jpeg"
        print("Путь к картинке:", image_path)
        image = QPixmap(str(image_path))
        
        scaled_pixmap = image.scaled(
        self.width(), self.height(),
        Qt.KeepAspectRatioByExpanding,  # или Qt.KeepAspectRatio (тогда будут поля) # type: ignore
        Qt.SmoothTransformation # type: ignore
        )
        self.background_label.setPixmap(scaled_pixmap)
        self.background_label.setAlignment(Qt.AlignCenter)  # центрируем
        self.background_label.setGeometry(0, 0, self.width(), self.height())

        # 2. Виджеты с родителем
        self.label_login = QLabel("Логин:", self)
        self.input_login = QLineEdit(self)
        self.input_login.setPlaceholderText("Введите логин")

        self.label_password = QLabel("Пароль:", self)
        self.input_password = QLineEdit(self)
        self.input_password.setPlaceholderText("Введите пароль")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.btn_login = QPushButton("Войти", self)
        self.btn_register = QPushButton("Регистрация", self)

        # 3. Сигналы
        self.input_password.returnPressed.connect(self.handle_login)
        self.btn_login.clicked.connect(self.handle_login)
        self.btn_register.clicked.connect(self.show_register_message)

        # 4. Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_login)
        layout.addWidget(self.input_login)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.btn_login)
        layout.addWidget(self.btn_register)
        self.setLayout(layout)

        # 5. Фон на задний план
        self.background_label.lower()
    # Слот для кнопки "Войти"
    def handle_login(self):
        login = self.input_login.text()
        password = self.input_password.text()

        # Пока заглушка: пропускаем только admin / 12345
        if login == "admin" and password == "12345":
            # Закрываем окно входа
            self.close()
            # Создаём и показываем главное окно
            self.main_window = MainWindow()
            self.main_window.show()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль")

    def show_register_message(self):
        QMessageBox.information(self, "Регистрация", "Функция регистрации будет добавлена позже")
