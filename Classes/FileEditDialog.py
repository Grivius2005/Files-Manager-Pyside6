from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QGridLayout, QPlainTextEdit, QPushButton


class FileEditDialog(QDialog):
    status = 0
    filecontent = ""

    def __init__(self, filename: str, filecontent: str):
        super().__init__()
        self.filecontent = filecontent

        self.setGeometry(0, 0, 600, 400)
        icon = QIcon()
        icon.addFile('./public/icon.png')
        self.setWindowIcon(icon)
        self.setWindowTitle(f"Edit - {filename}")
        self.layout = QGridLayout()

        self.editText = QPlainTextEdit(self)
        self.editText.insertPlainText(self.filecontent)
        self.layout.addWidget(self.editText, 0, 0, 1, 0)

        self.saveBtn = QPushButton("Save")
        self.saveBtn.clicked.connect(self.__save)
        self.layout.addWidget(self.saveBtn, 1, 0,)

        self.cancelBtn = QPushButton("Cancel")
        self.cancelBtn.clicked.connect(self.close)
        self.layout.addWidget(self.cancelBtn, 1, 1)

        self.setLayout(self.layout)

    def __save(self):
        self.status = 1
        self.filecontent = self.editText.toPlainText()
        self.close()
