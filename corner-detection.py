import cv2
import numpy as np

def nothing(x):
    pass
cv2.namedWindow('trackbars')
cv2.createTrackbar('quality','trackbars',1,100,nothing)
cv2.createTrackbar('maxCorners','trackbars',0,500,nothing)

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    quality = cv2.getTrackbarPos('quality','trackbars')
    maxCorners = cv2.getTrackbarPos('maxCorners','trackbars')
    # quality = 25; maxCorners = 106
    if quality > 0:
        quality = quality/100
    else :
        quality=0.01

        
    corners = cv2.goodFeaturesToTrack(gray,maxCorners,quality,10)
    
    if corners is not None:
        corners = np.int0(corners)

    for corner in corners:
        
        x,y = corner.ravel()
        cv2.circle(frame,(x,y),5,(0,0,255),-1)
        
    cv2.imshow("frame",frame)

    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break 

cap.release()
cv2.destroyAllWindows()
