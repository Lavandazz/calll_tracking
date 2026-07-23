from PySide6.QtWidgets import QMainWindow, QMessageBox
from app.core.auth_service import AuthService
from app.windows.create_windiws.register_dialog import RegisterDialog
from app.windows.panel import PanelWindow
from login import Ui_MainWindow



class LoginWindow(QMainWindow):
    def __init__(self, session_maker):
        super().__init__()
        self.session_maker = session_maker
        self.auth_service = AuthService(session_maker)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        # Подключаем сигналы
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.show_register_message)
        self.ui.enterLogin.returnPressed.connect(self.login)
        self.ui.enterLogin_2.returnPressed.connect(self.login)

    def login(self):
        username = self.ui.enterLogin.text().strip()
        password = self.ui.enterLogin_2.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Ошибка", "Введите логин и пароль")
            return

        # Выполняем аутентификацию через сервис
        if self.auth_service.login(username, password):
            # Закрываем окно входа
            self.close()
            # Открываем главное окно (передаём session_maker)
            self.main_window = PanelWindow(session_maker=self.session_maker)
            self.main_window.show()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль")

    def show_register_message(self):
        # Открываем диалог регистрации
        register_dialog = RegisterDialog(session_maker=self.session_maker, parent=self)
        register_dialog.exec()