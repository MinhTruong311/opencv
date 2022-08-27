import cv2
import numpy as np

img = cv2.imread('image for python/her86.jpg')
#img = cv2.resize(img, (400,400))
img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
#cv2.imwrite('new.jpg', img)

#print(img.shape)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()