import cv2
import os

face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)

dir_name = 'dataset_image'

try:
	os.mkdir(dir_name)
except:
	print("already created")

count=0
while cap.isOpened():
	status, frame = cap.read()
	gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_data.detectMultiScale(gray_img, 1.5, 5)

	for (x,y,w,h) in faces:
		count += 1
		print(count)
		cv2.imwrite(dir_name+'/images'+str(count)+'.jpg', gray_img)

	cv2.imshow('video', frame)
	if cv2.waitKey(2) & 0xFF == ord('q'):
		break
	if cv2.waitKey(50) & count == 50:
		break

cv2.destroyAllWindows()
cap.release()
