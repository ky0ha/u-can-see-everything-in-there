import cv2 as cv
import numpy as np

# read the image by local path
image = cv.imread('C:\\Users\\25315\\Desktop\\2021 APMCM Problem A\\Annex 1\\Pic1_1.bmp')
# make a copy and store it in the variable 'result' to show the final result
result = image.copy()
# define an operator which be filled by 1 and shape is (5,5)
kernel = np.ones((5, 5), np.float32)/10
# use the operator processing pictures by 2-d convolution
image = cv.filter2D(image, -1, kernel)
# change the image to grayscale image
imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# binarize the picture
ret,  dst = cv.threshold(imgray, 110, 255, 0)
# find contours in binary image
contours, hierarchy = cv.findContours(dst, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

print(len(contours))

bgr_list = [(0, 0, 255), (0, 255, 255), (0, 255, 0), (255, 255, 0), (255, 0, 0), (255, 0, 255)]

for index, value in enumerate(contours[1:]):
    perimeter = cv.arcLength(value, True)
    print(f'{len(value)}, {perimeter:.4f}')
    cv.drawContours(result, [value], 0, bgr_list[index%6], 3)

cv.imshow('image',result)
# cv.imwrite('C:\\Users\\25315\\Desktop\\2021 APMCM Problem A\\Annex 1\\result\\pic1_1.bmp', result)
cv.waitKey(0)

