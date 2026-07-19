# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panel2.ui'
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
        MainWindow.resize(1713, 1138)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background:qlineargradient(spread:pad, x1:1, y1:0.016, x2:0.699809, y2:0.014, stop:0 rgba(114, 159, 167, 80), stop:0.353234 rgba(0, 0, 0, 218))")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(400, 600))
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leftPanel = QWidget(self.centralwidget)
        self.leftPanel.setObjectName(u"leftPanel")
        self.leftPanel.setMinimumSize(QSize(400, 600))
        self.leftPanel.setMaximumSize(QSize(410, 16777215))
        self.leftPanel.setStyleSheet(u"background: black;")
        self.verticalLayout = QVBoxLayout(self.leftPanel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.leftPanel)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u"app/images/Group 2.png"))

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.leftPanel)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(310, 0))
        self.label_4.setPixmap(QPixmap(u"app/images/Control panel.png"))

        self.verticalLayout.addWidget(self.label_4)

        self.navigation = QWidget(self.leftPanel)
        self.navigation.setObjectName(u"navigation")
        sizePolicy.setHeightForWidth(self.navigation.sizePolicy().hasHeightForWidth())
        self.navigation.setSizePolicy(sizePolicy)
        self.navigation.setMaximumSize(QSize(700, 16777215))
        self.navigation.setStyleSheet(u"background: none;")
        self.verticalLayout_2 = QVBoxLayout(self.navigation)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.company = QPushButton(self.navigation)
        self.company.setObjectName(u"company")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.company.sizePolicy().hasHeightForWidth())
        self.company.setSizePolicy(sizePolicy1)
        self.company.setMinimumSize(QSize(100, 60))
        self.company.setMaximumSize(QSize(260, 90))
        self.company.setStyleSheet(u"QPushButton {\n"
"color: rgb(219, 255, 252);\n"
"background-color: rgba(61, 60, 61, 227);\n"
"border: 1px solid rgba(183, 245, 255, 100);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(120, 155, 155, 179)\n"
"}")

        self.verticalLayout_2.addWidget(self.company)

        self.vacancy = QPushButton(self.navigation)
        self.vacancy.setObjectName(u"vacancy")
        sizePolicy1.setHeightForWidth(self.vacancy.sizePolicy().hasHeightForWidth())
        self.vacancy.setSizePolicy(sizePolicy1)
        self.vacancy.setMinimumSize(QSize(100, 60))
        self.vacancy.setMaximumSize(QSize(260, 90))
        self.vacancy.setStyleSheet(u"QPushButton {\n"
"color: rgb(219, 255, 252);\n"
"background-color: rgba(61, 60, 61, 227);\n"
"border: 1px solid rgba(183, 245, 255, 100);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(120, 155, 155, 179)\n"
"}")

        self.verticalLayout_2.addWidget(self.vacancy)

        self.candidates = QPushButton(self.navigation)
        self.candidates.setObjectName(u"candidates")
        sizePolicy1.setHeightForWidth(self.candidates.sizePolicy().hasHeightForWidth())
        self.candidates.setSizePolicy(sizePolicy1)
        self.candidates.setMinimumSize(QSize(100, 60))
        self.candidates.setMaximumSize(QSize(260, 90))
        self.candidates.setStyleSheet(u"QPushButton {\n"
"color: rgb(219, 255, 252);\n"
"background-color: rgba(61, 60, 61, 227);\n"
"border: 1px solid rgba(183, 245, 255, 100);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(120, 155, 155, 179)\n"
"}")

        self.verticalLayout_2.addWidget(self.candidates)

        self.callLog = QPushButton(self.navigation)
        self.callLog.setObjectName(u"callLog")
        sizePolicy1.setHeightForWidth(self.callLog.sizePolicy().hasHeightForWidth())
        self.callLog.setSizePolicy(sizePolicy1)
        self.callLog.setMinimumSize(QSize(100, 60))
        self.callLog.setMaximumSize(QSize(260, 90))
        self.callLog.setStyleSheet(u"QPushButton {\n"
"color: rgb(219, 255, 252);\n"
"background-color: rgba(61, 60, 61, 227);\n"
"border: 1px solid rgba(183, 245, 255, 100);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(120, 155, 155, 179)\n"
"}")

        self.verticalLayout_2.addWidget(self.callLog)

        self.reportCall = QPushButton(self.navigation)
        self.reportCall.setObjectName(u"reportCall")
        sizePolicy1.setHeightForWidth(self.reportCall.sizePolicy().hasHeightForWidth())
        self.reportCall.setSizePolicy(sizePolicy1)
        self.reportCall.setMinimumSize(QSize(100, 60))
        self.reportCall.setMaximumSize(QSize(260, 90))
        self.reportCall.setStyleSheet(u"QPushButton {\n"
"color: rgb(219, 255, 252);\n"
"background-color: rgba(61, 60, 61, 227);\n"
"border: 1px solid rgba(183, 245, 255, 100);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(120, 155, 155, 179)\n"
"}")

        self.verticalLayout_2.addWidget(self.reportCall)

        self.callStatistic = QPushButton(self.navigation)
        self.callStatistic.setObjectName(u"callStatistic")
        sizePolicy1.setHeightForWidth(self.callStatistic.sizePolicy().hasHeightForWidth())
        self.callStatistic.setSizePolicy(sizePolicy1)
        self.callStatistic.setMinimumSize(QSize(100, 60))
        self.callStatistic.setMaximumSize(QSize(260, 90))
        self.callStatistic.setStyleSheet(u"QPushButton {\n"
"color: rgb(219, 255, 252);\n"
"background-color: rgba(61, 60, 61, 227);\n"
"border: 1px solid rgba(183, 245, 255, 100);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(120, 155, 155, 179)\n"
"}")

        self.verticalLayout_2.addWidget(self.callStatistic)


        self.verticalLayout.addWidget(self.navigation)


        self.horizontalLayout_2.addWidget(self.leftPanel)

        self.rightPanel = QWidget(self.centralwidget)
        self.rightPanel.setObjectName(u"rightPanel")
        sizePolicy.setHeightForWidth(self.rightPanel.sizePolicy().hasHeightForWidth())
        self.rightPanel.setSizePolicy(sizePolicy)
        self.rightPanel.setStyleSheet(u"background: rgba(254, 253, 255, 0)")
        self.horizontalLayout = QHBoxLayout(self.rightPanel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.rightPanel)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(800, 800))
        self.stackedWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.stackedWidget.setAutoFillBackground(False)
        self.companyPage = QWidget()
        self.companyPage.setObjectName(u"companyPage")
        self.stackedWidget.addWidget(self.companyPage)
        self.vacancyPage = QWidget()
        self.vacancyPage.setObjectName(u"vacancyPage")
        self.stackedWidget.addWidget(self.vacancyPage)
        self.reportCallPage = QWidget()
        self.reportCallPage.setObjectName(u"reportCallPage")
        self.stackedWidget.addWidget(self.reportCallPage)
        self.statisticCallPage = QWidget()
        self.statisticCallPage.setObjectName(u"statisticCallPage")
        self.stackedWidget.addWidget(self.statisticCallPage)
        self.welcomePage = QWidget()
        self.welcomePage.setObjectName(u"welcomePage")
        self.textBrowser = QTextBrowser(self.welcomePage)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(200, 300, 881, 361))
        self.textBrowser.setStyleSheet(u"background: rgba(204, 248, 255, 43);\n"
"border-radius: 7px;")
        self.stackedWidget.addWidget(self.welcomePage)
        self.callLogPage = QWidget()
        self.callLogPage.setObjectName(u"callLogPage")
        sizePolicy.setHeightForWidth(self.callLogPage.sizePolicy().hasHeightForWidth())
        self.callLogPage.setSizePolicy(sizePolicy)
        self.widget_3 = QWidget(self.callLogPage)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(-20, 20, 1221, 1061))
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 40, 58, 16))
        self.dateFrom = QDateEdit(self.widget_3)
        self.dateFrom.setObjectName(u"dateFrom")
        self.dateFrom.setGeometry(QRect(40, 60, 110, 22))
        self.dateFrom.setCalendarPopup(True)
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 40, 58, 16))
        self.dateFor = QDateEdit(self.widget_3)
        self.dateFor.setObjectName(u"dateFor")
        self.dateFor.setGeometry(QRect(160, 60, 110, 22))
        self.dateFor.setCalendarPopup(True)
        self.candidat = QLabel(self.widget_3)
        self.candidat.setObjectName(u"candidat")
        self.candidat.setGeometry(QRect(280, 40, 81, 16))
        self.candidateEdit = QLineEdit(self.widget_3)
        self.candidateEdit.setObjectName(u"candidateEdit")
        self.candidateEdit.setGeometry(QRect(280, 60, 321, 21))
        self.btnApplyFilter = QPushButton(self.widget_3)
        self.btnApplyFilter.setObjectName(u"btnApplyFilter")
        self.btnApplyFilter.setGeometry(QRect(660, 60, 100, 30))
        sizePolicy.setHeightForWidth(self.btnApplyFilter.sizePolicy().hasHeightForWidth())
        self.btnApplyFilter.setSizePolicy(sizePolicy)
        self.btnApplyFilter.setMinimumSize(QSize(100, 30))
        self.btnApplyFilter.setMaximumSize(QSize(100, 30))
        self.btnApplyFilter.setStyleSheet(u"\n"
"QPushButton {\n"
"background:rgba(218, 255, 255, 230);\n"
"color: black;\n"
"border: 1px solid rgb(205, 239, 255);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white\n"
"}")
        self.btnResetFilter = QPushButton(self.widget_3)
        self.btnResetFilter.setObjectName(u"btnResetFilter")
        self.btnResetFilter.setGeometry(QRect(780, 60, 100, 30))
        sizePolicy.setHeightForWidth(self.btnResetFilter.sizePolicy().hasHeightForWidth())
        self.btnResetFilter.setSizePolicy(sizePolicy)
        self.btnResetFilter.setMinimumSize(QSize(100, 30))
        self.btnResetFilter.setMaximumSize(QSize(100, 30))
        self.btnResetFilter.setStyleSheet(u"\n"
"QPushButton {\n"
"background:rgba(218, 255, 255, 230);\n"
"color: black;\n"
"border: 1px solid rgb(205, 239, 255);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: white\n"
"}")
        self.tableLog = QTableWidget(self.widget_3)
        self.tableLog.setObjectName(u"tableLog")
        self.tableLog.setGeometry(QRect(40, 120, 1181, 881))
        self.tableLog.setColumnCount(0)
        self.stackedWidget.addWidget(self.callLogPage)
        self.candidatesPage = QWidget()
        self.candidatesPage.setObjectName(u"candidatesPage")
        sizePolicy.setHeightForWidth(self.candidatesPage.sizePolicy().hasHeightForWidth())
        self.candidatesPage.setSizePolicy(sizePolicy)
        self.widget = QWidget(self.candidatesPage)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 60, 1200, 800))
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(800, 800))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.search = QLineEdit(self.widget)
        self.search.setObjectName(u"search")
        sizePolicy1.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.search)

        self.tableCandidates = QTableWidget(self.widget)
        if (self.tableCandidates.columnCount() < 7):
            self.tableCandidates.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableCandidates.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableCandidates.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableCandidates.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableCandidates.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableCandidates.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableCandidates.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableCandidates.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableCandidates.setObjectName(u"tableCandidates")
        self.tableCandidates.setStyleSheet(u"background: rgba(50, 65, 67, 56);")
        self.tableCandidates.setColumnCount(7)

        self.verticalLayout_3.addWidget(self.tableCandidates)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 90))
        self.addCandidate = QPushButton(self.widget_2)
        self.addCandidate.setObjectName(u"addCandidate")
        self.addCandidate.setGeometry(QRect(60, 20, 161, 41))
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
        self.editCandidate = QPushButton(self.widget_2)
        self.editCandidate.setObjectName(u"editCandidate")
        self.editCandidate.setGeometry(QRect(240, 20, 161, 41))
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
        self.deleteCandidate = QPushButton(self.widget_2)
        self.deleteCandidate.setObjectName(u"deleteCandidate")
        self.deleteCandidate.setGeometry(QRect(420, 20, 161, 41))
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

        self.verticalLayout_3.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.candidatesPage)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.rightPanel)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Call Tracking", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.company.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u0438", None))
        self.vacancy.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438", None))
        self.candidates.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u044b", None))
        self.callLog.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0437\u0432\u043e\u043d\u043a\u043e\u0432", None))
        self.reportCall.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442 \u043f\u043e \u0437\u0432\u043e\u043d\u043a\u0430\u043c", None))
        self.callStatistic.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u0437\u0432\u043e\u043d\u043a\u043e\u0432", None))
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
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" marg"
                        "in-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- \u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u044b \u2013 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0431\u0430\u0437\u043e\u0439 \u043a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u043e\u0432 (\u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435, \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435, \u043f\u043e\u0438\u0441\u043a).</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- \u0416\u0443\u0440\u043d\u0430\u043b \u0437\u0432\u043e\u043d\u043a\u043e\u0432 \u2013 \u0438\u0441\u0442\u043e\u0440\u0438\u044f \u0432\u0441\u0435\u0445 \u0437\u0432\u043e\u043d\u043a\u043e\u0432 \u0441 \u0444\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u0435\u0439.</span></p>\n"
