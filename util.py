import typing

from PySide6.QtCore import Signal, QThread, QObject
from PySide6.QtWidgets import QAbstractItemView, QTableWidget, QLabel
from faker import Faker

"""
ar_EG - Arabic (Egypt)
ar_PS - Arabic (Palestine)
ar_SA - Arabic (Saudi Arabia)
bg_BG - Bulgarian
bs_BA - Bosnian
cs_CZ - Czech
de_DE - German
dk_DK - Danish
el_GR - Greek
en_AU - English (Australia)
en_CA - English (Canada)
en_GB - English (Great Britain)
en_NZ - English (New Zealand)
en_US - English (United States)
es_ES - Spanish (Spain)
es_MX - Spanish (Mexico)
et_EE - Estonian
fa_IR - Persian (Iran)
fi_FI - Finnish
fr_FR - French
hi_IN - Hindi
hr_HR - Croatian
hu_HU - Hungarian
hy_AM - Armenian
it_IT - Italian
ja_JP - Japanese
ka_GE - Georgian (Georgia)
ko_KR - Korean
lt_LT - Lithuanian
lv_LV - Latvian
ne_NP - Nepali
nl_NL - Dutch (Netherlands)
no_NO - Norwegian
pl_PL - Polish
pt_BR - Portuguese (Brazil)
pt_PT - Portuguese (Portugal)
ro_RO - Romanian
ru_RU - Russian
sl_SI - Slovene
sv_SE - Swedish
tr_TR - Turkish
uk_UA - Ukrainian
zh_CN - Chinese (China Mainland)
zh_TW - Chinese (China Taiwan)
"""


class CONST:
    LOCALE = 'zh-CN'
    HELP_TEXT = "顶部数据名称区，可以单击，可以双击；数据区标题栏，可以拖拽，可以双击。"
    AUTHOR_TEXT = "如果想增加新的数据类型，请联系作者，邮箱377486624@qq.com"
    BIRTHDAY_START = '1950-01-01'
    BIRTHDAY_END = '2019-01-01'


faker = Faker(locale=CONST.LOCALE)


class CfgItem:
    __slots__ = ['name', 'func']

    def __init__(self, name, func):
        self.name = name
        self.func = func


tabs = {
    '地区': [
        CfgItem('国家', faker.country)
        , CfgItem('省', faker.province)
        , CfgItem('市', faker.city)
        , CfgItem('区县', faker.district)
        , CfgItem('街道名', faker.street_name)
        , CfgItem('街道地址', faker.street_address)
        , CfgItem('邮编', faker.postcode)
        , CfgItem('经度', faker.longitude)
        , CfgItem('维度', faker.latitude)
    ]
    , '公司': [
        CfgItem('公司(长)', faker.company)
        , CfgItem('公司(短)', faker.company_prefix)
        , CfgItem('公司性质', faker.company_suffix)
    ]
    , '网络': [
        CfgItem('ipv4', faker.ipv4)
        , CfgItem('linux信息', faker.linux_platform_token)
        , CfgItem('用户代理', faker.user_agent)
        , CfgItem('URI', faker.uri)
        , CfgItem('MAC', faker.mac_address)
    ]
    , '个人': [
        CfgItem('姓名', faker.name)
        , CfgItem('女性名', faker.name_female)
        , CfgItem('手机号', faker.phone_number)
        , CfgItem('生日', f'''
from datetime import datetime
start = datetime.strptime('{CONST.BIRTHDAY_START}', '%Y-%m-%d')
end = datetime.strptime('{CONST.BIRTHDAY_END}', '%Y-%m-%d')
val = faker.date_time_between_dates(datetime_start=start,datetime_end=end)
val = val.strftime('%Y-%m-%d')
''')
        , CfgItem('身份证号', faker.ssn)
        , CfgItem('职位', faker.job)
        , CfgItem('邮箱', faker.free_email)
    ]
    , '文字': [
        CfgItem('文章', faker.text)
        , CfgItem('词语', faker.word)

    ]
    , '其他': [
        CfgItem('颜色', faker.color_name)
        , CfgItem('安全色', faker.safe_color_name)
    ]
}
mappings = {

}


def get_value(func):
    if callable(func):
        val = func()
    elif isinstance(func, str):
        local = {'val': None}
        exec(func, globals(), local)
        val = local['val']
    else:
        raise ValueError(f"不识别的类型 {func}")
    return str(val)


class DDTable(QTableWidget):
    """
    可以拖拽表头的表格，双击表头可以删除列
    """
    remove_cindex = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropOverwriteMode(False)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)

        self.horizontalHeader().setSectionsMovable(True)
        self.horizontalHeader().setDragEnabled(True)
        self.horizontalHeader().setDragDropMode(QAbstractItemView.InternalMove)
        self.horizontalHeader().sectionDoubleClicked.connect(self.remove_column)

    def remove_column(self, column):
        self.removeColumn(column)
        self.remove_cindex.emit(column)


class MySignal(QObject):
    click_label = Signal(str)
    click_example = Signal(str)
    dbclick_btn = Signal(str)
    export_thread = Signal(str)


sgls = MySignal()


class MyLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setObjectName(text)
        self.setFixedHeight(24)
        self.setStyleSheet('''
        MyLabel {
            border: 1px solid gray;
        }
        MyLabel:hover{
            background-color: #a0a0a0;
        }
        ''')

    def mousePressEvent(self, event):
        sgls.click_label.emit(self.objectName())

    def mouseDoubleClickEvent(self, event):
        sgls.dbclick_btn.emit(self.objectName())

class ExampleLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
    def mousePressEvent(self, event):
        sgls.click_example.emit(self.text())


class ExportThread(QThread):
    def __init__(self, labels: typing.List[str], count: int):
        super().__init__()
        self.__labels = labels
        self.__count = count

    def run(self):
        sgls.export_thread.emit("开始导出")
        with open('fake.csv', 'w', encoding='utf-8') as f:
            f.write(','.join(self.__labels))
            f.write('\n')
            rows = []
            for i in range(self.__count):
                row = []
                for key in self.__labels:
                    val = get_value(mappings[key])
                    row.append(val)
                rows.append(row)
            f.write('\n'.join([','.join(row) for row in rows]))
        sgls.export_thread.emit("成功导出")
