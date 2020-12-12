import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QGroupBox, 
                                  QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit)
from PySide2.QtCore import Slot                            

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Color Calculator")
        self.label3 = QLabel('Hello! Enter your RGB value or HEX values to find your desired color.  ')
        self.label1 = QLabel('Input R: ')
        self.line_edit = QLineEdit()
        self.labelg = QLabel('Input G: ')
        self.lineg_edit = QLineEdit()
        self.labelb = QLabel('Input B: ')
        self.lineb_edit = QLineEdit()

        self.label2 = QLabel('Input: ')
        self.line2_edit = QLineEdit()

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label3)
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.line_edit)
        vbox1.addWidget(self.labelg)
        vbox1.addWidget(self.lineg_edit)
        vbox1.addWidget(self.labelb)
        vbox1.addWidget(self.lineb_edit)
        vbox1.addWidget(self.label2)
        vbox1.addWidget(self.line2_edit)

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