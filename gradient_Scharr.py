# utlize Sobel operator (filter) to get Image gradient
import cv2
import numpy as np
def cv2show(name : str, img ):
    cv2.imshow(name, img)
    cv2.waitKey(0)

if __name__ == '__main__':
    img1 = cv2.imread(r'./1.jpg',0)
    img1 = cv2.resize(img1,(0,0),fx = 0.8, fy = 0.8)

    print('圖形格式為 (高，寬，通道數) :', img1.shape)
    print(img1)
    cv2show('Origin', img1)

    # pixel 於 X 方向 (左到右 → ) 的圖像梯度


    # 3 * 3 Sobel filter取得計算pixel的梯度
    newimg1=img1.copy()

    # cv2.CV_64F 格式可以表示灰階負數的形式 (理應是數值範圍變廣了)
    # 儘管可顯示的數值範圍變廣了 ， 但是 灰階依然是 0 - 255 ，負灰階會被系統截斷，都變為 0 
    scharrx = cv2.Scharr(newimg1, cv2.CV_64F, 1, 0 )
    # 將負灰階取絕對值，就可以知道"實際整張圖的梯度大小 -> 即可知道邊界
    scharrx = cv2.convertScaleAbs(scharrx)

    # new_img = np.hstack((img1,sobelx))
    cv2show('Sobel X', scharrx)

    # pixel 於 Y 方向 (上到下 ↓ ) 的圖像梯度

    scharry = cv2.Scharr(newimg1, cv2.CV_64F, 0, 1 )
    scharry = cv2.convertScaleAbs(scharry)
    cv2show('Sobel Y', scharry)

    # 分別計算 X 、 Y 方向梯度後， 在求和 → 可以得出 Sobel(X,Y)
    scharrxy = cv2.addWeighted(scharrx, 0.5 , scharry, 0.5 , 0)
    # sobelxy = 0.5*(sobel(x),0) + 0.5(0,sobel(y)) # 依照權重分配 取得sobelxy
    scharrxy = cv2.convertScaleAbs(scharrxy)
    cv2show('Sobel XY', scharrxy)

    # Scharr 方法不能直接使用 X - Y 梯度量測
    #  !! scharrxy_direct = cv2.Scharr(newimg1, cv2.CV_64F, 1, 1)