import numpy as np
import cv2

# Generate a 16x16 numpy array of random grayscale values between 0 and 255
img = np.random.randint(low=0, high=256, size=(16,16), dtype=np.uint8)
zoomed = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_LINEAR)
# Display the image using OpenCV
print(img,type(img))
cv2.imshow("Random Image", zoomed)
cv2.waitKey(0)
cv2.destroyAllWindows()
crop_img=img[0:1,0:2]
print(crop_img,crop_img.shape)
list = [1,2,3]
print(list[0:2])