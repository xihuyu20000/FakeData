# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidgetItem, QVBoxLayout, QWidget)

from util import DDTable

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_author = QAction(MainWindow)
        self.action_author.setObjectName(u"action_author")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_btnbar = QFrame(self.centralwidget)
        self.frame_btnbar.setObjectName(u"frame_btnbar")
        self.frame_btnbar.setStyleSheet(u"QFrame { border:1px solid gray;} ")
        self.frame_btnbar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_btnbar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_btnbar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(759, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame_btnbar)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.label_example = QLabel(self.frame_2)
        self.label_example.setObjectName(u"label_example")
        self.label_example.setMinimumSize(QSize(500, 0))

        self.horizontalLayout_2.addWidget(self.label_example)

        self.horizontalSpacer_2 = QSpacerItem(211, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_2)

        self.tableWidget_data = DDTable(self.centralwidget)
        self.tableWidget_data.setObjectName(u"tableWidget_data")

        self.verticalLayout.addWidget(self.tableWidget_data)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit_count = QLineEdit(self.frame_3)
        self.lineEdit_count.setObjectName(u"lineEdit_count")

        self.horizontalLayout_3.addWidget(self.lineEdit_count)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.btn_export_csv = QPushButton(self.frame_3)
        self.btn_export_csv.setObjectName(u"btn_export_csv")

        self.horizontalLayout_3.addWidget(self.btn_export_csv)

        self.btn_export_excel = QPushButton(self.frame_3)
        self.btn_export_excel.setObjectName(u"btn_export_excel")

        self.horizontalLayout_3.addWidget(self.btn_export_excel)

        self.horizontalSpacer_3 = QSpacerItem(597, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_author)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_author.setText(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb\u4f5c\u8005", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u793a\u4f8b\uff1a", None))
        self.label_example.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.lineEdit_count.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6761\u8bb0\u5f55\uff0c\u5bfc\u51fa\u5230", None))
        self.btn_export_csv.setText(QCoreApplication.translate("MainWindow", u"CSV", None))
        self.btn_export_excel.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

