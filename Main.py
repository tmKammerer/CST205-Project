import PIL
from PySide2 import QWidget, 

RGB_List={'Red':['cName: Red', 'cTuple':(255,0,0),'cHex':'#FF0000'],
 'Green':['cName':'Green', 'cTuple':(0,128,0), 'cHex':'#008000'], 'Blue':['cName':'Blue', 'cTuple':(0,0,255), 'cHex':'#0000FF']
 'Yellow':['cName':'Yellow', 'cTuple':(255,255,0), 'cHex':'#FFFF00'], 'Gold':['cName':'Gold', 'cTuple':(255,215,0), 'cHex':'#FFD700'],
 'Magenta':['cName':'Magenta', 'cTuple':(255,0,255), 'cHex':'#FF00FF'], 'Bisque':['cName':'Bisque', 'cTuple':(255,228,196), 'cHex':'#FFE4C4'],
 'Indigo':['cName':'Indigo', 'cTuple':(75,0,130), 'cHex':'#4B0082'], 'Turquoise':['cName':'Turquoise', 'cTuple':(64,224,208), 'cHex':'#40E0D0'],
 'Chocolate':['cName':'Chocolate', 'cTuple':(210,105,30), 'cHex':'#D2691E'],'Olive':['cName':'Olive', 'cTuple':(128,128,0), 'cHex':'#808000'],
 'Salmon':['cName':'Salmon', 'cTuple':(250,128,114), 'cHex':'#FA8072'], 'Orange':['cName':'Orange', 'cTuple':(255,165,0), 'cHex':'#FFA500'],
 'Teal':['cName':'Teal', 'cTuple':(0,128,128), 'cHex':'#008080'], 'Purple':['cName':'Purple', 'cTuple':(128,0,128), 'cHex':'#800080'],
 'Tan':['cName':'Tan', 'cTuple':(210,180,140), 'cHex':'#D2B48C'], 'Lime':['cName':'Lime', 'cTuple':(0,255,0), 'cHex':'#00FF00'],
 'Coral':['cName':'Coral', 'cTuple':(255,127,80), 'cHex':'#FF7F50'], 'Violet':['cName':'Violet', 'cTuple':(238,130,238), 'cHex':'#EE82EE'],
 'Khaki':['cName':'Khaki', 'cTuple':(240,230,140), 'cHex':'#F0E68C']}

Grayscale_List={'Black':['cName':'Black', 'cTuple':(0,0,0), 'cHex':'#000000'], 'Dark Charcoal':['cName':'Dark Charcoal', 'cTuple':(51,51,51), 'cHex': '#333333'],
  'Spanish Gray':['cName':'Spanish Gray', 'cTuple':(153,153,153), 'cHex':'#999999'], 'Gray':['cName':'Gray', 'cTuple':(128,128,128), 'cHex':'#808080'],
  'Silver':['cName':'Silver','cTuple':(192,192,192), 'cHex':'#C0C0C0'], 'Gainsboro':['cName':'Gainsboro', 'cTuple':(220,220,220), 'cHex':'#DCDCDC'],
  'White':['cName':'White', 'cTuple':(255,255,255), 'cHex':'#FFFFFF']}


for color in RGB_List:
  if colormatch == color[cTuple]:
    print({color[cName]})
    print({color[cHex]})
    
