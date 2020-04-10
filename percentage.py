import cv2
import os
import csv
import numpy as np


images_folder_path = os.path.abspath(os.path.join('generated')) + '/'
generated_folder_path = os.path.abspath(os.path.join('color')) + '/'
images = os.listdir(images_folder_path)

lower_green = np.array([40, 0, 0]) 
upper_green = np.array([100, 255, 255]) 
green_pixel = []
num_pixels = []

with open("info.txt", "a") as file_object:

    for image in images:
        img = cv2.imread(images_folder_path + image)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
        maskg = cv2.inRange(hsv, lower_green, upper_green) 
        cv2.imwrite(generated_folder_path + image, maskg)

        for i in range(0, maskg.shape[0]):
            for j in range(0,maskg.shape[1]):
                num_pixels.append([i,j])
                if maskg[i,j] == 255:
                    green_pixel.append([i,j])

        l = len(num_pixels)
        g = len(green_pixel)
        perc= round( (g/l*100) , 2)
        file_object.write(image + "," + str(perc))
        file_object.write("\n")


file_object.close()