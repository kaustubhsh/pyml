import cv2
cap = cv2.VideoCapture("http://192.168.0.101:8080/video")

while cap.isOpened():
    status, frame = cap.read()
    cv2.imshow("frame", frame)
    cv2.imwrite("frame.jpg",frame)
    if cv2.waitKey(27) &  0xff ==  ord('q') :
        break
    
cv2.destroyAllWindows()
cap.release()
