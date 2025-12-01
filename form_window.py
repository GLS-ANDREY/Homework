# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QTimeEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(469, 421)
        self.name = QLineEdit(Form)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(20, 10, 361, 22))
        self.price = QSpinBox(Form)
        self.price.setObjectName(u"price")
        self.price.setGeometry(QRect(20, 40, 361, 22))
        self.time = QTimeEdit(Form)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(20, 70, 361, 22))
        self.calendar = QCalendarWidget(Form)
        self.calendar.setObjectName(u"calendar")
        self.calendar.setGeometry(QRect(60, 160, 256, 190))
        self.residentButton = QRadioButton(Form)
        self.residentButton.setObjectName(u"residentButton")
        self.residentButton.setGeometry(QRect(290, 100, 89, 20))
        self.actualButton = QCheckBox(Form)
        self.actualButton.setObjectName(u"actualButton")
        self.actualButton.setGeometry(QRect(20, 100, 101, 20))
        self.commercialButton = QRadioButton(Form)
        self.commercialButton.setObjectName(u"commercialButton")
        self.commercialButton.setGeometry(QRect(290, 120, 111, 20))
        self.cancelButton = QPushButton(Form)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(250, 380, 211, 24))
        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(10, 380, 201, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"FormWindow", None))
        self.residentButton.setText(QCoreApplication.translate("Form", u"\u0416\u0438\u043b\u043e\u0435", None))
        self.actualButton.setText(QCoreApplication.translate("Form", u"\u0410\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.commercialButton.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043c\u043c\u0435\u0440\u0447\u0435\u0441\u043a\u043e\u0435", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

