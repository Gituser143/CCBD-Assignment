import cv2
import numpy as np
import os
import math
import csv
import copy

images_folder_path = os.path.abspath(os.path.join( 'images'))
generated_folder_path = os.path.abspath(os.path.join('Generated'))

img = cv2.imread('/home/skete/CCBD-Assignment/images/560001.png')

y=180
x=650
w=1030
h=690
crop_img = img[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)
cv2.imwrite('/home/skete/CCBD-Assignment/generated/560001.png',crop_img)

