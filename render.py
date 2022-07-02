from cgitb import text
from distutils.log import error
import cv2
import numpy
from moviepy.editor import *



keyRectangles = [
    #top row
    [{'x':165,'y':220,'w':55,'h':55}, 'esc'],

    [{'x':265,'y':220,'w':55,'h':55}, 'f1'],
    [{'x':325,'y':220,'w':55,'h':55}, 'f2'],
    [{'x':385,'y':220,'w':55,'h':55}, 'f3'],
    [{'x':445,'y':220,'w':55,'h':55}, 'f4'],

    [{'x':525,'y':220,'w':55,'h':55}, 'f5'],
    [{'x':585,'y':220,'w':55,'h':55}, 'f6'],
    [{'x':645,'y':220,'w':55,'h':55}, 'f7'],
    [{'x':700,'y':220,'w':55,'h':55}, 'f8'],

    [{'x':785,'y':220,'w':55,'h':55}, 'f9'],
    [{'x':840,'y':220,'w':55,'h':55}, 'f10'],
    [{'x':900,'y':220,'w':55,'h':55}, 'f11'],
    [{'x':960,'y':220,'w':55,'h':55}, 'f12'],

    [{'x':1042,'y':220,'w':55,'h':55},'print screen'],
    [{'x':1102,'y':220,'w':55,'h':55},'scroll lock'],
    [{'x':1162,'y':220,'w':55,'h':55},'pause break'],
    #second row
    [{'x':125,'y':298,'w':55,'h':55}, '`'],
    [{'x':185,'y':298,'w':55,'h':55}, '1'],
    [{'x':245,'y':298,'w':55,'h':55}, '2'],
    [{'x':305,'y':298,'w':55,'h':55}, '3'],
    [{'x':365,'y':298,'w':55,'h':55}, '4'],
    [{'x':425,'y':298,'w':55,'h':55}, '5'],
    [{'x':485,'y':298,'w':55,'h':55}, '6'],
    [{'x':545,'y':298,'w':55,'h':55}, '7'],
    [{'x':605,'y':298,'w':55,'h':55}, '8'],
    [{'x':665,'y':298,'w':55,'h':55}, '9'],
    [{'x':725,'y':298,'w':55,'h':55}, '0'],
    [{'x':785,'y':298,'w':55,'h':55}, '-'],
    [{'x':845,'y':298,'w':55,'h':55}, '='],
    [{'x':905,'y':298,'w':110,'h':55},'backspace'],
    [{'x':1040,'y':300,'w':55,'h':55}, 'insert'],
    [{'x':1100,'y':300,'w':55,'h':55}, 'home'],
    [{'x':1160,'y':300,'w':55,'h':55}, 'page up'],


    #third row
    [{'x':125,'y':360,'w':85,'h':55}, 'tab'],
    [{'x':215,'y':360,'w':55,'h':55}, 'q'],
    [{'x':275,'y':360,'w':55,'h':55}, 'w'],
    [{'x':335,'y':360,'w':55,'h':55}, 'e'],
    [{'x':395,'y':360,'w':55,'h':55}, 'r'],
    [{'x':455,'y':360,'w':55,'h':55}, 't'],
    [{'x':515,'y':360,'w':55,'h':55}, 'y'],
    [{'x':575,'y':360,'w':55,'h':55}, 'u'],
    [{'x':635,'y':360,'w':55,'h':55}, 'i'],
    [{'x':695,'y':360,'w':55,'h':55}, 'o'],
    [{'x':755,'y':360,'w':55,'h':55}, 'p'],
    [{'x':815,'y':360,'w':55,'h':55}, '['],
    [{'x':875,'y':360,'w':55,'h':55}, ']'],
    [{'x':935,'y':360,'w':80,'h':55}, '\\'],
    [{'x':1040,'y':360,'w':55,'h':55},'delete'],
    [{'x':1100,'y':360,'w':55,'h':55},'end'],
    [{'x':1160,'y':360,'w':55,'h':55},'page down'],

    #fourth row
    [{'x':125,'y':420,'w':100,'h':55}, 'caps lock'],
    [{'x':230,'y':420,'w':55,'h':55}, 'a'],
    [{'x':290,'y':420,'w':55,'h':55}, 's'],
    [{'x':350,'y':420,'w':55,'h':55}, 'd'],
    [{'x':410,'y':420,'w':55,'h':55}, 'f'],
    [{'x':470,'y':420,'w':55,'h':55}, 'g'],
    [{'x':530,'y':420,'w':55,'h':55}, 'h'],
    [{'x':590,'y':420,'w':55,'h':55}, 'j'],
    [{'x':650,'y':420,'w':55,'h':55}, 'k'],
    [{'x':710,'y':420,'w':55,'h':55}, 'l'],
    [{'x':770,'y':420,'w':55,'h':55}, ';'],
    [{'x':830,'y':420,'w':55,'h':55}, '\''],
    [{'x':890,'y':420,'w':125,'h':55}, 'enter'],
    
    #fifth row
    [{'x':125,'y':480,'w':130,'h':52}, 'shift'],
    [{'x':260,'y':480,'w':55,'h':52}, 'z'],
    [{'x':320,'y':480,'w':55,'h':52}, 'x'],
    [{'x':380,'y':480,'w':55,'h':52}, 'c'],
    [{'x':440,'y':480,'w':55,'h':52}, 'v'],
    [{'x':500,'y':480,'w':55,'h':52}, 'b'],
    [{'x':560,'y':480,'w':55,'h':52}, 'n'],
    [{'x':620,'y':480,'w':55,'h':52}, 'm'],
    [{'x':680,'y':480,'w':55,'h':52}, ','],
    [{'x':740,'y':480,'w':55,'h':52}, '.'],
    [{'x':800,'y':480,'w':55,'h':52}, '/'],
    [{'x':860,'y':480,'w':155,'h':52}, 'shift'],

    #sixth row
    [{'x':125,'y':540,'w':85,'h':55}, 'ctrl'],
    [{'x':220,'y':540,'w':60,'h':52}, 'window'],
    [{'x':295,'y':540,'w':55,'h':52}, 'alt'],
    [{'x':370,'y':540,'w':340,'h':52},'space'],
    [{'x':730,'y':540,'w':55,'h':52}, 'alt'],
    [{'x':805,'y':540,'w':60,'h':52}, 'window'],
    [{'x':875,'y':540,'w':65,'h':52}, 'doc'],
    [{'x':950,'y':540,'w':55,'h':52}, 'ctrl'],

    #arrow keys
    [{'x':1100,'y':480,'w':55,'h':52}, 'up'],
    [{'x':1100,'y':540,'w':55,'h':52}, 'down'],
    [{'x':1040,'y':540,'w':55,'h':52}, 'left'],
    [{'x':1160,'y':540,'w':55,'h':52}, 'right'],

]


