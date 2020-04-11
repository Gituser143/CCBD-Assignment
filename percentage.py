import cv2
import os
import csv
import numpy as np


images_folder_path = os.path.abspath(os.path.join('generated')) + '/'
generated_folder_path = os.path.abspath(os.path.join('masks')) + '/'
images_list = os.listdir(images_folder_path)
images = [i.split('.')[0] for i in images_list]

lower_green = np.array([40, 0, 0])
upper_green = np.array([100, 255, 255])

if os.path.exists("data.txt"):
  os.remove("data.txt")
else:
  print("The file 'data.txt' does not exist")

with open("data.txt", "a") as file_object:

    for image in images:

        img = cv2.imread(images_folder_path + image + '.png')
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        maskg = cv2.inRange(hsv, lower_green, upper_green)
        cv2.imwrite(generated_folder_path + image + '.png', maskg)

        green_pixels = 0
        total_pixels = img.shape[0] * img.shape[1]

        for i in range(0, maskg.shape[0]):
            for j in range(0,maskg.shape[1]):
                if maskg[i,j] == 255:
                    green_pixels += 1

        perc = round( (green_pixels / total_pixels * 100) , 2)
        
        file_object.write(image + "," + str(perc) + "\n")
