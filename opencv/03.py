import cv2
import numpy as np

# img = cv2.imread('C:\\Users\\25315\\Desktop\\Pic1_3.bmp', 0)
src = cv2.imread('C:\\Users\\25315\\Desktop\\2021 APMCM Problem A\\Annex 2\\Pic2_1.bmp')
# kernelx = np.array([[0, -1, 0],[-1, 5, -1], [0, -1, 0]], dtype=np.float32)
# img = cv2.filter2D(src, cv2.CV_32F, kernelx)
# img = cv2.convertScaleAbs(img)
# kernel = np.ones((5, 5), np.float32)/10
# img = cv2.filter2D(img, -1, kernel)

# img = cv2.fastNlMeansDenoisingColored(src,None,60,10,7,21)
img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# img = cv2.GaussianBlur(img, (3, 3), 0)


# img = cv2.Canny(img, 50, 300, L2gradient=True)
cv2.imshow('img', img)

result = src.copy()
# lsd = cv2.createLineSegmentDetector(1)
# dlines = lsd.detect(img)
# dlines = cv2.HoughLinesP(img, 1, np.pi/180, 100, minLineLength=100, maxLineGap=5)
# for dline in dlines[0]:
#     x0 = int(round(dline[0][0]))
#     y0 = int(round(dline[0][1]))
#     x1 = int(round(dline[0][2]))
#     y1 = int(round(dline[0][3]))
#     cv2.line(result, (x0, y0), (x1, y1), (0, 255, 0), 1, cv2.LINE_AA)
# for line in dlines:
#     print(line)
#     x1,y1,x2,y2 = line[0]
#     cv2.line(result,(x1,y1),(x2,y2),(0,255,0),2)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=300,param2=30,minRadius=0,maxRadius=15)
circles = np.uint16(np.around(circles))
print(circles.shape)
print(circles[0,:])
def avg(ls):
    return int(round(sum(ls)/len(ls)))
print(circles[0,:][:,2])
print(avg(circles[0,:][:,2]))
# for i in circles[0,:]:
#     # 绘制外圆
#     cv2.circle(result,(i[0],i[1]),i[2],(0,0,255),2)
#     # 绘制圆心
#     cv2.circle(result,(i[0],i[1]),1,(0,255,0),3)

# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.applyColorMap(img, cv2.COLORMAP_AUTUMN)
# cv2.imshow('img1', result)

# cv2.waitKey(0)
# cv2.destroyAllWindows()