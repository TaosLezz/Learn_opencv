import cv2
import numpy as np

path = r'E:\aHieu\pictures\test_elon.jpg'


img = cv2.imread(path)

blank = np.zeros((img.shape[:2]), dtype='uint8')
mask = cv2.circle(blank, (img.shape[0]//2, img.shape[1]//2), 100, (255,0,255), -1)

masked = cv2.bitwise_and(img, img, mask=mask)
blur = cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
flip = cv2.flip(img,1)
cv2.imshow('k', masked)
cv2.imshow('img', img)
# # cv2.imshow('blur', blur)
# # cv2.imshow('flip', flip)
# cv2.imshow('rgb', rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

