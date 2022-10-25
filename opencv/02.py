import cv2
import numpy as np

src = cv2.imread('C:\\Users\\25315\\Desktop\\2021 APMCM Problem A\\Annex 1\\Pic1_1.bmp')
img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(img, 60, 250)
line = cv2.HoughLinesP(edge, 1, np.pi/180, 100, minLineLength=80, maxLineGap=20)
for l in line:
    print(l)
    x1, y1, x2, y2 = l[0]
    cv2.line(src, (x1, y1), (x2, y2), (255, 0, 0), 1)
cv2.imshow('line', src)
cv2.waitKey(0)
cv2.destroyAllWindows()