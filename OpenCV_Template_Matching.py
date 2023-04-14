import cv2
import numpy as np

def cv2show(name : str, img ):
    cv2.imshow(name, img)
    cv2.waitKey(0)

if __name__ == '__main__':
    img1 = cv2.imread(r'./1.jpg')
    img1_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    cv2show('img1',img1)
    print(img1.shape)
    print(img1[0,0])