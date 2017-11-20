import numpy as np
import cv2
cap = cv2.VideoCapture('forward_6sec.mp4')
cap_rev = cv2.VideoCapture('reverse_6sec.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
fgbg.setShadowValue(0)
kernel5 = np.ones((5,5), np.uint8)
kernel7 = np.ones((7,7), np.uint8)
kernel3 = np.ones((3,3), np.uint8)
i=1
while(1):
    ret, frame = cap.read()
    ret, frame_rev = cap_rev.read()
    fgmask = fgbg.apply(frame)
    fgmask_rev = fgbg.apply(frame_rev)
    if i==182:
        break;
    elif i<=9:
        vid_erode = cv2.erode(fgmask, kernel3, iterations=1)
        vid_dilate = cv2.dilate(vid_erode, kernel3, iterations=1)
        vid_erode_rev = cv2.erode(fgmask_rev, kernel7, iterations=1)
        vid_dilate_rev = cv2.dilate(vid_erode_rev, kernel7, iterations=1)
        #cv2.imshow('frame',fgmask)
        #vid_dilate = cv2.dilate(fgmask, kernel3, iterations=1)
        #vid_dilate_rev = cv2.dilate(fgmask_rev, kernel7, iterations=1)
        cv2.imwrite('forward/f'+str(i)+'.bmp',vid_dilate);
        cv2.imwrite('reverse/r'+str(182-i)+'.bmp',vid_dilate_rev);
        cv2.imshow('Eroded and dilated',vid_dilate)
        cv2.imshow('Eroded and dilated reverse',vid_dilate_rev)
    elif i>=172:
        vid_erode = cv2.erode(fgmask, kernel7, iterations=1)
        vid_dilate = cv2.dilate(vid_erode, kernel7, iterations=1)
        vid_erode_rev = cv2.erode(fgmask_rev, kernel3, iterations=1)
        vid_dilate_rev = cv2.dilate(vid_erode_rev, kernel3, iterations=1)
        #cv2.imshow('frame',fgmask)
        #vid_dilate = cv2.dilate(fgmask, kernel7, iterations=1)
        #vid_dilate_rev = cv2.dilate(fgmask_rev, kernel3, iterations=1)
        cv2.imwrite('forward/f'+str(i)+'.bmp',vid_dilate);
        cv2.imwrite('reverse/r'+str(182-i)+'.bmp',vid_dilate_rev);
        cv2.imshow('Eroded and dilated',vid_dilate)
        cv2.imshow('Eroded and dilated reverse',vid_dilate_rev)
    else:
        vid_erode = cv2.erode(fgmask, kernel5, iterations=1)
        vid_dilate = cv2.dilate(vid_erode, kernel5, iterations=1)
        vid_erode_rev = cv2.erode(fgmask_rev, kernel5, iterations=1)
        vid_dilate_rev = cv2.dilate(vid_erode_rev, kernel5, iterations=1)
        #cv2.imshow('frame',fgmask)
        #vid_dilate = cv2.dilate(fgmask, kernel5, iterations=1)
        #vid_dilate_rev = cv2.dilate(fgmask_rev, kernel5, iterations=1)
        cv2.imwrite('forward/f'+str(i)+'.bmp',vid_dilate);
        cv2.imwrite('reverse/r'+str(182-i)+'.bmp',vid_dilate_rev);
        cv2.imshow('Eroded and dilated',vid_dilate)
        cv2.imshow('Eroded and dilated reverse',vid_dilate_rev)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    i+=1
cap.release()
cv2.destroyAllWindows()
i=1
while i<=181:
    img_f = cv2.imread('forward/f'+str(i)+'.bmp')
    img_r = cv2.imread('reverse/r'+str(i)+'.bmp')
    img_final = cv2.bitwise_or(img_f,img_r)
    #img_final_eroded = cv2.erode(img_final,kernel7,iterations=1)
    cv2.imwrite('Final/fin'+str(i)+'.bmp',img_final)
    i+=1
