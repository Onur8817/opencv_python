import cv2
from matplotlib import pyplot
img = cv2.imread("picture/insan4.jpg")

face_cascade= cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml")
face = face_cascade.detectMultiScale(img)

for (x,y,w,h) in face:
    print(x,y,w,h)
    cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=(255,0,0),thickness=4)

pyplot.imshow(img)
pyplot.show()
cv2.waitKey()
