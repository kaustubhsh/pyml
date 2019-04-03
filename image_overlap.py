import cv2
import matplotlib.pyplot as plt
# reading the image
penguin = cv2.imread('Penguins.jpg', 1)
messi = cv2.imread('messi.jpg', 1)
land_big = cv2.imread('land_big.jpg', 1)


# prints img in array form (~BGR)
# print(penguin)
# print(messi)


# resizing the image
# land_small = cv2.resize(land_big, None, fx=.1, fy=.1, interpolation = cv2.INTER_AREA) # based on percentage
land_small = cv2.resize(land_big , (300,200))  # input rows and cols
penguin_small = cv2.resize(penguin, (300,200))
messi_small = cv2.resize(messi, (300,200))
messi_small_orig = messi_small.copy()
messi_small_edit = messi_small.copy()

# image blending of penguin and landscape
superimposed_img = cv2.addWeighted(penguin_small, 0.3, land_small, 0.7, 0)
# cv2.imshow("superimposed_img", superimposed_img)


# making duplicate balls in messi image
ball = messi_small[167:196, 176:209]
messi_small[167:196, 76:109] = ball
# cv2.imshow("Messi", messi_small)

# # making duplicate balls in messi image
# ball = messi_small[422:488, 443:514]
# messi_small[422:488, 243:314] = ball
# cv2.imshow("Messi", messi_small)

# placing line and figure on image
cv2.line(messi_small_edit, (0,150), (50,200), (233,45,100), 2)
cv2.rectangle(messi_small_edit, (176,167), (209, 196), (123,231,87), 2)

# placing the point on the image
# img[100,100] = [0,0,255]


#  print the image
# cv2.imshow("Penguin", penguin_small)
# cv2.imshow("land_small", land_small)
# cv2.imshow("land_big", land_big)

plt.subplot(231), plt.imshow(land_small), plt.title("land_small")
plt.subplot(232), plt.imshow(penguin_small), plt.title("penguin_small")
plt.subplot(233), plt.imshow(superimposed_img), plt.title("superimposed_img")
plt.subplot(234), plt.imshow(messi_small_orig), plt.title("messi_small_orig")
plt.subplot(235), plt.imshow(messi_small), plt.title("messi_small")
plt.subplot(236), plt.imshow(messi_small_edit), plt.title("messi_small_edit")



plt.show()
# plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
# plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
# plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
# plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
# plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
# plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
# plt.show()


# wait for ... sec
# cv2.waitKey(0)    # infinity
cv2.waitKey(5000)   # 5 sec

cv2.destroyAllWindows()
