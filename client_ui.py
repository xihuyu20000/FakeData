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
    QStatusBar, QTabWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from util import (DDTable, ExampleLabel)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_author = QAction(MainWindow)
        self.action_author.setObjectName(u"action_author")
        self.action_help = QAction(MainWindow)
        self.action_help.setObjectName(u"action_help")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(16777215, 70))

        self.verticalLayout.addWidget(self.tabWidget)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.label_example = ExampleLabel(self.frame_2)
        self.label_example.setObjectName(u"label_example")
        self.label_example.setMinimumSize(QSize(500, 0))

        self.horizontalLayout_2.addWidget(self.label_example)

        self.horizontalSpacer_2 = QSpacerItem(211, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_config = QPushButton(self.frame_2)
        self.btn_config.setObjectName(u"btn_config")

        self.horizontalLayout_2.addWidget(self.btn_config)


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
        self.lineEdit_count.setMinimumSize(QSize(100, 0))
        self.lineEdit_count.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_count)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.btn_export_csv = QPushButton(self.frame_3)
        self.btn_export_csv.setObjectName(u"btn_export_csv")

        self.horizontalLayout_3.addWidget(self.btn_export_csv)

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
        self.menu.addAction(self.action_help)
        self.menu.addAction(self.action_author)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_author.setText(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb\u4f5c\u8005", None))
        self.action_help.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u8bf4\u660e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u793a\u4f8b\uff1a", None))
        self.label_example.setText("")
        self.btn_config.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.lineEdit_count.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6761\u8bb0\u5f55\uff0c\u5bfc\u51fa", None))
        self.btn_export_csv.setText(QCoreApplication.translate("MainWindow", u"CSV\u6587\u4ef6", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

