import cv2
img = cv2.imread("picture/a.jpg")

nesne_cascade = cv2.CascadeClassifier("Cascades/myhaar.xml")

nesne = nesne_cascade.detectMultiScale(img)

for (x,y,w,h) in nesne:
    cv2.rectangle(img,pt1=(x,y),pt2=((x+w),(y+h)),color=(255,0,0))

cv2.imshow("window", img)
cv2.waitKey()

