import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QGroupBox, 
                                  QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit)
class MyWindow(QWidget):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Color Calculator")
    self.label3 = QLabel('Hello! Enter your RGB value or HEX values to find your desired color.  ')
    self.label1 = QLabel('Input: ')
    self.line_edit = QLineEdit()

    self.label2 = QLabel('Input: ')
    self.line2_edit = QLineEdit()

    hbox1 = QVBoxLayout()
    hbox1.addWidget(self.label3)
    hbox1.addWidget(self.label1)
    hbox1.addWidget(self.line_edit)
    hbox1.addWidget(self.label2)
    hbox1.addWidget(self.line2_edit)

    gbox1 = QGroupBox('Welcome to the color calculator!')
    gbox1.setLayout(hbox1)

   

    mbox = QVBoxLayout()
    mbox.addWidget(gbox1)

    self.setLayout(mbox)
    

app = QApplication([])
win = MyWindow()
win.show()
app.exec_()