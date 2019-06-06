import numpy as np
import cv2

img = cv2.imread("square.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,100,0.01,10)
corners = np.float32(corners)
print(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),5,(0,0,255),-1)
    
cv2.imshow('img',img)
#cv2.imshow('gray',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
