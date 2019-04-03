import cv2

# face_data  = cv2.CascadeClassifier("C:/umesh/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
face_data  = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
print(face_data)
cap = cv2.VideoCapture(0)

while cap.isOpened():
	status, frame = cap.read()
	faces = face_data.detectMultiScale(frame, 1.5, 5)
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
		print(frame)
	cv2.imshow('hh', frame)
	if cv2.waitKey(2) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
