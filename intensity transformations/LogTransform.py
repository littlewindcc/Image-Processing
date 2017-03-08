import scipy.misc
import numpy, math
from scipy.misc.pilutil import Image

#opening the image and converting it to grayscale
a = Image.open('intensity transform.jpg').convert('L')
a.save('input.jpg')

# a is converted to an ndarray
b = scipy.misc.fromimage(a)

# b is converted to type float
b1 = b.astype(float)

# maximum value in b1 is determined
b2 = numpy.max(b1)

# performing the log transformation
c = (255.0*numpy.log(1+b1))/numpy.log(1+b2)

# c is converted to type int
c1 = c.astype(int)

# c1 is converted from ndarray to Image
d = scipy.misc.toimage(c1)

#saving d as logtransform_output.png
d.save('output.jpg')
