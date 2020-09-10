from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

class Stats():
    def __init__(self):
        self.ui = QUiLoader().load('UI/fish_controller.ui')
        self.ui.run.clicked.connect(self.run_game)
        self.ui.save.clicked.connect(self.save)


    def run_game(self):
        print("程序开始")

    def save(self):
        time1 = self.ui.time1.text()
        print(time1)


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()