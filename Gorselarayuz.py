import cv2
from matplotlib import pyplot

img = cv2.imread("picture/test.jpg")
cv2.line(img,pt1=(10,10),pt2=(50,50),color=((12,54,140)),thickness=5)

cv2.rectangle(img,pt1=(100,50),pt2=(300,200),thickness=5,color=(255,0,0))

cv2.circle(img,center=(471,524),radius=(50),color=(0,255,0),thickness=5)



pyplot.imshow(img)
pyplot.show()