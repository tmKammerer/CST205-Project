import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QGroupBox, 
                                  QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit)
from PySide2.QtCore import Slot                            

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        #Window Title
        self.setWindowTitle("Color Calculator")

        self.label_title = QLabel('Hello! Enter your RGB value or HEX values to find your desired color.  ')
        self.label_r = QLabel('Input R: ')
        self.liner_edit = QLineEdit()
        self.label_g = QLabel('Input G: ')
        self.lineg_edit = QLineEdit()
        self.label_b = QLabel('Input B: ')
        self.lineb_edit = QLineEdit()

        self.label_hex = QLabel('Input: ')
        self.lineh_edit = QLineEdit()

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label_title)
        vbox1.addWidget(self.label_r)
        vbox1.addWidget(self.liner_edit)
        vbox1.addWidget(self.label_g)
        vbox1.addWidget(self.lineg_edit)
        vbox1.addWidget(self.label_b)
        vbox1.addWidget(self.lineb_edit)
        vbox1.addWidget(self.label_hex)
        vbox1.addWidget(self.lineh_edit)

        gbox1 = QGroupBox('Welcome to the color calculator!')
        gbox1.setLayout(vbox1)
        
        mbox = QVBoxLayout()
        mbox.addWidget(gbox1)

        
        self.my_btn = QPushButton("Submit")
        self.my_lbl = QLabel('Button not clicked')
        self.my_btn.clicked.connect(self.on_click)
        vbox1.addWidget(self.my_btn)
        vbox1.addWidget(self.my_lbl)
        self.setLayout(vbox1)
        self.setLayout(mbox)

        hbox = QHBoxLayout()
        gbox1.setLayout(hbox)

    @Slot()
    def on_click(self):
        self.my_lbl.setText('Button clicked')
        self.repaint()

app = QApplication([])
my_win = MyWindow()
my_win.show()
app.exec_()