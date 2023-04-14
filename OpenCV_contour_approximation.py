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
    # I. Find Contour
    # 圖形二值化 binary : 灰階值>127 → 255 ， 灰階值<127 → 0 
    ret, thresh = cv2.threshold(img1_gray, 127, 255, cv2.THRESH_BINARY)
    cv2show('Binarize', thresh)

    # 尋找二值化後圖形的輪廓
    contours, hierarchy  = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # contours (描述輪廓的list), hierarchy (階級(目前不重要))
  
    # 找到紀錄輪廓的list (contours)後，接下來直接使用method畫出來 
    cv2.drawContours(img1, contours, -1 ,( 0, 255, 255) , 1) # (src, contours , index of contours (-1 to draw all contours), (B,G,R), thickness)
    cv2show('Contours',img1)

    # II. estimate Approximation Contour (只能找到Contours(list裝有多個輪廓)其中一個輪廓並繪製近似輪廓)
    one_contour = contours[21]                              # 從裝有許多輪廓的列表中，取出一個輪廓
    epsilon = 0.1 * cv2.arcLength(one_contour,True)      # arcLength, 計算目標輪廓的周長，可以藉由調整閾值epsilon來找出一個近似輪廓
    print('周長為 : ', cv2.arcLength(one_contour,True))
    approx = cv2.approxPolyDP(one_contour, epsilon, True)
    cv2.drawContours(img1, [approx], -1 ,( 255, 255, 0) , 2)
    cv2show('Contours vs Approx Contours',img1)