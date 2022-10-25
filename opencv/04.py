import cv2
import numpy as np
img=cv2.imread('C:\\Users\\25315\\Desktop\\2021 APMCM Problem A\\Annex 1\\Pic1_1.bmp',cv2.IMREAD_UNCHANGED)
img2=cv2.cvtColor(img,cv2.COLOR_RGBA2BGR)
gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy=cv2.findContours(gray,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
middle=img2.copy()
result=cv2.drawContours(middle,contours,-1,(0,0,255),3)
 
cv2.imshow("original",img)
cv2.imshow("resuly",result)
 
cv2.waitKey()
cv2.destroyAllWindows()
