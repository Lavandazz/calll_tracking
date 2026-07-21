# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panel3.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1279, 918)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(90, 174, 190, 78), stop:0.353234 rgba(0, 0, 0, 218))")
        self.verticalLayout_10 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftPanel = QWidget(self.centralwidget)
        self.leftPanel.setObjectName(u"leftPanel")
        sizePolicy.setHeightForWidth(self.leftPanel.sizePolicy().hasHeightForWidth())
        self.leftPanel.setSizePolicy(sizePolicy)
        self.leftPanel.setMaximumSize(QSize(405, 16777215))
        self.leftPanel.setStyleSheet(u"background-color: none;")
        self.verticalLayout_5 = QVBoxLayout(self.leftPanel)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.CRMlabel = QLabel(self.leftPanel)
        self.CRMlabel.setObjectName(u"CRMlabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.CRMlabel.sizePolicy().hasHeightForWidth())
        self.CRMlabel.setSizePolicy(sizePolicy1)
        self.CRMlabel.setPixmap(QPixmap(u"app/images/Group 2.png"))

        self.verticalLayout_5.addWidget(self.CRMlabel)

        self.CPlabel = QLabel(self.leftPanel)
        self.CPlabel.setObjectName(u"CPlabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.CPlabel.sizePolicy().hasHeightForWidth())
        self.CPlabel.setSizePolicy(sizePolicy2)
        self.CPlabel.setMinimumSize(QSize(0, 0))
        self.CPlabel.setMaximumSize(QSize(16777215, 60))
        self.CPlabel.setPixmap(QPixmap(u"app/images/Control panel.png"))

        self.verticalLayout_5.addWidget(self.CPlabel)

        self.company = QPushButton(self.leftPanel)
        self.company.setObjectName(u"company")
        sizePolicy1.setHeightForWidth(self.company.sizePolicy().hasHeightForWidth())
        self.company.setSizePolicy(sizePolicy1)
        self.company.setMinimumSize(QSize(100, 60))
        self.company.setMaximumSize(QSize(260, 90))
        self.company.setStyleSheet(u"QPushButton {\n"
"color: rgb(219, 255, 252);\n"
"background-color: black;\n"
"border: 1px solid qlineargradient(spread:pad, x1:0.691334, y1:0, x2:0, y2:0, stop:0 rgba(90, 174, 190, 78), stop:0.353234 rgba(0, 0, 0, 218));\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(120, 155, 155, 179)\n"
"}")

        self.verticalLayout_5.addWidget(self.company)

        self.vacancy = QPushButton(self.leftPanel)
        self.vacancy.setObjectName(u"vacancy")
        sizePolicy1.setHeightForWidth(self.vacancy.sizePolicy().hasHeightForWidth())
        self.vacancy.setSizePolicy(sizePolicy1)
        self.vacancy.setMinimumSize(QSize(100, 60))
        self.vacancy.setMaximumSize(QSize(260, 90))
        self.vacancy.setStyleSheet(u"QPushButton {\n"
"color: rgb(219, 255, 252);\n"
"background-color: black;\n"
"border: 1px solid qlineargradient(spread:pad, x1:0.691334, y1:0, x2:0, y2:0, stop:0 rgba(90, 174, 190, 78), stop:0.353234 rgba(0, 0, 0, 218));\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(120, 155, 155, 179)\n"
"}")

        self.verticalLayout_5.addWidget(self.vacancy)

        self.candidates = QPushButton(self.leftPanel)
        self.candidates.setObjectName(u"candidates")
        sizePolicy1.setHeightForWidth(self.candidates.sizePolicy().hasHeightForWidth())
        self.candidates.setSizePolicy(sizePolicy1)
        self.candidates.setMinimumSize(QSize(100, 60))
        self.candidates.setMaximumSize(QSize(260, 90))
        self.candidates.setStyleSheet(u"QPushButton {\n"
"color: rgb(219, 255, 252);\n"
"background-color: black;\n"
"border: 1px solid qlineargradient(spread:pad, x1:0.691334, y1:0, x2:0, y2:0, stop:0 rgba(90, 174, 190, 78), stop:0.353234 rgba(0, 0, 0, 218));\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(120, 155, 155, 179)\n"
"}")

        self.verticalLayout_5.addWidget(self.candidates)

        self.callStatistic = QPushButton(self.leftPanel)
        self.callStatistic.setObjectName(u"callStatistic")
        sizePolicy1.setHeightForWidth(self.callStatistic.sizePolicy().hasHeightForWidth())
        self.callStatistic.setSizePolicy(sizePolicy1)
        self.callStatistic.setMinimumSize(QSize(100, 60))
        self.callStatistic.setMaximumSize(QSize(260, 90))
        self.callStatistic.setStyleSheet(u"QPushButton {\n"
"color: rgb(219, 255, 252);\n"
"background-color: black;\n"
"border: 1px solid qlineargradient(spread:pad, x1:0.691334, y1:0, x2:0, y2:0, stop:0 rgba(90, 174, 190, 78), stop:0.353234 rgba(0, 0, 0, 218));\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(120, 155, 155, 179)\n"
"}")

        self.verticalLayout_5.addWidget(self.callStatistic)

        self.callLog = QPushButton(self.leftPanel)
        self.callLog.setObjectName(u"callLog")
        sizePolicy1.setHeightForWidth(self.callLog.sizePolicy().hasHeightForWidth())
        self.callLog.setSizePolicy(sizePolicy1)
        self.callLog.setMinimumSize(QSize(100, 60))
        self.callLog.setMaximumSize(QSize(260, 90))
        self.callLog.setStyleSheet(u"QPushButton {\n"
"color: rgb(219, 255, 252);\n"
"background-color: black;\n"
"border: 1px solid qlineargradient(spread:pad, x1:0.691334, y1:0, x2:0, y2:0, stop:0 rgba(90, 174, 190, 78), stop:0.353234 rgba(0, 0, 0, 218));\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(120, 155, 155, 179)\n"
"}")

        self.verticalLayout_5.addWidget(self.callLog)


        self.horizontalLayout.addWidget(self.leftPanel)

        self.rightPanel = QWidget(self.centralwidget)
        self.rightPanel.setObjectName(u"rightPanel")
        sizePolicy.setHeightForWidth(self.rightPanel.sizePolicy().hasHeightForWidth())
        self.rightPanel.setSizePolicy(sizePolicy)
        self.rightPanel.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.verticalLayout_6 = QVBoxLayout(self.rightPanel)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.rightPanel)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.welcomePage = QWidget()
        self.welcomePage.setObjectName(u"welcomePage")
        self.verticalLayout_20 = QVBoxLayout(self.welcomePage)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.textBrowser = QTextBrowser(self.welcomePage)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.textBrowser.setStyleSheet(u"background: rgba(204, 248, 255, 43);\n"
"border-radius: 7px;")

        self.verticalLayout_20.addWidget(self.textBrowser)

        self.stackedWidget.addWidget(self.welcomePage)
        self.companyPage = QWidget()
        self.companyPage.setObjectName(u"companyPage")
        self.verticalLayout_7 = QVBoxLayout(self.companyPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.candidat = QLabel(self.companyPage)
        self.candidat.setObjectName(u"candidat")

        self.verticalLayout_7.addWidget(self.candidat)

        self.companyEdit = QLineEdit(self.companyPage)
        self.companyEdit.setObjectName(u"companyEdit")

        self.verticalLayout_7.addWidget(self.companyEdit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.tableCompany = QTableWidget(self.companyPage)
        self.tableCompany.setObjectName(u"tableCompany")
        self.tableCompany.setStyleSheet(u"")
        self.tableCompany.setColumnCount(0)

        self.verticalLayout_7.addWidget(self.tableCompany)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.addCompany = QPushButton(self.companyPage)
        self.addCompany.setObjectName(u"addCompany")
        self.addCompany.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"background:rgba(218, 255, 255, 230);\n"
"color: black;\n"
"border: 1px solid rgb(205, 239, 255);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white\n"
"}")

        self.horizontalLayout_15.addWidget(self.addCompany)

        self.editCompany = QPushButton(self.companyPage)
        self.editCompany.setObjectName(u"editCompany")
        self.editCompany.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"background:rgba(218, 255, 255, 230);\n"
"color: black;\n"
"border: 1px solid rgb(205, 239, 255);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white\n"
"}")

        self.horizontalLayout_15.addWidget(self.editCompany)

        self.deleteCompany = QPushButton(self.companyPage)
        self.deleteCompany.setObjectName(u"deleteCompany")
        self.deleteCompany.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"background:rgba(218, 255, 255, 230);\n"
"color: black;\n"
"border: 1px solid rgb(205, 239, 255);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white\n"
"}")

        self.horizontalLayout_15.addWidget(self.deleteCompany)


        self.verticalLayout_7.addLayout(self.horizontalLayout_15)

        self.verticalLayout_7.setStretch(3, 1)
        self.stackedWidget.addWidget(self.companyPage)
        self.vacancyPage = QWidget()
        self.vacancyPage.setObjectName(u"vacancyPage")
        self.verticalLayout_11 = QVBoxLayout(self.vacancyPage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.vacancySearch = QLabel(self.vacancyPage)
        self.vacancySearch.setObjectName(u"vacancySearch")

        self.verticalLayout_11.addWidget(self.vacancySearch)

        self.vacancyEdit = QLineEdit(self.vacancyPage)
        self.vacancyEdit.setObjectName(u"vacancyEdit")

        self.verticalLayout_11.addWidget(self.vacancyEdit)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnResetFilter_8 = QPushButton(self.vacancyPage)
        self.btnResetFilter_8.setObjectName(u"btnResetFilter_8")
        sizePolicy.setHeightForWidth(self.btnResetFilter_8.sizePolicy().hasHeightForWidth())
        self.btnResetFilter_8.setSizePolicy(sizePolicy)
        self.btnResetFilter_8.setMinimumSize(QSize(100, 30))
        self.btnResetFilter_8.setMaximumSize(QSize(100, 30))
        self.btnResetFilter_8.setStyleSheet(u"\n"
"QPushButton {\n"
"background:rgba(218, 255, 255, 230);\n"
"color: black;\n"
"border: 1px solid rgb(205, 239, 255);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white\n"
"}")

        self.horizontalLayout_4.addWidget(self.btnResetFilter_8)

        self.btnApplyFilter_8 = QPushButton(self.vacancyPage)
        self.btnApplyFilter_8.setObjectName(u"btnApplyFilter_8")
        sizePolicy.setHeightForWidth(self.btnApplyFilter_8.sizePolicy().hasHeightForWidth())
        self.btnApplyFilter_8.setSizePolicy(sizePolicy)
        self.btnApplyFilter_8.setMinimumSize(QSize(100, 30))
        self.btnApplyFilter_8.setMaximumSize(QSize(100, 30))
        self.btnApplyFilter_8.setStyleSheet(u"\n"
"QPushButton {\n"
"background:rgba(218, 255, 255, 230);\n"
"color: black;\n"
"border: 1px solid rgb(205, 239, 255);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white\n"
"}")

        self.horizontalLayout_4.addWidget(self.btnApplyFilter_8)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)

        self.tableVacancy = QTableWidget(self.vacancyPage)
        self.tableVacancy.setObjectName(u"tableVacancy")
        self.tableVacancy.setColumnCount(0)

        self.verticalLayout_11.addWidget(self.tableVacancy)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.addVacancy = QPushButton(self.vacancyPage)
        self.addVacancy.setObjectName(u"addVacancy")
        self.addVacancy.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"background:rgba(218, 255, 255, 230);\n"
