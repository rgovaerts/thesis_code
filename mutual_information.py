import numpy
import Image
import sys

def mutual_information(i1, i2, bins=256):
    i1 = numpy.asarray(i1)
    i2 = numpy.asarray(i2)
    
    # validate function arguments
    if not i1.shape == i2.shape:
        raise Exception('the two supplied array-like sequences i1 and i2 must be of the same shape')
    
    # compute i1 and i2 histogram range
    i1_range = __range(i1, bins)
    i2_range = __range(i2, bins)
    
    # compute joined and separated normed histograms
    i1i2_hist, _, _ = numpy.histogram2d(i1.flatten(), i2.flatten(), bins=bins, range=[i1_range, i2_range]) # Note: histogram2d does not flatten array on its own
    i1_hist, _ = numpy.histogram(i1, bins=bins, range=i1_range)
    i2_hist, _ = numpy.histogram(i2, bins=bins, range=i2_range)
    
    # compute joined and separated entropy
    i1i2_entropy = __entropy(i1i2_hist)
    i1_entropy = __entropy(i1_hist)
    i2_entropy = __entropy(i2_hist)
    
    # compute and return the mutual information distance
    return i1_entropy + i2_entropy - i1i2_entropy

def __range(a, bins):
    '''Compute the histogram range of the values in the array a according to
    scipy.stats.histogram.'''
    a = numpy.asarray(a)
    a_max = a.max()
    a_min = a.min()
    s = 0.5 * (a_max - a_min) / float(bins - 1)
    return (a_min - s, a_max + s)
 
def __entropy(data):
    '''Compute entropy of the flattened data set (e.g. a density distribution).'''
    # normalize and convert to float
    data = data/float(numpy.sum(data))
    # for each grey-value g with a probability p(g) = 0, the entropy is defined as 0, therefore we remove these values and also flatten the histogram
    data = data[numpy.nonzero(data)]
    # compute entropy
    return -1. * numpy.sum(data * numpy.log2(data))
    
if __name__ == "__main__":
	img1 = Image.open(sys.argv[1])
	img2 = Image.open(sys.argv[2])
	#f1=open('MI.txt', 'w+')
	#print >>f1, mutual_information(img1, img2)
	print mutual_information(img1, img2)
