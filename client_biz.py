import pyperclip
from PySide6.QtGui import QActionGroup, QIntValidator
from PySide6.QtWidgets import QMainWindow, QButtonGroup, QTableWidgetItem, QMessageBox, QFrame, QHBoxLayout, \
    QSpacerItem, QSizePolicy, QLabel
from faker import Faker

import util
from client_ui import Ui_MainWindow
from config_biz import ConfigBiz
from util import CONST, mappings, tabs, sgls, ExportThread, MyLabel, get_value


class FakeDataClient(QMainWindow, Ui_MainWindow):
    VERSION = '0.1.1'
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 菜单栏
        self.action_group = QActionGroup(self)
        self.action_group.addAction(self.action_help)
        self.action_group.addAction(self.action_author)
        self.action_group.triggered.connect(self.action_group_triggered)

        # 顶部工具栏
        self.init_toolbar()

        # 按钮
        self.btn_group = QButtonGroup(self)
        self.btn_group.addButton(self.btn_export_csv)
        self.btn_group.addButton(self.btn_config)
        self.btn_group.buttonClicked.connect(self.btn_group_clicked)


        intVal = QIntValidator()
        intVal.setRange(1, 99999999)
        self.lineEdit_count.setValidator(intVal)

        # 信号槽函数
        sgls.click_label.connect(self.show_example)
        sgls.dbclick_btn.connect(self.dbclick_btn)
        sgls.click_example.connect(self.paste_example)
        sgls.export_thread.connect(self.show_msg_statusbar)

        self.labels = []
        # 删除列的事件
        self.tableWidget_data.remove_cindex.connect(self.remove_column_label)
        # 显示版本号
        self.statusbar.addPermanentWidget(QLabel(f"当前版本 {FakeDataClient.VERSION}"))


    def action_group_triggered(self, act):
        match act.objectName():
            case 'action_help':
                QMessageBox.information(None, "使用帮助", CONST.HELP_TEXT)
                return
            case 'action_author':
                QMessageBox.information(None, "联系作者", CONST.AUTHOR_TEXT)
            case _:
                ...

    def btn_group_clicked(self, btn):

        match btn.objectName():
            case 'btn_config':
                self.config_dialog = ConfigBiz()
                self.config_dialog.exec()

                CONST.BIRTHDAY_START = self.config_dialog.birthday_start.text()
                CONST.BIRTHDAY_END = self.config_dialog.birthday_end.text()


            case 'btn_export_csv':
                self.thread = ExportThread(self.labels, int(self.lineEdit_count.text()))
                self.thread.start()
                return
            case _:
                ...

    def init_toolbar(self):
        """
        初始化工具栏
        """
        for tabName, itemlist in tabs.items():
            frame = QFrame()
            layout = QHBoxLayout(frame)
            layout.setContentsMargins(10, 0, 0, 0)
            for item in itemlist:
                mappings[item.name] = item.func
                btn = MyLabel(item.name)
                layout.addWidget(btn)
            layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
            self.tabWidget.addTab(frame, tabName)

    def show_example(self, objname):
        """
        显示示例
        :param objname:
        """
        self.label_example.setText(get_value(mappings[objname]))

    def dbclick_btn(self, objname):
        """
        双击分类，
        :param objname:
        """
        self.labels.append(objname)
        val = get_value(mappings[objname])
        self.label_example.setText(val)
        self.init_table()

    def paste_example(self, text):
        pyperclip.copy(text)
        self.show_msg_statusbar('已经复制到剪贴板')

    def init_table(self):
        """
        填充数据区
        """
        self.tableWidget_data.setColumnCount(len(self.labels))
        self.tableWidget_data.setRowCount(10)

        self.tableWidget_data.setHorizontalHeaderLabels(self.labels)

        for i in range(10):
            for j in range(len(self.labels)):
                val = get_value(mappings[self.labels[j]])
                self.tableWidget_data.setItem(i, j, QTableWidgetItem(str(val)))

    def remove_column_label(self, i):
        """
        数据区，删除列时，维护一下
        :param i:
        """
        self.labels.remove(self.labels[i])

    def show_msg_statusbar(self, str):
        """
        状态栏显示信息
        :param str:
        """
        self.statusbar.showMessage(str, timeout=10000)

