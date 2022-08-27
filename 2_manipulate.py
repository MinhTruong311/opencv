import cv2
import random

img = cv2.imread('image/mom.jpg')
img = cv2.resize(img, (0, 0), fx = 0.4, fy = 0.4)
#print(img.shape)
tag = img[200: 600, 200: 300]
img[100:500, 150:250] = tag
#print(img[400][45])
'''for i in range(100):
    for j in range (img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]'''



cv2.imshow('Image6',img)
cv2.waitKey(0)
cv2.destroyAllWindows()