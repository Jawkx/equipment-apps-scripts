import os
import cv2 
imgsdir = os.listdir('before_resized')

w = 480
h = 480

for imgdir in imgsdir:
    if imgdir != "DO NOT DELETE THIS.txt" :
        print(imgdir)
        im = cv2.imread('before_resized/' + imgdir)
        resized = cv2.resize(im, (w,h), interpolation = cv2.INTER_AREA)
        cv2.imwrite("resized/" + imgdir ,resized )