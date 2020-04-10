import cv2
import os
import csv
import numpy as np


images_folder_path = os.path.abspath(os.path.join('generated')) + '/'
generated_folder_path = os.path.abspath(os.path.join('color')) + '/'
images = os.listdir(images_folder_path)

lower_green = np.array([40, 0, 0]) 
upper_green = np.array([100, 255, 255]) 


for image in images:
    img = cv2.imread(images_folder_path + image)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
    maskg = cv2.inRange(hsv, lower_green, upper_green) 
    cv2.imwrite(generated_folder_path + image, maskg)
