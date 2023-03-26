import cv2

video = cv2.VideoCapture("picture/insan.mp4")
face_cascade= cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml")

while video.isOpened():
    test,frame=video.read()
    face = face_cascade.detectMultiScale(frame)
    for (x,y,w,h) in face:
        cv2.rectangle(frame,pt1=(x,y),pt2=((x+w),(y+h)),color=(255,0,0),thickness=4)
    cv2.circle(frame,center=(100,100),radius=50,thickness=5,color=(255,0,0))
    cv2.imshow("Test",frame)
    if cv2.waitKey() == ord("q"):
        break


video.release()
cv2.destroyAllWindows()
