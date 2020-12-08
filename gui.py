from PySide2.QtWidgets import *

app = QApplication([]) 
window = QWidget() # Create a window.
window.setWindowTitle('Calculator')
layout = QVBoxLayout() # Create a layout.
button = QPushButton("Click Button") 
layout.addWidget(button) 
window.setLayout(layout) # Pass the layout to the window
window.show() 
app.exec_() 