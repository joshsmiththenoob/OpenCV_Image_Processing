# 連通元標記 (Connected Component Labelling, CC Labelling)

import cv2
import numpy as np

def cv2show(name : str,file):
    cv2.imshow(name,file)
    cv2.waitKey(0)

if __name__ == '__main__':
    # Read image with single channgel (GrayScale)
    CC_img = cv2.imread('./invert_CC.png',0)
    print(CC_img.shape)
    cv2show('testing',CC_img)
    # CC Label
    n, labels = cv2.connectedComponents(CC_img) 
    print("Num of COnnected Components =", n)
    print(labels,type(labels),labels.shape)
    cv2.normalize(labels,labels,0,255,cv2.NORM_MINMAX)
    print(labels)
    img2 = np.uint8(labels)
    cv2show('Connected Component Labeling',img2)
    