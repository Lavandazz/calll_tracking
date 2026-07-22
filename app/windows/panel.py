
from PySide6.QtWidgets import QHeaderView, QMainWindow, QTableWidget, QTableWidgetItem
from app.core.company_service import CompanyService
from app.core.vacancy_service import VacancyService
from app.windows.create_windiws.company_dialog import CompanyEditDialog
from panel3 import Ui_MainWindow
from PySide6.QtWidgets import (QDialog, QMessageBox)

class PanelWindow(QMainWindow):
    def __init__(self, session_maker):
        super().__init__()
        # Создается экземпляр класса Ui_MainWindow 
        # и вызывается метод setupUi для настройки интерфейса
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.company_service = CompanyService(
            table_widget=self.ui.tableCompany,
            parent_widget=self,
            session_maker=session_maker
        )
                # Сервис для вакансий
        self.vacancy_service = VacancyService(
            table_widget=self.ui.tableVacancy,
            parent_widget=self,
            session_maker=session_maker
        )

        self.stacked = self.ui.stackedWidget
        self.stacked.setCurrentWidget(self.ui.welcomePage)
        
        self.ui.company.clicked.connect(self.show_company)
        self.ui.vacancy.clicked.connect(lambda: self.stacked.setCurrentWidget(self.ui.vacancyPage))
        self.ui.candidates.clicked.connect(lambda: self.stacked.setCurrentWidget(self.ui.candidatesPage))
        self.ui.callLog.clicked.connect(lambda: self.stacked.setCurrentWidget(self.ui.callLogPage))
        self.ui.callStatistic.clicked.connect(lambda: self.stacked.setCurrentWidget(self.ui.statisticPage))


        self.setup_call_log_table()
        self.setup_statistics_table()
        self.setup_candidates_table()

        # Подключаем кнопки добавления, редактирования и удаления компаний к методам CompanyService
        self.ui.addCompany.clicked.connect(self.company_service.add_company)
        self.ui.editCompany.clicked.connect(self.company_service.edit_company)
        self.ui.deleteCompany.clicked.connect(self.company_service.delete_company)

        self.ui.addVacancy.clicked.connect(self.vacancy_service.add_vacancy)
        self.ui.editVacancy.clicked.connect(self.vacancy_service.edit_vacancy)
        self.ui.deleteVacancy.clicked.connect(self.vacancy_service.delete_vacancy)



    def show_company(self):
        self.ui.company.clicked.connect(lambda: self.stacked.setCurrentWidget(self.ui.companyPage))

    def setup_call_log_table(self):
        table = self.ui.tableLog   # objectName из дизайнера
        # Задаём 7 столбцов (ID, Дата/время, Кандидат, Результат, Длительность, Комментарий, Действия)
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels([
            "ID", "Дата/время", "Кандидат", "Результат",
            "Длительность (мин)", "Комментарий", "Действия"
        ])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # Устанавливаем режим растяжения для всех столбцов
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # Запрещаем редактирование
        table.setEditTriggers(QTableWidget.NoEditTriggers) # type: ignore
        # Затем для столбца 0 (ID) устанавливаем фиксированный режим и задаём ширину
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        table.setColumnWidth(0, 20)  # ширина в пикселях 

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


    def setup_statistics_table(self):
        table = self.ui.tableStatistics
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["Показатель", "Значение"])
        # Запрещаем редактирование
        table.setEditTriggers(QTableWidget.NoEditTriggers) # type: ignore
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # Устанавливаем режим растяжения для всех столбцов
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.populate_statistics()

    def populate_statistics(self):
        # Здесь вы получаете данные из журнала (пока из тестовых)
        # В реальном проекте — из базы данных
        data = [
            ("Всего звонков", "120"),
            ("Дозвонились", "80"),
            ("Не дозвонились", "40"),
            ("Заинтересованы", "45"),
            ("Приглашены на собеседование", "20"),
            ("Отказов", "10"),
            ("Нанято", "5"),
            ("Средняя длительность", "6.2 мин"),
            ("Эффективность", "25%"),
        ]
        table = self.ui.tableStatistics
        table.setRowCount(len(data))
        for row, (label, value) in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(label))
            table.setItem(row, 1, QTableWidgetItem(value))

    def setup_candidates_table(self):
        table = self.ui.tableCandidates   # objectName из дизайнера
        table.setColumnCount(8)
        table.setHorizontalHeaderLabels([
            "ID", "ФИО", "Телефон", "Email", 
            "Статус", "Источник", "Комментарий", "Резюме"
        ])
        # Запрещаем редактирование (опционально, если нужно)
        table.setEditTriggers(QTableWidget.NoEditTriggers) # type: ignore
        
        header = table.horizontalHeader()
        # Столбец ID – узкий
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        table.setColumnWidth(0, 50)
        # Остальные столбцы – растягиваются равномерно
        for col in range(1, 8):
            header.setSectionResizeMode(col, QHeaderView.ResizeMode.Stretch)
        
        self.populate_candidates()

    def populate_candidates(self):
        table = self.ui.tableCandidates
        test_data = [
            (1, "Иванов Иван Иванович", "+7-999-111-22-33", "ivanov@mail.ru", 
            "В работе", "HH.ru", "Обсуждали зарплату", "https://cloud.ru/resume1.pdf"),
            (2, "Петрова Мария Сергеевна", "+7-999-222-33-44", "petrova@mail.ru", 
            "Новый", "LinkedIn", "Ждёт ответа", ""),
            (3, "Сидоров Алексей Петрович", "+7-999-333-44-55", "sidorov@mail.ru", 
            "Собеседование", "Работа.ру", "Назначена встреча", "https://cloud.ru/resume3.pdf"),
            (4, "Козлова Анна Дмитриевна", "+7-999-444-55-66", "kozlova@mail.ru", 
            "Отказ", "Рекомендация", "Не подходит график", ""),
            (5, "Николаев Дмитрий Викторович", "+7-999-555-66-77", "nikolaev@mail.ru", 
            "Нанят", "HH.ru", "Принят на позицию разработчика", "https://cloud.ru/resume5.pdf"),
        ]
        table.setRowCount(len(test_data))
        for row, data in enumerate(test_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                table.setItem(row, col, item)
