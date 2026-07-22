from PySide6.QtWidgets import QMainWindow, QMessageBox
from app.windows.panel import PanelWindow
from login import Ui_MainWindow

class LoginWindow(QMainWindow):
    def __init__(self, session_maker):
        super().__init__()
        # Создается экземпляр класса Ui_MainWindow 
        # и вызывается метод setupUi для настройки интерфейса
        self.session_maker = session_maker
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        # Подключаем сигналы кнопок
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.show_register_message)
        # Подключаем сигналы нажатия Enter в полях ввода
        self.ui.enterLogin.returnPressed.connect(self.login)
        self.ui.enterLogin_2.returnPressed.connect(self.login)


    def login(self):
        login = self.ui.enterLogin.text()      # получаем текст из поля логина
        password = self.ui.enterLogin_2.text() # получаем текст из поля пароля

        # Здесь потом будет запрос к БД через SQLAlchemy
        # Пока заглушка: пропускаем только admin / 12345
        if login == "admin" and password == "12345":
            # Закрываем окно входа
            self.close()
            # Создаём и показываем главное окно
            self.main_window = PanelWindow(session_maker=self.session_maker)
            self.main_window.show()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль")

    def show_register_message(self):
        QMessageBox.information(self, "Регистрация", "Функция регистрации будет добавлена позже")