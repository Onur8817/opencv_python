import cv2
img = cv2.imread("picture/test.jpg")



#cv2.imwrite("deneme.jpg",img)


cv2.line(img,pt1=(10,10),pt2=(50,50),color=((12,54,140)),thickness=5)
cv2.imshow("Window",img)
"""
RGB()
R,g,b-> 0-255
"""

cv2.waitKey()


