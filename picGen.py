# -*- coding: utf-8 -*-
'''
把图片变成C++的头文件中的数组
'''
import numpy as np
import cv2
W = 64
H = 64
img = cv2.imread('smell.png',0)
img = cv2.resize(img,(W, H))
ret, img0 = cv2.threshold(img,205,255,cv2.THRESH_BINARY)
r = cv2.imshow('img0',img0)
cv2.imwrite('out.bmp',img0)
a = np.zeros((W, H))
a = img0
a = a.reshape(W*H)
print a.shape
ss = 'const char out[] PROGMEM = {\n'
for i in xrange(0, W*H, 8):
    if a[i+7] > 0:
        a[i+7] = 128
    if a[i+6] > 0:
        a[i+6] = 64
    if a[i+5] > 0:
        a[i+5] = 32
    if a[i+4] > 0:
        a[i+4] = 16
    if a[i+3] > 0:
        a[i+3] = 8
    if a[i+2] > 0:
        a[i+2] = 4
    if a[i+1] > 0:
        a[i+1] = 2
    if a[i] > 0:
        a[i] = 1
    s = a[i] + a[i+1] + a[i+2] + a[i+3] + a[i+4] + a[i+5] + a[i+6] + a[i+7]
    r = hex(s).upper()
    ss = ss + str(r) + ','
    if i % 8 == 0:
        #ss = ss + '\n'
        pass
    #print r
ss = ss + '\n};'
print ss
cv2.waitKey(0)

