import cv2
img1 = cv2.imread('./1.jpg')

print('圖形格式為 (高，寬，通道數) :', img1.shape)
print(img1)
cv2.imshow('img1',img1)
cv2.waitKey(0)