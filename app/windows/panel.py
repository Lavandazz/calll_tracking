
from PySide6.QtWidgets import QHeaderView, QMainWindow, QTableWidget, QTableWidgetItem
from app.core.calll_service import CallService
from app.core.candidate_service import CandidateService
from app.core.company_service import CompanyService
from app.core.statistics_service import StatisticsService
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

                # Сервис для кандидатов
        self.candidate_service = CandidateService(
            table_widget=self.ui.tableCandidates,
            parent_widget=self,
            session_maker=session_maker
        )

        self.call_service = CallService(
            table_widget=self.ui.tableLog,
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


        # self.setup_statistics_table()
        # self.setup_candidates_table()

        # Подключаем кнопки добавления, редактирования и удаления компаний к методам CompanyService
        self.ui.addCompany.clicked.connect(self.company_service.add_company)
        self.ui.editCompany.clicked.connect(self.company_service.edit_company)
        self.ui.deleteCompany.clicked.connect(self.company_service.delete_company)

        self.ui.addVacancy.clicked.connect(self.vacancy_service.add_vacancy)
        self.ui.editVacancy.clicked.connect(self.vacancy_service.edit_vacancy)
        self.ui.deleteVacancy.clicked.connect(self.vacancy_service.delete_vacancy)

        self.ui.addCall.clicked.connect(self.call_service.add_call)       # предположим, есть кнопка
        self.ui.editCall.clicked.connect(self.call_service.edit_call)     # предположим, есть
        self.ui.deleteCall.clicked.connect(self.call_service.delete_call) # предположим, есть

        self.ui.addCandidate.clicked.connect(self.candidate_service.add_candidate)
        self.ui.editCandidate.clicked.connect(self.candidate_service.edit_candidate)
        self.ui.deleteCandidate.clicked.connect(self.candidate_service.delete_candidate)

        self.statistics_service = StatisticsService(
            table_widget=self.ui.tableStatistics,
            parent_widget=self,
            session_maker=session_maker
        )

        # Подключаем кнопки фильтрации (предполагаются имена btnDay, btnWeek, btnMonth, btnAll)
        self.ui.btnDay.clicked.connect(self.statistics_service.load_day)
        self.ui.btnWeek.clicked.connect(self.statistics_service.load_week)
        self.ui.btnMonth.clicked.connect(self.statistics_service.load_month)
        self.ui.btnAll.clicked.connect(self.statistics_service.load_all)


    def show_company(self):
        self.ui.company.clicked.connect(lambda: self.stacked.setCurrentWidget(self.ui.companyPage))
