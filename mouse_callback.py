import cv2
import matplotlib.pyplot as plt

img = cv2.imread("garden.jpg",1)
plt.xticks([1,2,3], ['Blue','Green','Red'])
i=0

def getcolor(event, x,y, flags, param):
	global img, i
	if event == cv2.EVENT_MOUSEMOVE:
		plt.plot([1,2,3], img[y,x])
#		plt.bar([1,2,3], img[y,x], color=['blue', 'green', 'red'])
		i=i+1
		plt.savefig('plot'+str(i) +'.png')
#		plot = cv2.imread('plot'+str(i) +'.png',1)		
#		cv2.imshow('plot', plot)
#		plt.show()
		print(y,x , img[y,x])

cv2.namedWindow('image')
cv2.setMouseCallback('image', getcolor)

cv2.imshow('image', img)
cv2.waitKey(1000)

cv2.destroyAllWindows()
print(i)