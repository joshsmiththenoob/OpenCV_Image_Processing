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
    # 圖形二值化 binary : 灰階值>127 → 255 ， 灰階值<127 → 0 
    ret, thresh = cv2.threshold(img1_gray, 127, 255, cv2.THRESH_BINARY)
    cv2show('Binarize', thresh)

    # 尋找二值化後圖形的輪廓
    contours, hierarchy  = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # contours (描述輪廓的list), hierarchy (階級(目前不重要))
  
    # 找到紀錄輪廓的list (contours)後，接下來直接使用method畫出來 
    cv2.drawContours(img1, contours, -1 ,( 0, 255, 255) , 1) # (src, contours , index of contours (-1 to draw all contours), (B,G,R), thickness)
    cv2show('Contours',img1)