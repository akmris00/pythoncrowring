import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
import datetime
import re
from lib.You_viewer_layout import Ui_MainWindow

#form_class = uic.loadUiType('C:/Atom/Crowring/section6/ui/you_viewer_v1.0.ui')[0]

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initAuthLock()

    def initAuthLock(self):
        self.previewButten.setEnabled(False)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec()
