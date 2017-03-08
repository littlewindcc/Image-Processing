import cv2
from numpy import *

def SaltAndPepper(src,percetage):
    NoiseImg=src
    NoiseNum=int(percetage*src.shape[0]*src.shape[1])
    for i in range(NoiseNum):
        randX=random.random_integers(0,src.shape[0]-1)
        randY=random.random_integers(0,src.shape[1]-1)
        if random.random_integers(0,1)==0:
            NoiseImg[randX,randY]=0
        else:
            NoiseImg[randX,randY]=255
    return NoiseImg


img=cv2.imread('original image.jpg',flags=0)

# add SaltAndPepp
# add 10%,30%,50% SaltAndPepper respectively
Pers=[0.1,0.3,0.5]
for i in Pers:
    NoiseImg=SaltAndPepper(img,i)
    fileName='SaltPepper'+str(i)+'.jpg'
    cv2.imwrite(fileName,NoiseImg,[cv2.IMWRITE_JPEG_QUALITY,100])
    cv2.imshow('AfterNoise',NoiseImg)
    cv2.waitKey(0)