def returnkeyrect(keyStr, rects = keyRectangles):
    try:
        i = [r[1] for r in rects].index(keyStr)
        rect = [r[0] for r in rects][i]
        return rect    
    except:
        print(f'-- {keyStr} -- Key not found. see reference: ', [r[1] for r in rects])
        return {'x':0,'y':0,'w':0,'h':0}

def highlightKeys(img, keys, color = (255, 0, 0), lineThickness = 3):
    retImg = img.copy()
    for rect in [returnkeyrect(key) for key in keys]:
        startPoint = (rect['x'],rect['y'])
        endPoint = (rect['x']+rect['w'],rect['y']+rect['h'])
        retImg = cv2.rectangle(retImg, startPoint, endPoint, color, lineThickness)
    return retImg
    

def makeKeyStrokeImgs(keyCombos:list[list[str]], img):
    beforeAfter = img.copy()
    imgs = [beforeAfter]

    for keyStroke in keyCombos:
        keyStrokeImg = highlightKeys(img.copy(), keyStroke)
        imgs.append(keyStrokeImg)
    imgs.append(beforeAfter)
    imgs = [img[180:620, 120:1235] for img in imgs]
    return imgs

def makeKeystrokeGif(keystroke, img, filename:str, fps=.5):
    clip = ImageSequenceClip(makeKeyStrokeImgs(keystroke,img), fps=.75)
    if not filename.endswith('.gif'):
        filename = filename+'.gif'
    clip.write_gif(filename)
    return clip


path = 'logitechK120.png'

img = cv2.imread(path, cv2.IMREAD_COLOR)
exampleKeystroke = [
    ['alt'],
    ['alt', 'tab']
    ]


from keystrokes import keystrokes

for application in keystrokes:
    for keystroke in application['keystrokes']:
        print(application['program'],keystroke['name'], keystroke['keystroke'])
        makeKeystrokeGif(keystroke['keystroke'], img, 'keystrokeGifs/'+application['program']+'-'+keystroke['name'])


#makeKeystrokeGif(exampleKeystroke, img, 'testkeystroke')
