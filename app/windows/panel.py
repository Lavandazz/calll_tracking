import sys
from PySide6.QtWidgets import QHeaderView, QMainWindow,  QMessageBox, QStackedWidget, QTableWidgetItem
from app.windows.main_app import MainWindow
from main_panel import Ui_MainWindow


class PanelWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Создается экземпляр класса Ui_MainWindow 
        # и вызывается метод setupUi для настройки интерфейса
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stacked = self.ui.stackedWidget
        print("Количество страниц в стеке:", self.stacked.count())
        self.stacked.setCurrentWidget(self.ui.welcomePage)
        
        self.ui.company.clicked.connect(self.show_company)
        self.ui.vacancy.clicked.connect(lambda: self.stacked.setCurrentWidget(self.ui.vacancyPage))
        self.ui.candidates.clicked.connect(lambda: self.stacked.setCurrentWidget(self.ui.candidatesPage))
        self.ui.callLog.clicked.connect(lambda: self.stacked.setCurrentWidget(self.ui.callLogPage))
        self.ui.reportCall.clicked.connect(lambda: self.stacked.setCurrentWidget(self.ui.reportCallPage))
        self.ui.callStatistic.clicked.connect(lambda: self.stacked.setCurrentWidget(self.ui.statisticCallPage))



        self.setup_call_log_table()

    def show_company(self):
        # QMessageBox.information(self, "Компании", "Функция компании будет добавлена позже")
        self.ui.company.clicked.connect(lambda: self.stacked.setCurrentWidget(self.ui.companyPage))

    def setup_call_log_table(self):
        table = self.ui.tableLog   # objectName из дизайнера
        # Задаём 7 столбцов (ID, Дата/время, Кандидат, Результат, Длительность, Комментарий, Действия)
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels([
            "ID", "Дата/время", "Кандидат", "Результат",
            "Длительность (мин)", "Комментарий", "Действия"
        ])
        # Растягиваем столбцы по ширине
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # Заполняем тестовыми данными
        self.populate_call_log()

    def populate_call_log(self):
        table = self.ui.tableLog
        test_data = [
            (1, "2026-07-18 10:30", "Иванов Иван", "Заинтересован", "5", "Обсудили условия", ""),
            (2, "2026-07-18 11:15", "Петрова Мария", "Не дозвонился", "0", "Автоответчик", ""),
            (3, "2026-07-17 16:20", "Сидоров Алексей", "Приглашён на собеседование", "12", "Назначена встреча на пятницу", ""),
            (4, "2026-07-17 09:45", "Козлова Анна", "Отказ", "3", "Не подходит график", ""),
            (5, "2026-07-16 14:00", "Николаев Дмитрий", "Нанят", "8", "Принят на позицию", "")
        ]
        table.setRowCount(len(test_data))
        for row, data in enumerate(test_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                table.setItem(row, col, item)


    