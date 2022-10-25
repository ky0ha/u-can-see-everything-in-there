import cv2 as cv
import numpy as np

image = cv.imread('C:\\Users\\25315\\Desktop\\2021 APMCM Problem A\\Annex 1\\Pic1_2.bmp')
result = image.copy()
kernel = np.ones((5, 5), np.float32)/10
image = cv.filter2D(image, -1, kernel)

imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret,  dst = cv.threshold(imgray, 110, 255, 0)
contours, hierarchy = cv.findContours(dst, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

print(len(contours))

bgr_list = [(0, 0, 255), (0, 255, 255), (0, 255, 0), (255, 255, 0), (255, 0, 0), (255, 0, 255)]

for index, value in enumerate(contours):
    perimeter = cv.arcLength(value, True)
    print(f'{len(value)}, {perimeter:.4f}')
    cv.drawContours(result, [value], 0, bgr_list[index%6], 3)

cv.imshow('image',result)
# cv.imwrite('C:\\Users\\25315\\Desktop\\2021 APMCM Problem A\\Annex 1\\result\\pic1_2.bmp', result)
cv.waitKey(0)

