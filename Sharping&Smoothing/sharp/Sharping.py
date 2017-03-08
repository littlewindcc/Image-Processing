import cv
import cv2

#function for LaplacianSharp
def LFilter(image,array):
    w = image.width
    h = image.height
    size = (w,h)
    iFilter = cv.CreateImage(size,8,1)
    for i in range(h):
        for j in range(w):
            if i in [0,h-1] or j in [0,w-1]:
                iFilter[i,j] = image[i,j]
            else:
                a= [0]*9
                for k in range(3):
                    for l in range(3):
                        a[k*3+l] = image[i-1+k,j-1+l]
                sum = 0
                for m in range(9):
                    sum = sum+array[m]*a[m]
                iFilter[i,j] = int(sum)
    return iFilter



#load image
image = cv.LoadImage('sharp.jpg',0)
cv.ShowImage('Original',image)
#show aftersharping image
H1 = [-1,-1,-1,-1,9,-1,-1,-1,-1]
iH1F = LFilter(image,H1)
cv.ShowImage('AfterSharp',iH1F)
cv.WaitKey(0)

