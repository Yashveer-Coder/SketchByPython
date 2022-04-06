import cv2    #YOU NEED TO RUN THIS COMMAND FIRST IN CMD" pip install opencv-python"WOTHOUT IT CODE WONT WORK! 
image = cv2.imread("mj.jpg") #YOUR IMAGE SHOULD BE IN THE SAME FOLDER IN WHICh YOUR CODE IS SAVED ELSE IT WILL GIVE ERROR!
                           #YOU CAN CHOOSE ANY IMAGE BUT WITH MORE LIGHTING OR FILTERS THE QUALITY OF SKETCH MAY DECREASE
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(invert, (21,21),0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

cv2.imwrite("sketch.png", sketch)
