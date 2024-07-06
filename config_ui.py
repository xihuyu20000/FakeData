# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QHBoxLayout,
    QLabel, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(489, 423)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 60, 232, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.birthday_start = QDateEdit(self.widget)
        self.birthday_start.setObjectName(u"birthday_start")
        self.birthday_start.setDateTime(QDateTime(QDate(1949, 12, 31), QTime(0, 0, 0)))
        self.birthday_start.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.birthday_start)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.birthday_end = QDateEdit(self.widget)
        self.birthday_end.setObjectName(u"birthday_end")
        self.birthday_end.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.birthday_end)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u751f\u65e5", None))
        self.birthday_start.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy-MM-dd", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5230", None))
        self.birthday_end.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy-MM-dd", None))
    # retranslateUi

