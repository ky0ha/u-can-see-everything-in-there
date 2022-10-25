import cv2 as cv
import numpy as np

src = cv.imread('C:\\Users\\25315\\Desktop\\2021 APMCM Problem A\\Annex 2\\Pic2_1.bmp')
img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow('origin', src)

result = src.copy()

circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,param1=300,param2=30,minRadius=0,maxRadius=15)
circles = np.uint16(np.around(circles))

def avg(ls):
    return int(round(sum(ls)/len(ls)))*2

pre = avg(circles[0,:][:,2])
print(pre)

image = cv.imread('C:\\Users\\25315\\Desktop\\2021 APMCM Problem A\\Annex 2\\Pic2_4.bmp')
result = image.copy()

kernel = np.ones((5, 5), np.float32)/25
image = cv.filter2D(image, -1, kernel)

imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret,  dst = cv.threshold(imgray, 110, 255, 0)
contours, hierarchy = cv.findContours(dst, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

bgr_list = [(0, 0, 255), (0, 255, 255), (0, 255, 0), (255, 255, 0), (255, 0, 0), (255, 0, 255)]

print(len(contours))
for i in contours[1:]:
    print(len(i))
    
total = 0
for index, value in enumerate(contours[1:]):
    perimeter = cv.arcLength(value, True)
    print(f'{perimeter/pre:.2f}')
    total += perimeter/pre
    cv.drawContours(result, [value], 0, bgr_list[index%6], 3)
print(f'{total:.2f}')
cv.imshow('image',result)
# cv.imwrite('C:\\Users\\25315\\Desktop\\2021 APMCM Problem A\\Annex 2\\result\\pic2_4.bmp', result)
cv.waitKey(0)