"color: black;\n"
"border: 1px solid rgb(205, 239, 255);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white\n"
"}")

        self.horizontalLayout_16.addWidget(self.addVacancy)

        self.editVacancy = QPushButton(self.vacancyPage)
        self.editVacancy.setObjectName(u"editVacancy")
        self.editVacancy.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"background:rgba(218, 255, 255, 230);\n"
"color: black;\n"
"border: 1px solid rgb(205, 239, 255);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white\n"
"}")

        self.horizontalLayout_16.addWidget(self.editVacancy)

        self.deleteVacancy = QPushButton(self.vacancyPage)
        self.deleteVacancy.setObjectName(u"deleteVacancy")
        self.deleteVacancy.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"background:rgba(218, 255, 255, 230);\n"
"color: black;\n"
"border: 1px solid rgb(205, 239, 255);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white\n"
"}")

        self.horizontalLayout_16.addWidget(self.deleteVacancy)


        self.verticalLayout_11.addLayout(self.horizontalLayout_16)

        self.verticalLayout_11.setStretch(3, 1)
        self.stackedWidget.addWidget(self.vacancyPage)
        self.statisticPage = QWidget()
        self.statisticPage.setObjectName(u"statisticPage")
        self.verticalLayout_18 = QVBoxLayout(self.statisticPage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_6 = QLabel(self.statisticPage)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_18.addWidget(self.label_6)

        self.dateFrom = QDateEdit(self.statisticPage)
        self.dateFrom.setObjectName(u"dateFrom")
        self.dateFrom.setCalendarPopup(True)

        self.verticalLayout_18.addWidget(self.dateFrom)

        self.label_7 = QLabel(self.statisticPage)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_18.addWidget(self.label_7)

        self.dateFor = QDateEdit(self.statisticPage)
        self.dateFor.setObjectName(u"dateFor")
        self.dateFor.setCalendarPopup(True)

        self.verticalLayout_18.addWidget(self.dateFor)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.btnApplyFilter_12 = QPushButton(self.statisticPage)
        self.btnApplyFilter_12.setObjectName(u"btnApplyFilter_12")
        sizePolicy.setHeightForWidth(self.btnApplyFilter_12.sizePolicy().hasHeightForWidth())
        self.btnApplyFilter_12.setSizePolicy(sizePolicy)
        self.btnApplyFilter_12.setMinimumSize(QSize(100, 30))
        self.btnApplyFilter_12.setMaximumSize(QSize(100, 30))
        self.btnApplyFilter_12.setStyleSheet(u"\n"
"QPushButton {\n"
"background:rgba(218, 255, 255, 230);\n"
"color: black;\n"
"border: 1px solid rgb(205, 239, 255);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white\n"
"}")

        self.horizontalLayout_17.addWidget(self.btnApplyFilter_12)

        self.btnResetFilter_12 = QPushButton(self.statisticPage)
        self.btnResetFilter_12.setObjectName(u"btnResetFilter_12")
        sizePolicy.setHeightForWidth(self.btnResetFilter_12.sizePolicy().hasHeightForWidth())
        self.btnResetFilter_12.setSizePolicy(sizePolicy)
        self.btnResetFilter_12.setMinimumSize(QSize(100, 30))
        self.btnResetFilter_12.setMaximumSize(QSize(100, 30))
        self.btnResetFilter_12.setStyleSheet(u"\n"
"QPushButton {\n"
"background:rgba(218, 255, 255, 230);\n"
"color: black;\n"
"border: 1px solid rgb(205, 239, 255);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white\n"
"}")

        self.horizontalLayout_17.addWidget(self.btnResetFilter_12)


        self.verticalLayout_18.addLayout(self.horizontalLayout_17)

        self.tableStatistics = QTableWidget(self.statisticPage)
        self.tableStatistics.setObjectName(u"tableStatistics")
        self.tableStatistics.setColumnCount(0)

        self.verticalLayout_18.addWidget(self.tableStatistics)

        self.verticalLayout_18.setStretch(5, 1)
        self.stackedWidget.addWidget(self.statisticPage)
        self.candidatesPage = QWidget()
        self.candidatesPage.setObjectName(u"candidatesPage")
        self.verticalLayout_14 = QVBoxLayout(self.candidatesPage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.candidateSearch_2 = QLabel(self.candidatesPage)
        self.candidateSearch_2.setObjectName(u"candidateSearch_2")

        self.verticalLayout_14.addWidget(self.candidateSearch_2)

        self.candidateEdit = QLineEdit(self.candidatesPage)
        self.candidateEdit.setObjectName(u"candidateEdit")

        self.verticalLayout_14.addWidget(self.candidateEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnApplyFilter_9 = QPushButton(self.candidatesPage)
        self.btnApplyFilter_9.setObjectName(u"btnApplyFilter_9")
        sizePolicy.setHeightForWidth(self.btnApplyFilter_9.sizePolicy().hasHeightForWidth())
        self.btnApplyFilter_9.setSizePolicy(sizePolicy)
        self.btnApplyFilter_9.setMinimumSize(QSize(100, 30))
        self.btnApplyFilter_9.setMaximumSize(QSize(100, 30))
        self.btnApplyFilter_9.setStyleSheet(u"\n"
"QPushButton {\n"
"background:rgba(218, 255, 255, 230);\n"
"color: black;\n"
"border: 1px solid rgb(205, 239, 255);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnApplyFilter_9)

        self.btnResetFilter_9 = QPushButton(self.candidatesPage)
        self.btnResetFilter_9.setObjectName(u"btnResetFilter_9")
        sizePolicy.setHeightForWidth(self.btnResetFilter_9.sizePolicy().hasHeightForWidth())
        self.btnResetFilter_9.setSizePolicy(sizePolicy)
        self.btnResetFilter_9.setMinimumSize(QSize(100, 30))
        self.btnResetFilter_9.setMaximumSize(QSize(100, 30))
        self.btnResetFilter_9.setStyleSheet(u"\n"
"QPushButton {\n"
"background:rgba(218, 255, 255, 230);\n"
"color: black;\n"
"border: 1px solid rgb(205, 239, 255);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnResetFilter_9)


        self.verticalLayout_14.addLayout(self.horizontalLayout_2)

        self.tableCandidates = QTableWidget(self.candidatesPage)
        self.tableCandidates.setObjectName(u"tableCandidates")
        self.tableCandidates.setColumnCount(0)

        self.verticalLayout_14.addWidget(self.tableCandidates)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.addCandidate = QPushButton(self.candidatesPage)
        self.addCandidate.setObjectName(u"addCandidate")
        self.addCandidate.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"background:rgba(218, 255, 255, 230);\n"
"color: black;\n"
"border: 1px solid rgb(205, 239, 255);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white\n"
"}")

        self.horizontalLayout_10.addWidget(self.addCandidate)

        self.editCandidate = QPushButton(self.candidatesPage)
        self.editCandidate.setObjectName(u"editCandidate")
        self.editCandidate.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"background:rgba(218, 255, 255, 230);\n"
"color: black;\n"
"border: 1px solid rgb(205, 239, 255);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white\n"
"}")

        self.horizontalLayout_10.addWidget(self.editCandidate)

        self.deleteCandidate = QPushButton(self.candidatesPage)
        self.deleteCandidate.setObjectName(u"deleteCandidate")
        self.deleteCandidate.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"background:rgba(218, 255, 255, 230);\n"
"color: black;\n"
"border: 1px solid rgb(205, 239, 255);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white\n"
"}")

        self.horizontalLayout_10.addWidget(self.deleteCandidate)


        self.verticalLayout_14.addLayout(self.horizontalLayout_10)

        self.verticalLayout_14.setStretch(3, 1)
        self.stackedWidget.addWidget(self.candidatesPage)
        self.callLogPage = QWidget()
        self.callLogPage.setObjectName(u"callLogPage")
        self.verticalLayout_19 = QVBoxLayout(self.callLogPage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.tableLog = QTableWidget(self.callLogPage)
        self.tableLog.setObjectName(u"tableLog")
        self.tableLog.setColumnCount(0)

        self.horizontalLayout_18.addWidget(self.tableLog)


        self.verticalLayout_19.addLayout(self.horizontalLayout_18)

        self.stackedWidget.addWidget(self.callLogPage)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.rightPanel)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.CRMlabel.setText("")
        self.CPlabel.setText("")
        self.company.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u0438", None))
        self.vacancy.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438", None))
        self.candidates.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u044b", None))
        self.callStatistic.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u0437\u0432\u043e\u043d\u043a\u043e\u0432", None))
        self.callLog.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0437\u0432\u043e\u043d\u043a\u043e\u0432", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><spa"
                        "n style=\" font-size:18pt;\">\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432 CRM-\u0441\u0438\u0441\u0442\u0435\u043c\u0443 &quot;\u0420\u0435\u043a\u0440\u0443\u0442\u0435\u0440&quot;!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u0412 \u043b\u0435\u0432\u043e\u0439 \u043f\u0430\u043d\u0435\u043b\u0438 \u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043d\u0443\u0436\u043d\u044b\u0439 \u0440\u0430\u0437\u0434\u0435\u043b:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0p"
                        "x; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\"> </span><span style=\" font-size:14pt; font-weight:700;\">\u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u044b</span><span style=\" font-size:14pt;\"> \u2013 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0431\u0430\u0437\u043e\u0439 \u043a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u043e\u0432 (\u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435, \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435, \u043f\u043e\u0438\u0441\u043a).</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top"
                        ":0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">\u0416\u0443\u0440\u043d\u0430\u043b \u0437\u0432\u043e\u043d\u043a\u043e\u0432</span><span style=\" font-size:14pt;\"> \u2013 \u0438\u0441\u0442\u043e\u0440\u0438\u044f \u0432\u0441\u0435\u0445 \u0437\u0432\u043e\u043d\u043a\u043e\u0432 \u0441 \u0444\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u0435\u0439.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u0438</span><span style=\" font-size:14pt;\"> \u2013 \u0441\u043f\u0438\u0441\u043e\u043a \u043a\u043e\u043c\u043f\u0430\u043d"
                        "\u0438\u0439-\u0440\u0430\u0431\u043e\u0442\u043e\u0434\u0430\u0442\u0435\u043b\u0435\u0439.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438</span><span style=\" font-size:14pt;\"> \u2013 \u043e\u0442\u043a\u0440\u044b\u0442\u044b\u0435 \u0432\u0430\u043a\u0430\u043d\u0441\u0438\u0438.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                        "0px;\"><span style=\" font-size:14pt; font-weight:700;\">\u041e\u0442\u0447\u0451\u0442</span><span style=\" font-size:14pt;\"> \u2013 \u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u043e\u0442\u0447\u0451\u0442\u043e\u0432 \u043f\u043e \u0437\u0432\u043e\u043d\u043a\u0430\u043c.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430</span><span style=\" font-size:14pt;\"> \u2013 \u0430\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430 \u044d\u0444\u0444\u0435\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u0438.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bot"
                        "tom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u0414\u043b\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u043d\u0443\u0436\u043d\u0443\u044e \u043a\u043d\u043e\u043f\u043a\u0443 \u0441\u043b\u0435\u0432\u0430.</span></p></body></html>", None))
        self.candidat.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u044e \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438:", None))
        self.companyEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.addCompany.setText(QCoreApplication.translate("MainWindow", u"\u2795 \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.editCompany.setText(QCoreApplication.translate("MainWindow", u"\u270f\ufe0f \u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.deleteCompany.setText(QCoreApplication.translate("MainWindow", u"\U0001f5d1\U0000fe0f \U00000423\U00000434\U00000430\U0000043b\U00000438\U00000442\U0000044c", None))
        self.vacancySearch.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u044e \u0432\u0430\u043a\u0430\u043d\u0441\u0438\u0438:", None))
        self.vacancyEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.btnResetFilter_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.btnApplyFilter_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.addVacancy.setText(QCoreApplication.translate("MainWindow", u"\u2795 \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.editVacancy.setText(QCoreApplication.translate("MainWindow", u"\u270f\ufe0f \u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.deleteVacancy.setText(QCoreApplication.translate("MainWindow", u"\U0001f5d1\U0000fe0f \U00000423\U00000434\U00000430\U0000043b\U00000438\U00000442\U0000044c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0441:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e:", None))
        self.btnApplyFilter_12.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.btnResetFilter_12.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.candidateSearch_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u0430:", None))
        self.candidateEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0424\u0418\u041e", None))
        self.btnApplyFilter_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.btnResetFilter_9.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.addCandidate.setText(QCoreApplication.translate("MainWindow", u"\u2795 \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u0430", None))
        self.editCandidate.setText(QCoreApplication.translate("MainWindow", u"\u270f\ufe0f \u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.deleteCandidate.setText(QCoreApplication.translate("MainWindow", u"\U0001f5d1\U0000fe0f \U00000423\U00000434\U00000430\U0000043b\U00000438\U00000442\U0000044c", None))
    # retranslateUi

