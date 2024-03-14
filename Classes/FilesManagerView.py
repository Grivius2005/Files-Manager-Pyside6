import os

from PySide6.QtWidgets import QTreeView, QFileSystemModel, QWidget, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, \
    QLineEdit, QFileIconProvider
from PySide6.QtCore import Qt

from FileManager.Classes.FilesIconProvider import FilesIconProvider
from FileManager.Classes.FilesOperations import FilesOperations


class FilesManagerView(QWidget):
    __layout = None
    __urlEdit = None
    __treeView = None
    __treeModel = None

    currentPath = ''

    def __init__(self, dir_path: str = ""):
        super().__init__()

        self.__layout = QVBoxLayout()
        self.__layout.setSpacing(0)

        self.currentPath = dir_path
        self.__treeModel = QFileSystemModel()
        self.__treeModel.setRootPath("")

        self.__urlEdit = QLineEdit()
        self.__urlEdit.setStyleSheet("border: 1px solid black;background-color:lightgrey; padding: 5px;")
        self.__urlEdit.setText(self.currentPath)
        self.__urlEdit.editingFinished.connect(self.__showSelectedPath)
        self.__urlEdit.returnPressed.connect(lambda: self.__changeFilePath(self.__urlEdit.text()))
        self.__layout.addWidget(self.__urlEdit, stretch=1)

        self.__treeView = QTreeView()
        self.__treeView.setModel(self.__treeModel)
        self.__treeView.setRootIndex(self.__treeModel.index(self.currentPath))
        self.__treeView.setColumnWidth(0, 300)
        self.__treeView.setColumnWidth(1, 100)
        self.__treeView.setColumnWidth(2, 100)
        self.__treeView.setColumnWidth(3, 100)
        self.__treeView.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        self.__treeView.clicked.connect(self.__showSelectedPath)
        self.__treeView.doubleClicked.connect(lambda: FilesOperations.editFile(self, self.currentPath))

        self.__treeModel.setIconProvider(FilesIconProvider())

        self.__layout.addWidget(self.__treeView, stretch=25)

        self.setLayout(self.__layout)

    def __changeFilePath(self, url: str):
        self.__treeView.setCurrentIndex(self.__treeModel.index(url))
        self.__showSelectedPath()

    def __showSelectedPath(self):
        selectedIndex = self.__treeView.selectedIndexes()[0] if len(self.__treeView.selectedIndexes()) != 0 else None
        if selectedIndex:
            self.currentPath = self.__treeModel.filePath(selectedIndex)
            self.__urlEdit.setText(self.currentPath)
