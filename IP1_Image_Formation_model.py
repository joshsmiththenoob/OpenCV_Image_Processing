# Image Formation Model 
# 模擬數位影像的程像過程


# Image Formation Model -> f(x,y) = i(x,y) * r(x,y)
# i(x,y) : Illumination 打光函數(照明(燈源)函數) : 模擬光源於某一截面的光場分布
# r(x,y) : Reflectance (反射函數) : 一個非透明介質(物體 : 穿透率 為 0)， 則當反射率 = 0 時， 物體吸收所有(或特定波長)的光 → 部會反射任何光至 人眼 → 黑色 ， 
# 反之，當對特定波長的反射率 = 1時 → 物體會反射特定波長的光，使我們人眼能夠接受相對應波長的光 (ex: 550 nm 綠色 etc..) = 我們實際看到物體的顏色 ， 光強分布

import numpy as np
import cv2

class Img_Format_Model:
    def __init__(self) -> None:
        pass
    def image_format(self,f, x0, y0, sigma):
        g = f.copy()
        nr, nc = f.shape[:2] # nr : numbers of row (heigh) ; nc : numbers of coloum (width) -> image.shape : H,W,C
        illumination = np.zeros([nr,nc], dtype = np.float32)
        
        # Simulate point of light source - Illumination function : it's intensity distribution of section was like 2-DGuassian distribution
        for x in range(nr) :
            for y in range(nc) : # 每一列中的每一行(欄)  -> deal with each pixel in all columns in specific row
                illumination[x, y] = np.exp(-(((x - x0)**2 + (y - y0)**2) / (2 * sigma**2)))
                illumination[x, y] = np.exp(-((x - x0) ** 2 + (y - y0) ** 2) / (2 * sigma ** 2))
                
        # Illuminate the image
        for x in range(nr) :
            for y in range(nc):
                for k in range(3): # 3 channels if we got color img
                    val = round (illumination[x,y] * f[x,y,k])
                    # got new pixel intensity corresponding to each channel
                    g[x,y,k] = np.uint8(val)
        return illumination,g

 
    
def cv2show(name : str, img ):
    cv2.imshow(name, img)
    cv2.waitKey(0)

def main() :
    img = cv2.imread('./1.jpg')
    nr,nc = img.shape[:2]
    print(nr,nc)
    # get center coordinate : (x0,y0) 為高斯分布的平均值 → 高斯分布中，分布最高的位置(=高斯分布的中心) → 打光的中心點(Center position in Illuminated area)
    x0 = nr // 2
    y0 = nc // 2
    # 標準差 : 光束能量分布的能力(多數(66%)光子分布情形) ; sigma 小，光束(分布)越集中
    sigma = 400
    IMF = Img_Format_Model()
    Illumination,Illuminated_img = IMF.image_format(img,x0,y0,sigma)
    # cv2show('Illu',Illuminated_img)
    print(Illuminated_img.shape)
    cv2show('Illu',Illumination)
    comp = np.hstack((img,Illuminated_img))
    cv2show('img vs Iillu img',comp)


if __name__ == '__main__':
    main()

     

        


