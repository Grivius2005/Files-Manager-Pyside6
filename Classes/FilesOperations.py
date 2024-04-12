import os
import shutil

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFileDialog, QWidget, QMessageBox, QInputDialog, QLineEdit, QDialog

from .FileEditDialog import FileEditDialog


class FilesOperations:
    @staticmethod
    def createFile(widget: QWidget, path: str):
        if not os.path.exists(path):
            QMessageBox.critical(widget, "Error", "Selected path doesn't exist.")
        else:

            basedirpath = os.path.dirname(path) if os.path.isfile(path) else path

            filename, ok = QInputDialog.getText(widget, "Create file",
                                                "New File Name:", QLineEdit.Normal,
                                                "")
            if filename and ok:
                filepath = os.path.join(basedirpath, filename)
                try:
                    with open(filepath, "a") as f:
                        f.write("")
                except Exception as ex:
                    QMessageBox.critical(widget, "Error", str(ex))

    @staticmethod
    def createDir(widget: QWidget, path: str):
        if not os.path.exists(path):
            QMessageBox.critical(widget, "Error", "Selected path doesn't exist.")
        else:

            dirname, ok = QInputDialog.getText(widget, "Create directory",
                                               "New Directory Name:", QLineEdit.Normal,
                                               "")
            if dirname and ok:
                try:
                    os.mkdir(os.path.join(path, dirname))
                except Exception as ex:
                    QMessageBox.critical(widget, "Error", str(ex))

    @staticmethod
    def moveFileDir(widget: QWidget, path: str):
        if not os.path.exists(path):
            QMessageBox.critical(widget, "Error", "Selected path doesn't exist.")
        else:

            new_path, ok = QInputDialog.getText(widget, "Move file",
                                                "New path", QLineEdit.Normal,
                                                path)
            if new_path and ok:
                try:
                    shutil.move(path, new_path)
                except Exception as ex:
                    QMessageBox.critical(widget, "Error", str(ex))

    @staticmethod
    def copyFileDir(widget: QWidget, path: str):
        if not os.path.exists(path):
            QMessageBox.critical(widget, "Error", "Selected path doesn't exist.")
        else:

            copy_path, ok = QInputDialog.getText(widget, "Copy file",
                                                 "New path", QLineEdit.Normal,
                                                 path)
            if copy_path and ok:
                try:
                    shutil.copy(path, copy_path)
                except Exception as ex:
                    QMessageBox.critical(widget, "Error", str(ex))

    @staticmethod
    def renameFileDir(widget: QWidget, path: str):
        if not os.path.exists(path):
            QMessageBox.critical(widget, "Error", "Selected path doesn't exist.")
        else:
            filename = os.path.basename(path)
            dirname = os.path.dirname(path)

            new_filename, ok = QInputDialog.getText(widget, "Rename file",
                                                    "File New Name:", QLineEdit.Normal,
                                                    filename)
            if new_filename and ok:
                try:
                    os.rename(path, os.path.join(dirname, new_filename))
                except Exception as ex:
                    QMessageBox.critical(widget, "Error", str(ex))

    @staticmethod
    def deleteFileDir(widget: QWidget, path: str):
        if not os.path.exists(path):
            QMessageBox.critical(widget, "Error", "Selected path doesn't exist.")
        else:

            cofirmance = QMessageBox()
            cofirmance.setWindowTitle("Delete")
            icon = QIcon()
            icon.addFile('./public/icon.png')
            cofirmance.setWindowIcon(icon)
            cofirmance.setText("Are you sure you want to delete this?")
            cofirmance.setStandardButtons(QMessageBox.StandardButton.Yes |
                                          QMessageBox.StandardButton.No)

            confimed = cofirmance.exec()

            if confimed == QMessageBox.StandardButton.Yes:
                try:
                    if os.path.isdir(path):
                        shutil.rmtree(path)
                    else:
                        os.remove(path)
                except Exception as ex:
                    QMessageBox.critical(widget, "Error", str(ex))

    @staticmethod
    def editFile(widget: QWidget, path: str):
        if not os.path.exists(path):
            QMessageBox.critical(widget, "Error", "Selected path doesn't exist.")
        elif not os.path.isfile(path):
            return
        else:
            filecontent = ""
            try:
                with open(path, "r") as f:
                    filecontent = f.read()
            except:
                QMessageBox.critical(widget, "Error", "Error with reading file.")
                return
            fileEdit = FileEditDialog(os.path.basename(path), filecontent)
            fileEdit.exec()
            status = fileEdit.status
            if status:
                filecontent = fileEdit.filecontent
                try:
                    with open(path, "w") as f:
                        f.write(filecontent)
                except:
                    QMessageBox.critical(widget, "Error", "Error with saving file.")


