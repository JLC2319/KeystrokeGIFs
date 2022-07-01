import cv2

path = 'logitechK120.png'

img = cv2.imread(path, cv2.IMREAD_COLOR)

window_name = path

rects = [{'x':165,'y':220,'w':55,'h':55}, #esc

{'x':265,'y':220,'w':55,'h':55}, #f1
{'x':325,'y':220,'w':55,'h':55}, #f2
{'x':385,'y':220,'w':55,'h':55}, #f3
{'x':445,'y':220,'w':55,'h':55}, #f4

{'x':525,'y':220,'w':55,'h':55}, #f5
{'x':585,'y':220,'w':55,'h':55}, #f6
{'x':645,'y':220,'w':55,'h':55}, #f7
{'x':700,'y':220,'w':55,'h':55}, #f8

{'x':785,'y':220,'w':55,'h':55}, #f9
{'x':840,'y':220,'w':55,'h':55}, #f10
{'x':900,'y':220,'w':55,'h':55}, #f11
{'x':960,'y':220,'w':55,'h':55}, #f12

{'x':1042,'y':220,'w':55,'h':55}, #print screen
{'x':900,'y':220,'w':55,'h':55}, #scroll lock
{'x':960,'y':220,'w':55,'h':55}, #pause break

]

for rect in rects: 
    startPoint = (rect['x'],rect['y'])
    endPoint = (rect['x']+rect['w'],rect['y']+rect['h'])


    color = (100, 255, 255)

    thickness = 2

    img = cv2.rectangle(img, startPoint, endPoint, color, thickness)


cv2.imshow(window_name, img)
cv2.waitKey(0)