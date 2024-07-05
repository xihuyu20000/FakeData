from PySide6.QtCore import Signal
from PySide6.QtWidgets import QAbstractItemView, QTableWidget


class DDTable(QTableWidget):
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
