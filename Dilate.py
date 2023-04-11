import cv2
import numpy as np
img1 = cv2.imread('./1.jpg',0)
img1 = cv2.resize(img1,(0,0),fx = 0.8, fy = 0.8)

print('圖形格式為 (高，寬，通道數) :', img1.shape)
print(img1)


kernel = 1 * np.ones((3,3),np.uint8) # let np dtype becomes uint8 like pict's we read
img_dilate = cv2.dilate(img1,kernel,iterations = 2)

kernel = 0.01 * np.ones((3,3), np.uint8)
img_dilate_1 = cv2.dilate(img1,kernel,iterations = 20)

new_img = np.hstack((img1,img_dilate,img_dilate_1))
cv2.imshow('newimg',new_img)
cv2.waitKey(0)

