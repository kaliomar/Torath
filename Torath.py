import sys

from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow

class Comp(QWidget):
    pass

class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()

        self.init_ui()

    def init_ui(self):
        pass

        self.show()

app = QApplication(sys.argv)
win = window()
sys.exit(app.exec_())