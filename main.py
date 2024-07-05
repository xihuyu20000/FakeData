import sys

from PySide6.QtWidgets import QApplication

from client_biz import FakeDataClient

#     https://blog.csdn.net/weixin_42670810/article/details/110682327
if __name__ == '__main__':
    app = QApplication(sys.argv)

    client = FakeDataClient()
    client.show()

    sys.exit(app.exec())