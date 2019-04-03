import cv2
import numpy as np

img = cv2.imread('perspective_image.png',1)

# pts1 = np.float32([[56,65],[168,52],[28,187],[189,190]])
# pts2 = np.float32([[0,0],[150,0],[0,150],[150,150]])
# M = cv2.getPerspectiveTransform(pts1,pts2)
# dst = cv2.warpPerspective(img,M,(150,150))
pts1 = np.float32([[28,32],[182,26],[15,190],[193,191]])
pts2 = np.float32([[0,0],[150,0],[0,150],[150,150]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(150,150))


cv2.imshow("img",dst)
cv2.waitKey(10000)
cv2.destroyAllWindows()
