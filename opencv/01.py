import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\25315\\Desktop\\2021 APMCM Problem A\\Annex 1\\Pic1_1.bmp', 0)
# dst = cv.fastNlMeansDenoisingColored(img,None,100,10,7,21)
kernel = np.ones((5, 5), np.float32)/10
dst = cv.filter2D(img, -1, kernel)
# dst = cv.GaussianBlur(img, (5, 5), 0)
canny = cv.Canny(dst, 50, 300)
# cv.namedWindow('image', 1)


# dst = cv.filter2D(canny, -1, kernel)

cv.imshow('image1', canny)
cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()