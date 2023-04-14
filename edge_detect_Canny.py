# Canny 邊緣檢測 : 在 求出"圖形X-Y梯度"後，進行特定的過濾步驟(非極大值抑制+雙閾值檢測+抑制孤立弱邊緣)，進而產生出真正的邊緣圖形出來 !
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

    # Laplacian 方法只能能直接使用 X - Y 梯 度量測
    v1 = cv2.Canny(img1,80,150)  # 雙閾值檢測 (梯度最小值MinValue，圖像梯度最大值MaxValue))
    v2 = cv2.Canny(img1,50,100)  # 

    new = np.hstack((v1,v2))
    cv2show('twoCanny',new)