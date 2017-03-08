import cv

#function for Smoothing
def MedianFilter(image):
    w = image.width
    h = image.height
    size = (w,h)
    iMFilter = cv.CreateImage(size,8,1)
    for i in range(h):
        for j in range(w):
            if i in [0,h-1] or j in [0,w-1]:
                iMFilter[i,j] = image[i,j]
            else:
                a= [0]*9
                for k in range(3):
                    for l in range(3):
                        a[k*3+l] = image[i-1+k,j-1+l]
                a.sort()
                iMFilter[i,j] = a[4]
    return iMFilter

#load image
image_name=raw_input('Please input the image name:')+'.jpg'
image = cv.LoadImage(image_name,0)
cv.ShowImage('Original',image)

#show aftersmoothing image
iMF = MedianFilter(image)
cv.ShowImage('AfterSmoothing',iMF)
cv.WaitKey(0)
