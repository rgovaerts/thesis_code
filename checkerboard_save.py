import SimpleITK as sitk
from pylab import *
import Image
import sys

image1 = sitk.ReadImage(sys.argv[1])
image2 = sitk.ReadImage(sys.argv[2])
checker = sitk.CheckerBoardImageFilter()
checker.SetCheckerPattern(5)
res = checker.Execute(image1, image2)

Image.fromarray(sitk.GetArrayFromImage(res)).save(sys.argv[3])
