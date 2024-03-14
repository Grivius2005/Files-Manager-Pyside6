import os

from PySide6.QtCore import QFileInfo
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFileIconProvider

icons_path = ".\\public\\files_icons"

icons_suffix = ["doc", "html", "json", "mp3", "pdf", "txt", "zip", "mp4", "mov", "wav", "xls", "png", "jpg", "gif",
                "svg", "xml", "css", "js", "py"]


class FilesIconProvider(QFileIconProvider):
    def icon(self, parameter):
        if isinstance(parameter, QFileInfo):
            info = parameter
            suffix = info.suffix()
            if suffix in icons_suffix and not os.path.isdir(info.filePath()):
                return QIcon(os.path.join(icons_path, f"{suffix}.png"))
        return super(FilesIconProvider, self).icon(parameter)
