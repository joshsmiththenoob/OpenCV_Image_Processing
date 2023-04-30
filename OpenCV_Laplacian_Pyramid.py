import cv2
import numpy as np

def cv2show(name : str, img ):
    cv2.imshow(name, img)
    cv2.waitKey(0)

if __name__ == '__main__':
    img1 = cv2.imread(r'./1.jpg')
    cv2show('img1',img1)
    print(img1.shape)

    # L1 = 原圖 - Upsampling(Downsampling(原圖))
    
    L1 = img1 - cv2.pyrUp(cv2.pyrDown(img1))
    compare_Laplacian = np.hstack((img1,L1))
    
    cv2show('Compare Laplacian',compare_Laplacian)