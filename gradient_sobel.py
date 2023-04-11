# utlize Sobel operator (filter) to get Image gradient
import cv2
import numpy as np
def cv2show(name : str, img ):
    cv2.imshow(name, img)
    cv2.waitKey(0)

img1 = cv2.imread('./1.jpg',0)
img1 = cv2.resize(img1,(0,0),fx = 0.8, fy = 0.8)

print('圖形格式為 (高，寬，通道數) :', img1.shape)
print(img1)

# pixel 於 X 方向 (左到右 → ) 的圖像梯度


# 3 * 3 Sobel filter取得計算pixel的梯度
newimg1=img1.copy()

# cv2.CV_64F 格式可以表示灰階負數的形式 (理應是數值範圍變廣了)
# 儘管可顯示的數值範圍變廣了 ， 但是 灰階依然是 0 - 255 ，負灰階會被系統截斷，都變為 0 
sobelx = cv2.Sobel(newimg1, cv2.CV_64F, 1, 0 ,ksize=3)
# 將負灰階取絕對值，就可以知道"實際整張圖的梯度大小 -> 即可知道邊界
sobelx = cv2.convertScaleAbs(sobelx)

# new_img = np.hstack((img1,sobelx))
cv2show('Sobel X', sobelx)

# pixel 於 Y 方向 (上到下 ↓ ) 的圖像梯度

sobely = cv2.Sobel(newimg1, cv2.CV_64F, 0, 1 ,ksize=3)
sobely = cv2.convertScaleAbs(sobely)
cv2show('Sobel Y', sobely)

# 分別計算 X 、 Y 方向梯度後， 在求和 → 可以得出 Sobel(X,Y)
sobelxy = cv2.addWeighted(sobelx, 0.5 , sobely, 0.5 , 0)
# sobelxy = 0.5*(sobel(x),0) + 0.5(0,sobel(y)) # 依照權重分配 取得sobelxy
sobelxy = cv2.convertScaleAbs(sobelxy)
cv2show('Sobel XY', sobelxy)

# 如果我直接使用 cv2.Sobel(src,depth,1,1,ksize=3) : 不就可以達成 X - Y 方向的圖像梯度計算了嗎?
# 但是，與分別解析後相加的效果來說，直接呼叫函數的結果較差!
sobelxy_direct = cv2.Sobel(newimg1, cv2.CV_64F, 1, 1 ,ksize=3)
sobelxy_direct = cv2.convertScaleAbs(sobelxy_direct)
cv2show('Sobel XY direct', sobelxy_direct)