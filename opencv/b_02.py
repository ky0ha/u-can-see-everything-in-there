import cv2 as cv
import numpy as np
# path = '/home/lyone/Mine/code/apmcm'
# image= cv.imread(os.path.join(path,'Annex1/Pic1_1.bmp'),0)
image = cv.imread('C:\\Users\\25315\\Desktop\\2021 APMCM Problem A\\Annex 2\\Pic2_4.bmp')
result = image.copy()
# kernel = np.array([[0, -1, 0],[-1, 5, -1], [0, -1, 0]], dtype=np.float32)
# image = cv.filter2D(image, cv.CV_32F, kernel)
# image = cv.convertScaleAbs(image)
kernel = np.ones((5, 5), np.float32)/25
image = cv.filter2D(image, -1, kernel)
# image = cv.GaussianBlur(image, (3, 3), 0)
# image = cv.medianBlur(image, 5)

imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret,  dst = cv.threshold(imgray, 110, 255, 0)
contours, hierarchy = cv.findContours(dst, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

# cv.drawContours(image, contours, 1, (0, 255, 0), 3)

# half_length = int(len(contours)/2)

bgr_list = [(0, 0, 255), (0, 255, 255), (0, 255, 0), (255, 255, 0), (255, 0, 0), (255, 0, 255)]
print(len(contours))
for i in contours[1:]:
    print(len(i))
total = 0
for index, value in enumerate(contours[1:]):
    # cnt = contours[index]
    # cv.drawContours(image, [cnt], 0, (0, 255, 0), 3)
    perimeter = cv.arcLength(value, True)
    print(f'{perimeter/14:.2f}')
    total += perimeter/14
    cv.drawContours(result, [value], 0, bgr_list[index%6], 3)
print(f'{total:.2f}')
cv.imshow('image',result)
cv.imwrite('C:\\Users\\25315\\Desktop\\2021 APMCM Problem A\\Annex 2\\result\\pic2_4.bmp', result)
cv.waitKey(0)

