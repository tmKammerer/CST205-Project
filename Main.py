import PIL
from PySide2 import QWidget, 

RGB_List={'color':[{'cName': 'Red', 'cTuple':(255,0,0),'cHex':'#FF0000'},
 {'cName':'Green', 'cTuple':(0,128,0), 'cHex':'#008000'}, {'cName':'Blue', 'cTuple':(0,0,255), 'cHex':'#0000FF'},
 {'cName':'Yellow', 'cTuple':(255,255,0), 'cHex':'#FFFF00'}, {'cName':'Gold', 'cTuple':(255,215,0), 'cHex':'#FFD700'},
 {'cName':'Magenta', 'cTuple':(255,0,255), 'cHex':'#FF00FF'}, {'cName':'Bisque', 'cTuple':(255,228,196), 'cHex':'#FFE4C4'},
 {'cName':'Indigo', 'cTuple':(75,0,130), 'cHex':'#4B0082'}, {'cName':'Turquoise', 'cTuple':(64,224,208), 'cHex':'#40E0D0'},
 {'cName':'Chocolate', 'cTuple':(210,105,30), 'cHex':'#D2691E'},{'cName':'Olive', 'cTuple':(128,128,0), 'cHex':'#808000'},
 {'cName':'Salmon', 'cTuple':(250,128,114), 'cHex':'#FA8072'}, {'cName':'Orange', 'cTuple':(255,165,0), 'cHex':'#FFA500'},
 {'cName':'Teal', 'cTuple':(0,128,128), 'cHex':'#008080'}, {'cName':'Purple', 'cTuple':(128,0,128), 'cHex':'#800080'},
 {'cName':'Tan', 'cTuple':(210,180,140), 'cHex':'#D2B48C'}, {'cName':'Lime', 'cTuple':(0,255,0), 'cHex':'#00FF00'},
 {'cName':'Coral', 'cTuple':(255,127,80), 'cHex':'#FF7F50'}, {'cName':'Violet', 'cTuple':(238,130,238), 'cHex':'#EE82EE'},
 {'cName':'Khaki', 'cTuple':(240,230,140), 'cHex':'#F0E68C'}]}

Grayscale_List={'grayscale':[{'cName':'Black', 'cTuple':(0,0,0), 'cHex':'#000000'}, {'cName':'Dark Charcoal', 'cTuple':(51,51,51), 'cHex': '#333333'},
  {'cName':'Spanish Gray', 'cTuple':(153,153,153), 'cHex':'#999999'}, {'cName':'Gray', 'cTuple':(128,128,128), 'cHex':'#808080'},
  {'cName':'Silver','cTuple':(192,192,192), 'cHex':'#C0C0C0'}, {'cName':'Gainsboro', 'cTuple':(220,220,220), 'cHex':'#DCDCDC'},
  {'cName':'White', 'cTuple':(255,255,255), 'cHex':'#FFFFFF'}]}


for color in RGB_List:
  if colormatch == color[cTuple]:
    print({f'{color[cName]}')
    print(f'{color[cHex]}')
    
