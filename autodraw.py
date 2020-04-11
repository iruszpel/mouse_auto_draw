import pyautogui
import sys, getopt
import os  
from threading import Timer
from PIL import Image 

#Default values
inputimage = ''
basewidth = 210
time = 10


helpmessage= """Usage:
    autodraw.py -i <imagefile> 
    -i <path to image>
    -h <displays this help message>
    -w <drawing width in px, default: 210>
    -t <delay in seconds before drawing starts, default: 10>
    """
argv = sys.argv[1:]
try:
    args, vals = getopt.getopt(argv,"hi:w:t:")
except getopt.GetoptError:
    print(helpmessage)
    sys.exit(2)
for arg, val in args:
    if arg == '-h':
        print(helpmessage)
        sys.exit()
    elif arg == "-i":
        inputimage = val
    elif arg == "-w":
        basewidth = int(val)
    elif arg == "-t":
        time = int(val)


img = Image.open(inputimage) 
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
im = img.convert('1',dither=Image.FLOYDSTEINBERG)
width, height = im.size

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
pyautogui.FAILSAFE=True
pyautogui.PAUSE = 0
def draw():
    for y in range(height):
        clear()
        print('Drawing: ' + str(int((y/(height))*100)) + '%')
        for x in range(width):
            if im.getpixel((x, y)) == 0:
                pyautogui.drag(1,0)
                if x+1==width:
                    pyautogui.move(-width,1)
            else:
                if x+1==width:
                    pyautogui.move(-width+1,1)
                else:
                    pyautogui.move(1, 0)
print("Waiting " + str(time) + " seconds before drawing starts")
t = Timer(time, draw)
t.start()