"<p align=\"c"
                        "enter\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- \u041a\u043e\u043c\u043f\u0430\u043d\u0438\u0438 \u2013 \u0441\u043f\u0438\u0441\u043e\u043a \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0439-\u0440\u0430\u0431\u043e\u0442\u043e\u0434\u0430\u0442\u0435\u043b\u0435\u0439.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- \u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438 \u2013 \u043e\u0442\u043a\u0440\u044b\u0442\u044b\u0435 \u0432\u0430\u043a\u0430\u043d\u0441\u0438\u0438.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- \u041e\u0442\u0447\u0451\u0442 \u2013 \u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u043e\u0442\u0447"
                        "\u0451\u0442\u043e\u0432 \u043f\u043e \u0437\u0432\u043e\u043d\u043a\u0430\u043c.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">- \u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u2013 \u0430\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430 \u044d\u0444\u0444\u0435\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u0438.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u0414\u043b\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0440\u0430\u0431\u043e\u0442\u044b \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u043d\u0443\u0436\u043d"
                        "\u0443\u044e \u043a\u043d\u043e\u043f\u043a\u0443 \u0441\u043b\u0435\u0432\u0430.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0441:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e:", None))
        self.candidat.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442:", None))
        self.candidateEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0424\u0418\u041e", None))
        self.btnApplyFilter.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.btnResetFilter.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u0430:", None))
        self.search.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0438\u043b\u0438 \u0442\u0435\u043b\u0435\u0444\u043e\u043d", None))
        ___qtablewidgetitem = self.tableCandidates.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem1 = self.tableCandidates.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None))
        ___qtablewidgetitem2 = self.tableCandidates.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None))
        ___qtablewidgetitem3 = self.tableCandidates.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        ___qtablewidgetitem4 = self.tableCandidates.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        ___qtablewidgetitem5 = self.tableCandidates.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        ___qtablewidgetitem6 = self.tableCandidates.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.addCandidate.setText(QCoreApplication.translate("MainWindow", u"\u2795 \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u0430", None))
        self.editCandidate.setText(QCoreApplication.translate("MainWindow", u"\u270f\ufe0f \u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.deleteCandidate.setText(QCoreApplication.translate("MainWindow", u"\U0001f5d1\U0000fe0f \U00000423\U00000434\U00000430\U0000043b\U00000438\U00000442\U0000044c", None))
    # retranslateUi

