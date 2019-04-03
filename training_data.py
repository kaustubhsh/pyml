import cv2
import os
import numpy as np

face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

dir_name = 'dataset_image'

face_name = os.listdir(dir_name)

face_datax = []
label = []

c=0
for i in face_name:
	image_path = 'dataset_image/' + i
	face_values = cv2.imread(image_path, 0)
	print (face_values)
	faces = face_data.detectMultiScale(face_values, 1.5, 5)

	for (x,y,w,h) in faces:
		face_datax.append(face_values[y:y+h, x:x+w])
		label.append(c)
		
np.save('training_faces', face_datax)
np.save('training_label', label)

