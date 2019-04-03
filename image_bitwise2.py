"""
This python program is used to implant a balloon image 
over the landscape image
Shows the procejure to extract the balloon from the background using threshold and bitwise method
and add to the landscape image

"""

import cv2

# opening the original files
land = cv2.imread('land_big.jpg', 1)
cv2.imshow("landscape", land)
balloon = cv2.imread('balloon.jpeg', 1)
cv2.imshow("balloon", balloon)

# getting the dimension of the balloon image
rows, cols, channel = balloon.shape
print(balloon.shape)

# frame where the balloon  will be placed
roi = land[75:75+rows, 350:350+cols]  # region of insertion
cv2.imshow("land", roi)

# convert image to gray
b_gray = cv2.cvtColor(balloon, cv2.COLOR_BGR2GRAY)
cv2.imshow("frame", b_gray)

# inverting the image (b->w // w->b)
b_gray = cv2.bitwise_not(b_gray)
cv2.imshow("frame2", b_gray)

# convert every balloon pixel to white 
# and background to black
ret, mask = cv2.threshold(b_gray, 40, 255, cv2.THRESH_BINARY)
cv2.imshow("frame3", mask)

# inverting the mask
mask_inv = cv2.bitwise_not(mask)
cv2.imshow("frame4", mask_inv)

# making the base for the balloon insertion
# makes the roi portion  where balloon is to be inserted to be black
# it will later help help when adding images
img_black = cv2.bitwise_and(roi, roi, mask=mask_inv)	
cv2.imshow("frame5", img_black)

# removing the background from balloon image 
# in this case blue to black
img_fg = cv2.bitwise_and(balloon, balloon, mask = mask)
cv2.imshow("frame6", img_fg)

# adding the balloon image (img_fg) to roi image (img_black)
# successful integrate at small scale
part = cv2.add(img_black, img_fg)
cv2.imshow("frame7", part)

# overwrite the part image to the original image 
# (superimpose)
land[75:75+rows, 350:350+cols] = part
cv2.imshow("frame8", land)


cv2.waitKey(10000)
cv2.destroyAllWindows()