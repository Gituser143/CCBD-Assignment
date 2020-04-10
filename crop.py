import cv2
import numpy as np
import os
import math
import csv
import copy

images_folder_path = os.path.abspath(os.path.join('images')) + '/'
generated_folder_path = os.path.abspath(os.path.join('generated')) + '/'
images = os.listdir(images_folder_path)

#Dimensions
y = 180
x = 650
w = 1030
h = 690

for image in images:
    img = cv2.imread(images_folder_path + image)
    crop_img = img[y:y+h, x:x+w]
    cv2.imwrite(generated_folder_path + image, crop_img)
