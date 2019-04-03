import cv2

img = cv2.imread('Penguins.jpg', 1)
img2 = cv2.imread('Penguins.jpg', 0)

# prints img in array form (~BGR)
print(img)
print(img2)

cv2.imshow("Penguin color", img)
cv2.imshow("Penguin b/w", img2)

# wait for ... sec
# cv2.waitKey(0)    # infinity
cv2.waitKey(10000)   # 10 sec

cv2.destroyAllWindows()
