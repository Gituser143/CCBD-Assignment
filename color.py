import cv2
import numpy as np

ip_image = cv2.imread('generated/560079.png')
# cv2.imshow('yeet',a)
# cv2.waitKey(0)


# green_pixel_coords = []
# for i in range(0,ip_image.shape[0]):
#     for j in range(0,ip_image.shape[1]):
#         if ip_image[i,j][1]>180 and ip_image[i,j][2]>125 and ip_image[i,j][2]<155 and ip_image[i,j][0]<100 and ip_image[i,j][1]<230:
#             green_pixel_coords.append([i,j])

# print(green_pixel_coords)

hsv = cv2.cvtColor(ip_image, cv2.COLOR_BGR2HSV) 

lower_green = np.array([40, 0, 0]) 
upper_green = np.array([100, 255, 255]) 

# lower_green = np.array([21, 50, 136]) 
# upper_green = np.array([106, 137, 28]) 
  
maskg = cv2.inRange(hsv, lower_green, upper_green) 

green_pixel_coords = []

for i in range(0, maskg.shape[0]):
    for j in range(0,maskg.shape[1]):
        # print(maskg[i,j])
        if maskg[i,j] == 255:
            green_pixel_coords.append([i,j])

num_pixels = ip_image.shape[0] * ip_image.shape[1]
x = len(green_pixel_coords)
print(num_pixels)
print(x)
print(x/num_pixels)


cv2.imwrite('extra/maskg.png',maskg)
cv2.waitKey(0)
