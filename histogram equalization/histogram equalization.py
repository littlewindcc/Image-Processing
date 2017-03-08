from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


#this function is for histogram equalization
def histeq(image_array,image_bins=256):



    image_array2,bins = np.histogram(image_array.flatten(),image_bins)
    #print image_array2,bins
    # Calculate the cumulative histogram function
    cdf = image_array2.cumsum()

    # The cumulative function was transformed into the interval [ 0,255 ]
    cdf = (255.0/cdf[-1])*cdf

    # Original image matrix using integrated conversion function , interpolation process
    image2_array = np.interp(image_array.flatten(),bins[:-1],cdf)


    # Returns the image matrix leveled and cumulative function
    return image2_array.reshape(image_array.shape),cdf


#open the image and convert it to grayscale
image = Image.open("image.jpg").convert("L")

#Object into an image matrix
image_array = np.array(image)

#print grayscale image and its histogram
plt.subplot(2,2,1)
plt.imshow(image,cmap=cm.gray)
plt.axis("off")
plt.subplot(2,2,2)
plt.hist(image_array.flatten(),256) #flatten:Matrix can be converted into one-dimensional sequence

a = histeq(image_array)  # histogram equalization
plt.subplot(2,2,3)
plt.hist(a[0].flatten(),256)
plt.subplot(2,2,4)
plt.imshow(Image.fromarray(a[0]),cmap=cm.gray)
plt.axis("off")

plt.show()
