import sys

from PySide6.QtCore import QDateTime
from PySide6.QtGui import QIcon, QAction, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QListWidget, QHBoxLayout, QPushButton, \
    QTreeWidget, QLabel, QVBoxLayout, QMenu, QMenuBar
from Classes.FilesManagerView import FilesManagerView
from Classes.FilesOperations import FilesOperations


class MainWindow(QMainWindow):

    fileManager = None

    def __init__(self):
        super().__init__()

        self.setWindowTitle("FileManager")
        icon = QIcon()
        icon.addFile('public/icon.png')


        self.setWindowIcon(icon)
        self.setGeometry(0, 0, 750, 750)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)


        self.fileManager = FilesManagerView()
        self.layout.addWidget(self.fileManager)

        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        self.fileMenu = QMenu("File", self)
        self.menuBar.addMenu(self.fileMenu)

        actNewFile = QAction("New file",self)
        actNewFile.triggered.connect(lambda: FilesOperations.createFile(self, self.fileManager.currentPath))
        actNewFile.setShortcut(QKeySequence("Ctrl+N"))
        self.fileMenu.addAction(actNewFile)

        actNewDir = QAction("New directory", self)
        actNewDir.triggered.connect(lambda: FilesOperations.createDir(self, self.fileManager.currentPath))
        actNewDir.setShortcut(QKeySequence("Ctrl+Shift+N"))
        self.fileMenu.addAction(actNewDir)

        actCopy = QAction("Copy", self)
        actCopy.triggered.connect(lambda: FilesOperations.copyFileDir(self, self.fileManager.currentPath))
        actCopy.setShortcut(QKeySequence("Ctrl+C"))
        self.fileMenu.addAction(actCopy)

        actMove = QAction("Move", self)
        actMove.triggered.connect(lambda: FilesOperations.moveFileDir(self, self.fileManager.currentPath))
        actMove.setShortcut(QKeySequence("Ctrl+M"))
        self.fileMenu.addAction(actMove)

        actRename = QAction("Rename", self)
        actRename.triggered.connect(lambda: FilesOperations.renameFileDir(self, self.fileManager.currentPath))
        actRename.setShortcut(QKeySequence("Ctrl+R"))
        self.fileMenu.addAction(actRename)

        actDelete = QAction("Delete", self)
        actDelete.triggered.connect(lambda: FilesOperations.deleteFileDir(self, self.fileManager.currentPath))
        actDelete.setShortcut(QKeySequence("Ctrl+D"))
        self.fileMenu.addAction(actDelete)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
