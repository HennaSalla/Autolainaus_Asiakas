# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
import userUiRescources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 33, 72);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.takeCarPushButton = QPushButton(self.centralwidget)
        self.takeCarPushButton.setObjectName(u"takeCarPushButton")
        self.takeCarPushButton.setGeometry(QRect(290, 0, 331, 121))
        font = QFont()
        font.setPointSize(20)
        self.takeCarPushButton.setFont(font)
        self.takeCarPushButton.setStyleSheet(u"color: rgb(75, 188, 197);")
        self.returnCarPushButton = QPushButton(self.centralwidget)
        self.returnCarPushButton.setObjectName(u"returnCarPushButton")
        self.returnCarPushButton.setGeometry(QRect(680, 0, 311, 121))
        self.returnCarPushButton.setFont(font)
        self.returnCarPushButton.setStyleSheet(u"color: rgb(75, 188, 197);")
        self.humanLabel = QLabel(self.centralwidget)
        self.humanLabel.setObjectName(u"humanLabel")
        self.humanLabel.setGeometry(QRect(400, 180, 140, 210))
        self.humanLabel.setPixmap(QPixmap(u"uiPictrues/human.png"))
        self.humanLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.borrowerLabel = QLabel(self.centralwidget)
        self.borrowerLabel.setObjectName(u"borrowerLabel")
        self.borrowerLabel.setGeometry(QRect(410, 130, 131, 31))
        font1 = QFont()
        font1.setPointSize(18)
        self.borrowerLabel.setFont(font1)
        self.borrowerLabel.setStyleSheet(u"color: rgb(75, 188, 197);")
        self.carTakeLabel = QLabel(self.centralwidget)
        self.carTakeLabel.setObjectName(u"carTakeLabel")
        self.carTakeLabel.setGeometry(QRect(810, 140, 61, 31))
        self.carTakeLabel.setFont(font1)
        self.carTakeLabel.setStyleSheet(u"color: rgb(75, 188, 197);")
        self.carKeysLabel = QLabel(self.centralwidget)
        self.carKeysLabel.setObjectName(u"carKeysLabel")
        self.carKeysLabel.setGeometry(QRect(780, 190, 140, 210))
        self.carKeysLabel.setPixmap(QPixmap(u"uiPictrues/auto.png"))
        self.carKeysLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.clockPictureLabel = QLabel(self.centralwidget)
        self.clockPictureLabel.setObjectName(u"clockPictureLabel")
        self.clockPictureLabel.setGeometry(QRect(220, 170, 111, 91))
        self.clockPictureLabel.setPixmap(QPixmap(u"uiPictrues/clock.png"))
        self.clockPictureLabel.setScaledContents(True)
        self.clockPictureLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.keysLineEdit = QLineEdit(self.centralwidget)
        self.keysLineEdit.setObjectName(u"keysLineEdit")
        self.keysLineEdit.setGeometry(QRect(755, 410, 190, 51))
        font2 = QFont()
        font2.setFamilies([u"Trebuchet MS"])
        font2.setPointSize(24)
        font2.setBold(True)
        self.keysLineEdit.setFont(font2)
        self.keysLineEdit.setStyleSheet(u"color: rgb(7, 7, 7);\n"
"background-color: rgb(214, 213, 208);")
        self.keysLineEdit.setClearButtonEnabled(True)
        self.licenseLineEdit = QLineEdit(self.centralwidget)
        self.licenseLineEdit.setObjectName(u"licenseLineEdit")
        self.licenseLineEdit.setGeometry(QRect(380, 400, 201, 41))
        self.licenseLineEdit.setFont(font1)
        self.licenseLineEdit.setStyleSheet(u"color: rgb(75, 188, 197);")
        self.licenseLineEdit.setEchoMode(QLineEdit.EchoMode.NoEcho)
        self.licenseLineEdit.setClearButtonEnabled(True)
        self.calenderLabel = QLabel(self.centralwidget)
        self.calenderLabel.setObjectName(u"calenderLabel")
        self.calenderLabel.setGeometry(QRect(60, 170, 111, 91))
        self.calenderLabel.setPixmap(QPixmap(u"uiPictrues/calender.png"))
        self.calenderLabel.setScaledContents(True)
        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setGeometry(QRect(50, 280, 141, 21))
        self.dateLabel.setFont(font1)
        self.dateLabel.setStyleSheet(u"color: rgb(75, 188, 197);")
        self.goBackPushButton = QPushButton(self.centralwidget)
        self.goBackPushButton.setObjectName(u"goBackPushButton")
        self.goBackPushButton.setGeometry(QRect(1140, 610, 211, 91))
        self.goBackPushButton.setFont(font)
        self.goBackPushButton.setStyleSheet(u"color: rgb(75, 188, 197);")
        self.hourLabel = QLabel(self.centralwidget)
        self.hourLabel.setObjectName(u"hourLabel")
        self.hourLabel.setGeometry(QRect(240, 280, 61, 21))
        self.hourLabel.setFont(font1)
        self.hourLabel.setStyleSheet(u"color: rgb(75, 188, 197);")
        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(400, 450, 161, 41))
        self.nameLabel.setFont(font1)
        self.nameLabel.setStyleSheet(u"color: rgb(75, 188, 197);")
        self.carInfoLabel = QLabel(self.centralwidget)
        self.carInfoLabel.setObjectName(u"carInfoLabel")
        self.carInfoLabel.setGeometry(QRect(740, 470, 211, 81))
        self.carInfoLabel.setFont(font1)
        self.carInfoLabel.setStyleSheet(u"color: rgb(75, 188, 197);")
        self.okPushButton = QPushButton(self.centralwidget)
        self.okPushButton.setObjectName(u"okPushButton")
        self.okPushButton.setGeometry(QRect(1140, 480, 211, 91))
        self.okPushButton.setFont(font)
        self.okPushButton.setStyleSheet(u"color: rgb(75, 188, 197);")
        self.keysReturnLineEdit = QLineEdit(self.centralwidget)
        self.keysReturnLineEdit.setObjectName(u"keysReturnLineEdit")
        self.keysReturnLineEdit.setGeometry(QRect(575, 410, 190, 51))
        self.keysReturnLineEdit.setFont(font2)
        self.keysReturnLineEdit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(214, 213, 208);")
        self.keysReturnLineEdit.setClearButtonEnabled(True)
        self.carKeysReturnLabel = QLabel(self.centralwidget)
        self.carKeysReturnLabel.setObjectName(u"carKeysReturnLabel")
        self.carKeysReturnLabel.setGeometry(QRect(600, 180, 140, 210))
        self.carKeysReturnLabel.setPixmap(QPixmap(u"uiPictrues/auto.png"))
        self.carKeysReturnLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.carTakeReturnLabel = QLabel(self.centralwidget)
        self.carTakeReturnLabel.setObjectName(u"carTakeReturnLabel")
        self.carTakeReturnLabel.setGeometry(QRect(630, 130, 61, 31))
        self.carTakeReturnLabel.setFont(font1)
        self.carTakeReturnLabel.setStyleSheet(u"color: rgb(75, 188, 197);")
        self.freeCarLabel = QLabel(self.centralwidget)
        self.freeCarLabel.setObjectName(u"freeCarLabel")
        self.freeCarLabel.setGeometry(QRect(310, 120, 151, 31))
        self.freeCarLabel.setFont(font1)
        self.freeCarLabel.setStyleSheet(u"color: rgb(75, 188, 197);")
        self.freeCarLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.drivingCarLabel = QLabel(self.centralwidget)
        self.drivingCarLabel.setObjectName(u"drivingCarLabel")
        self.drivingCarLabel.setGeometry(QRect(890, 120, 81, 31))
        self.drivingCarLabel.setFont(font1)
        self.drivingCarLabel.setStyleSheet(u"color: rgb(75, 188, 197);")
        self.soundCheckBox = QCheckBox(self.centralwidget)
        self.soundCheckBox.setObjectName(u"soundCheckBox")
        self.soundCheckBox.setGeometry(QRect(1260, 20, 91, 81))
        self.soundCheckBox.setStyleSheet(u"background-color: rgb(0, 33, 72);")
        icon = QIcon()
        icon.addFile(u"uiPictrues/soundsOn.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.soundCheckBox.setIcon(icon)
        self.soundCheckBox.setIconSize(QSize(70, 70))
        self.carPicturesLabel = QLabel(self.centralwidget)
        self.carPicturesLabel.setObjectName(u"carPicturesLabel")
        self.carPicturesLabel.setGeometry(QRect(20, 410, 341, 261))
        self.carPicturesLabel.setPixmap(QPixmap(u"uiPictrues/FNK129.png"))
        self.carPicturesLabel.setScaledContents(True)
        self.carPicturesLabel.setWordWrap(False)
        self.carPicturesLabel.setOpenExternalLinks(False)
        self.freeCarPlainTextEdit = QPlainTextEdit(self.centralwidget)
        self.freeCarPlainTextEdit.setObjectName(u"freeCarPlainTextEdit")
        self.freeCarPlainTextEdit.setGeometry(QRect(170, 160, 501, 551))
        font3 = QFont()
        font3.setPointSize(12)
        self.freeCarPlainTextEdit.setFont(font3)
        self.freeCarPlainTextEdit.setStyleSheet(u"color: rgb(75, 188, 197);\n"
"border-color: rgb(75, 188, 197);\n"
"")
        self.freeCarPlainTextEdit.setFrameShape(QFrame.Shape.WinPanel)
        self.freeCarPlainTextEdit.setFrameShadow(QFrame.Shadow.Plain)
        self.freeCarPlainTextEdit.setLineWidth(3)
        self.drivingCarPlainTextEdit = QPlainTextEdit(self.centralwidget)
        self.drivingCarPlainTextEdit.setObjectName(u"drivingCarPlainTextEdit")
        self.drivingCarPlainTextEdit.setGeometry(QRect(670, 160, 531, 551))
        self.drivingCarPlainTextEdit.setFont(font3)
        self.drivingCarPlainTextEdit.setStyleSheet(u"color: rgb(75, 188, 197);\n"
"border-color: rgb(75, 188, 197);")
        self.drivingCarPlainTextEdit.setFrameShape(QFrame.Shape.WinPanel)
        self.drivingCarPlainTextEdit.setFrameShadow(QFrame.Shadow.Plain)
        self.drivingCarPlainTextEdit.setLineWidth(3)
        self.registerLabel = QLabel(self.centralwidget)
        self.registerLabel.setObjectName(u"registerLabel")
        self.registerLabel.setGeometry(QRect(720, 400, 241, 71))
        self.registerLabel.setPixmap(QPixmap(u":/pictures/uiPictrues/EU-kilpi.png"))
        self.registerLabel.setScaledContents(True)
        self.registerReturnLabel = QLabel(self.centralwidget)
        self.registerReturnLabel.setObjectName(u"registerReturnLabel")
        self.registerReturnLabel.setGeometry(QRect(540, 400, 241, 71))
        self.registerReturnLabel.setPixmap(QPixmap(u":/pictures/uiPictrues/EU-kilpi.png"))
        self.registerReturnLabel.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.takeCarPushButton.raise_()
        self.returnCarPushButton.raise_()
        self.humanLabel.raise_()
        self.borrowerLabel.raise_()
        self.carTakeLabel.raise_()
        self.carKeysLabel.raise_()
        self.clockPictureLabel.raise_()
        self.licenseLineEdit.raise_()
        self.calenderLabel.raise_()
        self.dateLabel.raise_()
        self.goBackPushButton.raise_()
        self.hourLabel.raise_()
        self.nameLabel.raise_()
        self.carInfoLabel.raise_()
        self.okPushButton.raise_()
        self.carKeysReturnLabel.raise_()
        self.carTakeReturnLabel.raise_()
        self.freeCarLabel.raise_()
        self.drivingCarLabel.raise_()
        self.soundCheckBox.raise_()
        self.carPicturesLabel.raise_()
        self.freeCarPlainTextEdit.raise_()
        self.drivingCarPlainTextEdit.raise_()
        self.registerReturnLabel.raise_()
        self.keysReturnLineEdit.raise_()
        self.registerLabel.raise_()
        self.keysLineEdit.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1366, 33))
        self.menubar.setStyleSheet(u"background-color: rgb(223, 32, 112);")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"background-color: rgb(223, 32, 112);")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.takeCarPushButton.setText(QCoreApplication.translate("MainWindow", u"Lainaa auto", None))
        self.returnCarPushButton.setText(QCoreApplication.translate("MainWindow", u"Palauta auto", None))
        self.humanLabel.setText("")
        self.borrowerLabel.setText(QCoreApplication.translate("MainWindow", u"Lainaaja", None))
        self.carTakeLabel.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.carKeysLabel.setText("")
        self.clockPictureLabel.setText("")
        self.keysLineEdit.setText("")
        self.keysLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lue avain", None))
        self.licenseLineEdit.setText("")
        self.licenseLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lue ajokortti", None))
        self.calenderLabel.setText("")
        self.dateLabel.setText(QCoreApplication.translate("MainWindow", u"27.1.2025", None))
        self.goBackPushButton.setText(QCoreApplication.translate("MainWindow", u"KUMOA", None))
        self.hourLabel.setText(QCoreApplication.translate("MainWindow", u"10.09", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Lainaajan nimi", None))
        self.carInfoLabel.setText(QCoreApplication.translate("MainWindow", u"Merkki ja Malli", None))
        self.okPushButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.keysReturnLineEdit.setText("")
        self.keysReturnLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lue avain", None))
        self.carKeysReturnLabel.setText("")
        self.carTakeReturnLabel.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.freeCarLabel.setText(QCoreApplication.translate("MainWindow", u"Vapaana", None))
        self.drivingCarLabel.setText(QCoreApplication.translate("MainWindow", u"Ajossa", None))
        self.soundCheckBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.carPicturesLabel.setText("")
        self.freeCarPlainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"XSE-778 Toyota BZ4X 5 henkil\u00f6\u00e4\n"
"ABC-123 VW Transporter 3 henkil\u00f6\u00e4", None))
        self.drivingCarPlainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"DSE-546 Nissan Micra 5 henkil\u00f6\u00e4\n"
"", None))
        self.registerLabel.setText("")
        self.registerReturnLabel.setText("")
    # retranslateUi

