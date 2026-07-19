# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSplitter, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1120, 762)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-80, 0, 1284, 764))
        self.label.setPixmap(QPixmap(u"app/images/11.png"))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(460, 580, 180, 55))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color:rgba(133, 132, 134, 199);\n"
"border-radius: 9px;\n"
"border: 1px solid rgba(254, 253, 255, 112);\n"
"font-family: \"Gill Sans\", sans-serif;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: black;\n"
"background-color:rgba(255, 255, 255, 181);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255, 70);\n"
"}")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(460, 640, 180, 55))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color:rgba(133, 132, 134, 199);\n"
"border-radius: 9px;\n"
"border: 1px solid rgba(254, 253, 255, 112);\n"
"font-family: \"Gill Sans\", sans-serif;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: black;\n"
"background-color:rgba(255, 255, 255, 181);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255, 70);\n"
"}")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(360, 420, 381, 101))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.login = QLabel(self.splitter)
        self.login.setObjectName(u"login")
        self.login.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.login.setStyleSheet(u"color: black;\n"
"border: 1px solid white;\n"
"background-color: rgba(255, 255, 255, 222);\n"
"padding: 5px;")
        self.login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter.addWidget(self.login)
        self.enterLogin = QLineEdit(self.splitter)
        self.enterLogin.setObjectName(u"enterLogin")
        self.enterLogin.setStyleSheet(u"background-color: rgba(51, 51, 51, 242);")
        self.splitter.addWidget(self.enterLogin)

        self.verticalLayout.addWidget(self.splitter)

        self.splitter_2 = QSplitter(self.widget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.login_2 = QLabel(self.splitter_2)
        self.login_2.setObjectName(u"login_2")
        self.login_2.setStyleSheet(u"color: black;\n"
"border: 1px solid white;\n"
"background-color: rgba(255, 255, 255, 222);\n"
"padding: 5px;")
        self.login_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter_2.addWidget(self.login_2)
        self.enterLogin_2 = QLineEdit(self.splitter_2)
        self.enterLogin_2.setObjectName(u"enterLogin_2")
        self.enterLogin_2.setStyleSheet(u"background-color: rgba(51, 51, 51, 242);")
        self.splitter_2.addWidget(self.enterLogin_2)

        self.verticalLayout.addWidget(self.splitter_2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 380, 501, 181))
        self.label_2.setStyleSheet(u"background-color: rgba(254, 253, 255, 100);\n"
"border-radius: 9px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.widget.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.login.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.login_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.label_2.setText("")
    # retranslateUi

