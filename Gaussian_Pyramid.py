import cv2
import numpy as np

def cv2show(name : str, img ):
    cv2.imshow(name, img)
    cv2.waitKey(0)

if __name__ == '__main__':
    img1 = cv2.imread(r'./1.jpg')
    cv2show('img1',img1)
    print(img1.shape)

    # pryUp = upsampling = oversampling 
    up = cv2.pyrUp(img1)
    cv2show('up',up)
    print(up.shape)
  
    # pryDown = downsampling
    down = cv2.pyrDown(img1)
    cv2show('down',down)
    print(down.shape)

    # 一張圖片進行上取樣 (經過一次高斯濾波(損失訊息)) → 再進行降取樣 (又經高斯濾波(損失信行)) → 雖然圖形大小與原圖相同，但資訊比原圖形還少 → 更加模糊、失真
    img2 = cv2.pyrDown(up)
    cv2show('img2',img2)
    print(img2.shape)

    cv2show('img1vsimg2',np.hstack((img1,img2)))