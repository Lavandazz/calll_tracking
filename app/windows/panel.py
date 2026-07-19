import sys
from PySide6.QtWidgets import QMainWindow,  QMessageBox
from app.windows.main_app import MainWindow
from panel import Ui_MainWindow


class PanelWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Создается экземпляр класса Ui_MainWindow 
        # и вызывается метод setupUi для настройки интерфейса
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        # Подключаем сигналы кнопок
        self.ui.candidates.clicked.connect(self.show_candidates)
        self.ui.callLog.clicked.connect(self.show_call_log)
        self.ui.reportCall.clicked.connect(self.show_report_call)
        self.ui.company.clicked.connect(self.show_company)
        self.ui.vacancy.clicked.connect(self.show_vacancy)


    def show_company(self):
        QMessageBox.information(self, "Компании", "Функция компании будет добавлена позже")

    def show_vacancy(self):
        QMessageBox.information(self, "Вакансии", "Функция вакансий будет добавлена позже")

    def show_candidates(self):
        QMessageBox.information(self, "Кандидаты", "Функция регистрации будет добавлена позже")

    def show_call_log(self):
        QMessageBox.information(self, "Журнал звонков", "Функция журнала вызовов будет добавлена позже")

    def show_report_call(self):
        QMessageBox.information(self, "Отчет о вызовах", "Функция отчета о вызовах будет добавлена позже")

    def show_statistic_call(self):
        QMessageBox.information(self, "Статистика звонков", "Функция отчета о вызовах будет добавлена позже")
