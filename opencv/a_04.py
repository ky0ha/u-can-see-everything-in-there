import csv
import cv2 as cv
import numpy as np

image = cv.imread('C:\\Users\\25315\\Desktop\\2021 APMCM Problem A\\Annex 1\\Pic1_1.bmp')
result = image.copy()
kernel = np.ones((5, 5), np.float32)/10
image = cv.filter2D(image, -1, kernel)

imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret,  dst = cv.threshold(imgray, 110, 255, 0)
contours, hierarchy = cv.findContours(dst, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for index, matrix in enumerate(contours[1:]):
    with open(f'C:\\Users\\25315\\Desktop\\pic1_1\\{index+1}.csv', 'w', encoding='utf-8', newline='') as f:
        for vector in matrix:
            w = csv.writer(f)
            w.writerow(vector[0])