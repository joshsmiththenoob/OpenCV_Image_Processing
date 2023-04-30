# 連通元標記 (Connected Component Labelling, CC Labelling)

import cv2
import numpy as np

def cv2show(name : str,file):
    cv2.imshow(name,file)
    cv2.waitKey(0)

if __name__ == '__main__':
    # Read image with single channgel (GrayScale)
    CC_img = cv2.imread('./invert_CC.png',0)
    cv2show('testing',CC_img)
    print(type(CC_img),CC_img.dtype)
    # Turn datatype to sign including Negative Value
    CC_img = np.array(CC_img, dtype=np.int32)
    CC_img = CC_img - 255
    print(CC_img)
    # Using Abs to turn the unsign value
    CC_img = cv2.convertScaleAbs(CC_img)
    # Turn dtype to uint8 that can display on screen
    CC_img = np.array(CC_img,dtype=np.uint8)
    print(CC_img)
    
    cv2show('testing',CC_img)


    # Method II : jRegular Method
    # Read image with single channgel (GrayScale)
    CC_img = cv2.imread('./CC_label.png', 0)
    cv2show('testing', CC_img)
    print(CC_img)
    
    # Invert the grayscale image using NumPy operations
    max_value = np.iinfo(CC_img.dtype).max
    inv_img = max_value - CC_img
    
    # Convert the image back to uint8 data type
    print(inv_img)

    cv2show('testing', inv_img)
