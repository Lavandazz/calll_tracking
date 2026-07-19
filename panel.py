# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panel.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1245, 789)
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
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.left_panel = QWidget(self.centralwidget)
        self.left_panel.setObjectName(u"left_panel")
        self.left_panel.setMinimumSize(QSize(300, 600))
        self.left_panel.setMaximumSize(QSize(400, 16777215))
        self.left_panel.setStyleSheet(u"background: black;")
        self.verticalLayout = QVBoxLayout(self.left_panel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.left_panel)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u"app/images/Group 2.png"))

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.left_panel)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u"app/images/Control panel.png"))

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.left_panel)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setPixmap(QPixmap(u"app/images/02623ef3802e11f1be9b8664f542c61e_1.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)


        self.gridLayout_2.addWidget(self.left_panel, 0, 0, 1, 1)

        self.right_panel = QWidget(self.centralwidget)
        self.right_panel.setObjectName(u"right_panel")
        sizePolicy.setHeightForWidth(self.right_panel.sizePolicy().hasHeightForWidth())
        self.right_panel.setSizePolicy(sizePolicy)
        self.right_panel.setMaximumSize(QSize(700, 16777215))
        self.right_panel.setStyleSheet(u"background: none;")
        self.gridLayout = QGridLayout(self.right_panel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.reportCall = QPushButton(self.right_panel)
        self.reportCall.setObjectName(u"reportCall")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.reportCall.sizePolicy().hasHeightForWidth())
        self.reportCall.setSizePolicy(sizePolicy1)
        self.reportCall.setMinimumSize(QSize(100, 60))
        self.reportCall.setMaximumSize(QSize(260, 160))
        self.reportCall.setStyleSheet(u"QPushButton {\n"
"color: rgb(219, 255, 252);\n"
"background-color: rgba(61, 60, 61, 227);\n"
"border: 1px solid rgba(183, 245, 255, 100);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(120, 155, 155, 179)\n"
"}")

        self.gridLayout.addWidget(self.reportCall, 3, 0, 1, 1)

        self.company = QPushButton(self.right_panel)
        self.company.setObjectName(u"company")
        sizePolicy1.setHeightForWidth(self.company.sizePolicy().hasHeightForWidth())
        self.company.setSizePolicy(sizePolicy1)
        self.company.setMinimumSize(QSize(100, 60))
        self.company.setMaximumSize(QSize(260, 160))
        self.company.setStyleSheet(u"QPushButton {\n"
"color: rgb(219, 255, 252);\n"
"background-color: rgba(61, 60, 61, 227);\n"
"border: 1px solid rgba(183, 245, 255, 100);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(120, 155, 155, 179)\n"
"}")

        self.gridLayout.addWidget(self.company, 1, 0, 1, 1)

        self.candidates = QPushButton(self.right_panel)
        self.candidates.setObjectName(u"candidates")
        sizePolicy1.setHeightForWidth(self.candidates.sizePolicy().hasHeightForWidth())
        self.candidates.setSizePolicy(sizePolicy1)
        self.candidates.setMinimumSize(QSize(100, 60))
        self.candidates.setMaximumSize(QSize(260, 160))
        self.candidates.setStyleSheet(u"QPushButton {\n"
"color: rgb(219, 255, 252);\n"
"background-color: rgba(61, 60, 61, 227);\n"
"border: 1px solid rgba(183, 245, 255, 100);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(120, 155, 155, 179)\n"
"}")

        self.gridLayout.addWidget(self.candidates, 1, 1, 1, 1)

        self.vacancy = QPushButton(self.right_panel)
        self.vacancy.setObjectName(u"vacancy")
        sizePolicy1.setHeightForWidth(self.vacancy.sizePolicy().hasHeightForWidth())
        self.vacancy.setSizePolicy(sizePolicy1)
        self.vacancy.setMinimumSize(QSize(100, 60))
        self.vacancy.setMaximumSize(QSize(260, 160))
        self.vacancy.setStyleSheet(u"QPushButton {\n"
"color: rgb(219, 255, 252);\n"
"background-color: rgba(61, 60, 61, 227);\n"
"border: 1px solid rgba(183, 245, 255, 100);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(120, 155, 155, 179)\n"
"}")

        self.gridLayout.addWidget(self.vacancy, 4, 0, 1, 1)

        self.callLog = QPushButton(self.right_panel)
        self.callLog.setObjectName(u"callLog")
        sizePolicy1.setHeightForWidth(self.callLog.sizePolicy().hasHeightForWidth())
        self.callLog.setSizePolicy(sizePolicy1)
        self.callLog.setMinimumSize(QSize(100, 60))
        self.callLog.setMaximumSize(QSize(260, 160))
        self.callLog.setStyleSheet(u"QPushButton {\n"
"color: rgb(219, 255, 252);\n"
"background-color: rgba(61, 60, 61, 227);\n"
"border: 1px solid rgba(183, 245, 255, 100);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(120, 155, 155, 179)\n"
"}")

        self.gridLayout.addWidget(self.callLog, 3, 1, 1, 1)

        self.callStatisric = QPushButton(self.right_panel)
        self.callStatisric.setObjectName(u"callStatisric")
        sizePolicy1.setHeightForWidth(self.callStatisric.sizePolicy().hasHeightForWidth())
        self.callStatisric.setSizePolicy(sizePolicy1)
        self.callStatisric.setMinimumSize(QSize(100, 60))
        self.callStatisric.setMaximumSize(QSize(260, 160))
        self.callStatisric.setStyleSheet(u"QPushButton {\n"
"color: rgb(219, 255, 252);\n"
"background-color: rgba(61, 60, 61, 227);\n"
"border: 1px solid rgba(183, 245, 255, 100);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(120, 155, 155, 179)\n"
"}")

        self.gridLayout.addWidget(self.callStatisric, 4, 1, 1, 1)


        self.gridLayout_2.addWidget(self.right_panel, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Call Tracking", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.reportCall.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442", None))
        self.company.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u0438", None))
        self.candidates.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u044b", None))
        self.vacancy.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438", None))
        self.callLog.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b \u0437\u0432\u043e\u043d\u043a\u043e\u0432", None))
        self.callStatisric.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u0437\u0432\u043e\u043d\u043a\u043e\u0432", None))
    # retranslateUi

