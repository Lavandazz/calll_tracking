from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget

from PySide6.QtWidgets import QLabel, QLineEdit, QMessageBox
from app.windows.main import MainWindow



class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход в систему")
        self.setFixedSize(300, 200)  # фиксированный размер

        # Создаём виджеты
        self.label_login = QLabel("Логин:")
        self.input_login = QLineEdit()
        self.input_login.setPlaceholderText("Введите логин")

        self.label_password = QLabel("Пароль:")
        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Введите пароль")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)  # скрываем символы

        self.input_password.returnPressed.connect(self.handle_login)  # сигнал нажатия Enter в поле пароля 
        self.btn_login = QPushButton("Войти")
        self.btn_login.clicked.connect(self.handle_login)  # сигнал нажатия

        self.btn_register = QPushButton("Регистрация")
        self.btn_register.clicked.connect(self.show_register_message)

        # Располагаем всё вертикально
        layout = QVBoxLayout()
        layout.addWidget(self.label_login)
        layout.addWidget(self.input_login)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.btn_login)
        layout.addWidget(self.btn_register)

        self.setLayout(layout)

    # Слот для кнопки "Войти"
    def handle_login(self):
        login = self.input_login.text()
        password = self.input_password.text()

        # ⚠️ Здесь потом будет запрос к БД через SQLAlchemy
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
