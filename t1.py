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
        if time1 =="":
            QMessageBox.about(self.ui,"提示","请输入触发时间")
        key1 = self.ui.key1.text()
        if key1 =="":
            QMessageBox.about(self.ui,"提示","请输入触发时间")
        time2 = self.ui.time2.text()
        key2 = self.ui.key2.text()
        ipAddr = self.ui.ipAddr.text()
        port = self.ui.ipAddr.text()
        print(type(time1),key1,time2,key2,ipAddr,port)


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()