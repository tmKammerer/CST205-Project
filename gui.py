import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QDialog, QGroupBox,
                               QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit,
                               QRadioButton)
from PySide2.QtCore import Slot

from PIL import Image

from tkinter import *
# New imports for adding radio button




RGB_List=[{'cName': 'Red', 'cTuple':(255,0,0),'cHex':'#FF0000'},
 {'cName':'Green', 'cTuple':(0,128,0), 'cHex':'#008000'}, {'cName':'Blue', 'cTuple':(0,0,255), 'cHex':'#0000FF'},
 {'cName':'Yellow', 'cTuple':(255,255,0), 'cHex':'#FFFF00'}, {'cName':'Gold', 'cTuple':(255,215,0), 'cHex':'#FFD700'},
 {'cName':'Magenta', 'cTuple':(255,0,255), 'cHex':'#FF00FF'}, {'cName':'Bisque', 'cTuple':(255,228,196), 'cHex':'#FFE4C4'},
 {'cName':'Indigo', 'cTuple':(75,0,130), 'cHex':'#4B0082'}, {'cName':'Turquoise', 'cTuple':(64,224,208), 'cHex':'#40E0D0'},
 {'cName':'Chocolate', 'cTuple':(210,105,30), 'cHex':'#D2691E'},{'cName':'Olive', 'cTuple':(128,128,0), 'cHex':'#808000'},
 {'cName':'Salmon', 'cTuple':(250,128,114), 'cHex':'#FA8072'}, {'cName':'Orange', 'cTuple':(255,165,0), 'cHex':'#FFA500'},
 {'cName':'Teal', 'cTuple':(0,128,128), 'cHex':'#008080'}, {'cName':'Purple', 'cTuple':(128,0,128), 'cHex':'#800080'},
 {'cName':'Tan', 'cTuple':(210,180,140), 'cHex':'#D2B48C'}, {'cName':'Lime', 'cTuple':(0,255,0), 'cHex':'#00FF00'},
 {'cName':'Coral', 'cTuple':(255,127,80), 'cHex':'#FF7F50'}, {'cName':'Violet', 'cTuple':(238,130,238), 'cHex':'#EE82EE'},
 {'cName':'Khaki', 'cTuple':(240,230,140), 'cHex':'#F0E68C'}]

Grayscale_List=[{'cName':'Black', 'cTuple':(0,0,0), 'cHex':'#000000'}, {'cName':'Dark Charcoal', 'cTuple':(51,51,51), 'cHex': '#333333'},
  {'cName':'Spanish Gray', 'cTuple':(153,153,153), 'cHex':'#999999'}, {'cName':'Gray', 'cTuple':(128,128,128), 'cHex':'#808080'},
  {'cName':'Silver','cTuple':(192,192,192), 'cHex':'#C0C0C0'}, {'cName':'Gainsboro', 'cTuple':(220,220,220), 'cHex':'#DCDCDC'},
  {'cName':'White', 'cTuple':(255,255,255), 'cHex':'#FFFFFF'}]

class NewWindow(QWidget):
  def __init__(self, colorChoice):
    super().__init__()
    
    #Window Title
    self.gui=tK(className=f'{colorChoice['cName']}')
    self.gui.geometry("400x400")
    self.gui.configure(bg=f'{colorChoice['cTuple']}')
    
    
  
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Window Title
        self.setWindowTitle("Color Calculator")

        # Need input of R,G,B in order to get number
        self.label_title = QLabel(
            'Hello! Enter your RGB value or HEX values to find your desired color.  ')

        # Created a box layout
        vbox1 = QVBoxLayout()


        # adding radio button
        radiobutton = QRadioButton("RGB")
        radiobutton.setChecked(True)
        radiobutton.type = "RGB"
        radiobutton.toggled.connect(self.onColorTypeClicked)
        vbox1.addWidget(radiobutton)

        radiobutton = QRadioButton("Grayscale")
        radiobutton.type = "Grayscale"
        radiobutton.toggled.connect(self.onColorTypeClicked)
        vbox1.addWidget(radiobutton)

        self.label_r = QLabel('Input R: ')
        self.liner_edit = QLineEdit()
        self.label_g = QLabel('Input G: ')
        self.lineg_edit = QLineEdit()
        self.label_b = QLabel('Input B: ')
        self.lineb_edit = QLineEdit()
        
        # This line_edit input is for Hex
        self.label_hex = QLabel('Input Hex: ')
        self.lineh_edit = QLineEdit()

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
        color= (self.liner_edit, self.lineg_edit, self.lineb_edit)
        if radioButton.type=="RGB":
          for x in RGB_list:
            if color==x['cTuple']:
              self.newWin= NewWindow(RGB_List[x])
        else if radioButton.type=="Grayscale":
          for x in Grayscale_List:
            if color == x['cTuple']:
              self.newWin= NewWindow(Grayscale_list[x])

    def onColorTypeClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print("Color Type is %s" % (radioButton.type))


app = QApplication([])
my_win = MyWindow()
my_win.show()
app.exec_()
