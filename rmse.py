import numpy
import Image
import sys
from sklearn.metrics import mean_squared_error
from math import sqrt

# code
def rmse(i1, i2):
    
    # pre-process function arguments
    i1 = numpy.asarray(i1)
    i2 = numpy.asarray(i2)
    
    # validate function arguments
    if not i1.shape == i2.shape:
        raise Exception('the two supplied array-like sequences i1 and i2 must be of the same shape')
    
    # compute and return the RMSE
    return sqrt(mean_squared_error(i1, i2))
    
if __name__ == "__main__":
	img1 = Image.open(sys.argv[1])
	img2 = Image.open(sys.argv[2])
	print rmse(img1, img2)
