import sys
from tkinter import CENTER
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,200,600,800)
        self.setWindowTitle('03_17.py')
        btn1 = QPushButton('버튼1', self)
        btn1.move(20,20)
        btn1.clicked.connect(self.btn1_clicked)
        btn2 = QPushButton('버튼2', self)
        btn2.move(20,60)
        btn2.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        print('버튼1 클릭!')
    def btn2_clicked(self):
        print('버튼2 클릭!') 


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()