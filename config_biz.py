from PySide6.QtWidgets import QDialog

from config_ui import Ui_Dialog


class ConfigBiz(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

