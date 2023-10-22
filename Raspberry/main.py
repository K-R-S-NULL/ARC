# This Python file uses the following encoding: utf-8
import sys
import os
import ui

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

if __name__ == "__main__":
    app = QApplication([])
    widget = ui.mainWindow()
    sys.exit(app.exec_())
