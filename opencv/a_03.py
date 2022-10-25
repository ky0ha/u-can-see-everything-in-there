import cv2 as cv
import numpy as np
import csv

image = cv.imread('C:\\Users\\25315\\Desktop\\2021 APMCM Problem A\\Annex 1\\Pic1_2.bmp')
result = image.copy()
cv.imshow('image',image)
kernel = np.ones((5, 5), np.float32)/10
image = cv.filter2D(image, -1, kernel)
cv.imshow('image_filter2d',image)
imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('image_gray',imgray)
ret,  dst = cv.threshold(imgray, 110, 255, 0)
cv.imshow('image_binary',dst)
contours, hierarchy = cv.findContours(dst, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

print(len(contours))

bgr_list = [(0, 0, 255), (0, 255, 255), (0, 255, 0), (255, 255, 0), (255, 0, 0), (255, 0, 255)]


contours = [i for i in contours]
dealed = {}
perimeters = []
for i in contours:
    perimeters.append(cv.arcLength(i, True))
print(perimeters)
for key, contour in enumerate(contours):
    rep = 0
    for index, value in enumerate(contour):
        if value[0][0]==0 or value[0][0]==1295 or value[0][1]==971 or value[0][1]==0:
            contour = np.delete(contour, index-rep, 0)
            rep += 1
            dealed[str(key)] = dealed.setdefault(str(key), 0) + 1
        dealed[str(key)] = dealed.setdefault(str(key), 0)
    contours[key] = contour
# for index, value in enumerate(contours):
#     perimeter = cv.arcLength(value, True)
#     print(f'{len(value)}, {perimeter:.4f}')
#     cv.drawContours(result, [value], 0, bgr_list[index%6], 3)

total = 0
for index, contour in enumerate(contours):
    with open(f'C:\\Users\\25315\\Desktop\\pic1_2\\{index+1}.csv', 'w', encoding='utf-8', newline='') as f:
        # perimeter = cv.arcLength(contour, True)
        perimeter = perimeters[index]
        print(f'{len(contour)}, {perimeter-dealed[str(index)]:.4f}')
        total += perimeter-dealed[str(index)]
        for j in contour:
            cv.circle(result, (j[0][0], j[0][1]), 2, bgr_list[index], -1)
            w = csv.writer(f)
            w.writerow([j[0][0], j[0][1]])
print(dealed)
print(f'{total:.4f}')

cv.imshow('image_result',result)
# cv.imwrite('C:\\Users\\25315\\Desktop\\2021 APMCM Problem A\\Annex 1\\result\\pic1_2.bmp', result)
cv.waitKey(0)

