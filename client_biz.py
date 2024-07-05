import os
import sys
import typing
import webbrowser

from PySide6.QtCore import Signal, QObject, QThread
from PySide6.QtGui import QActionGroup
from PySide6.QtWidgets import QMainWindow, QButtonGroup, QLabel, \
    QTableWidgetItem
from faker import Faker
import pandas as pd
from client_ui import Ui_MainWindow

faker = Faker(locale='zh-CN')
mappings = {
    '国家': faker.country
    , '省份': faker.province
    , '城市': faker.city
    , '街道地址': faker.street_address
    , '公司': faker.company
    , '邮编': faker.postcode
    , '邮箱': faker.free_email
    , '手机号': faker.phone_number
    , '女性名': faker.name_female
    , '姓名': faker.name
    , '身份证号':faker.ssn
    ,'职位':faker.job
    ,'ipv4':faker.ipv4
}


class MySignal(QObject):
    click_label = Signal(str)
    dbclick_btn = Signal(str)
    export_thread = Signal(str)

sgls = MySignal()


class MyBtn(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setObjectName(text)

    def mousePressEvent(self, event):
        sgls.click_label.emit(self.objectName())

    def mouseDoubleClickEvent(self, event):
        sgls.dbclick_btn.emit(self.objectName())

class ExportThread(QThread):
    def __init__(self, labels: typing.List[str], count:int):
        super().__init__()
        self.labels = labels
        self.count = count

    def run(self):
        sgls.export_thread.emit("开始导出")
        df = self.__gen_data()
        df.to_csv('aaa.csv',index=False)
        sgls.export_thread.emit("成功导出")

    def __gen_data(self):
        data = []
        for i in range(self.count):
            data.append((mappings[key]() for key in self.labels))
        return pd.DataFrame(columns=self.labels, data=data)

class FakeDataClient(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 菜单
        self.action_group = QActionGroup(self)
        self.action_group.addAction(self.action_author)
        self.action_group.triggered.connect(self.action_group_triggered)
        # 按钮
        self.btn_group = QButtonGroup(self)
        self.btn_group.addButton(self.btn_export_csv)
        self.btn_group.addButton(self.btn_export_excel)
        self.btn_group.buttonClicked.connect(self.btn_group_clicked)
        self.init_btnbar()
        sgls.click_label.connect(self.show_example)
        sgls.dbclick_btn.connect(self.use_btn)
        sgls.export_thread.connect(self.export_data_handler)

        self.labels = []
        # 删除列的事件
        self.tableWidget_data.remove_cindex.connect(self.remove_column_label)

    def action_group_triggered(self, act):
        webbrowser.open(os.path.join(os.path.dirname(sys.argv[0]), 'html', 'author.html'))
    def btn_group_clicked(self, btn):
        print(btn)
        self.thread = ExportThread(self.labels, int(self.lineEdit_count.text()))
        self.thread.start()
    def init_btnbar(self):
        for i in mappings.keys():
            btn = MyBtn(i)
            self.frame_btnbar.layout().insertWidget(0, btn)

    def show_example(self, objname):
        self.label_example.setText(mappings[objname]())

    def use_btn(self, objname):
        self.labels.append(objname)
        self.label_example.setText(mappings[objname]())
        self.init_table()

    def init_table(self):
        self.tableWidget_data.setColumnCount(len(self.labels))
        self.tableWidget_data.setRowCount(10)

        self.tableWidget_data.setHorizontalHeaderLabels(self.labels)

        for i in range(10):
            for j in range(len(self.labels)):
                val = mappings[self.labels[j]]()
                self.tableWidget_data.setItem(i, j, QTableWidgetItem(str(val)))

    def remove_column_label(self, i):
        self.labels.remove(self.labels[i])

    def export_data_handler(self, str):
        self.statusbar.showMessage(str)
