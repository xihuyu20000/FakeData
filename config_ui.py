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
    QLabel, QSizePolicy, QSpacerItem, QSpinBox,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(489, 423)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 60, 232, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.birthday_start = QDateEdit(self.layoutWidget)
        self.birthday_start.setObjectName(u"birthday_start")
        self.birthday_start.setDateTime(QDateTime(QDate(1949, 12, 29), QTime(0, 0, 0)))
        self.birthday_start.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.birthday_start)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.birthday_stop = QDateEdit(self.layoutWidget)
        self.birthday_stop.setObjectName(u"birthday_stop")
        self.birthday_stop.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.birthday_stop)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(50, 110, 274, 22))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(24, 16777215))

        self.horizontalLayout.addWidget(self.label_3)

        self.salary_start = QSpinBox(self.layoutWidget1)
        self.salary_start.setObjectName(u"salary_start")
        self.salary_start.setMinimumSize(QSize(88, 0))
        self.salary_start.setMaximumSize(QSize(88, 16777215))
        self.salary_start.setSizeIncrement(QSize(88, 0))
        self.salary_start.setMaximum(9999999)
        self.salary_start.setSingleStep(1)
        self.salary_start.setValue(1000)

        self.horizontalLayout.addWidget(self.salary_start)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(12, 16777215))

        self.horizontalLayout.addWidget(self.label_4)

        self.salary_stop = QSpinBox(self.layoutWidget1)
        self.salary_stop.setObjectName(u"salary_stop")
        self.salary_stop.setMinimumSize(QSize(88, 0))
        self.salary_stop.setMaximumSize(QSize(88, 16777215))
        self.salary_stop.setMaximum(99999999)
        self.salary_stop.setValue(10000)

        self.horizontalLayout.addWidget(self.salary_stop)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u751f\u65e5", None))
        self.birthday_start.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy-MM-dd", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5230", None))
        self.birthday_stop.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy-MM-dd", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u5de5\u8d44", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u5230", None))
    # retranslateUi

