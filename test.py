from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import uic
import sys

def run():
    print("program run")
    global  A
    A = ui.time1.text()

def save():


global A
A = 'B'
app = QApplication([])
ui = uic.loadUi('UI/fish_controller.ui')

ui.run.clicked.connect(run)
ui.save.clicked.connect(save)
ui.show()
app.exec_()
print(A)