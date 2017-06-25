# -*- coding: utf-8 -*-

import cv2
import numpy as np
import urllib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from time import gmtime, strftime
import threading
from facetest import faceron
from emotion import emotion
from myocr import getocr
import graphApi

import time
import urllib
import urllib2

BASE_URL = 'http://192.168.2.111'

def readmail(mail_txt):
    try:
        data = mail_txt
        url = BASE_URL
        geturl = url + '/mail/' + data
        print geturl
        request = urllib2.Request(geturl)
        response = urllib2.urlopen(request)
        r = response.read()
        print r
        return r
    except Exception, ex:
        print 'error', ':', ex

def login(yourname):
    try:
        data = yourname
        url = BASE_URL
        geturl = url + '/login/' + data
        print geturl
        request = urllib2.Request(geturl)
        response = urllib2.urlopen(request)
        r = response.read()
        print r
        return r
    except Exception, ex:
        print 'error', ':', ex

def wx():
    try:

        url = BASE_URL
        geturl = url + '/gpio/0'
        print geturl
        request = urllib2.Request(geturl)
        response = urllib2.urlopen(request)
        r = response.read()
        print r
        return r
    except Exception, ex:
        print 'error', ':', ex

def ocr(txt):
    try:

        url = BASE_URL
        geturl = url + '/ocr/'+txt+'\000\000\000\000\000\000\000\000\000'
        print geturl
        request = urllib2.Request(geturl)
        response = urllib2.urlopen(request)
        r = response.read()
        print r
        return r
    except Exception, ex:
        print 'error', ':', ex


def home():
    try:
        url = BASE_URL
        geturl = url + '/gpio/0'
        print geturl
        request = urllib2.Request(geturl)
        response = urllib2.urlopen(request)
        r = response.read()
        print r
        return r
    except Exception, ex:
        print 'error', ':', ex


def uploadimg(myFile):
    register_openers()
    f = open(myFile, "rb")

    datagen, headers = multipart_encode({"myFile": f})
    # 创建请求对象
    request = urllib2.Request("http://221.193.242.133:5113/lh0.php", datagen, headers)

    try:
        response = urllib2.urlopen(request, timeout=4)
        r = response.read()
        print r
    except:
        return False


def runface():
    global personname
    global happys
    global status
    #人脸检测学习经验数据集 (haar分类)
    cascPath = 'haarcascade_frontalface_alt2.xml'
    faceCascade = cv2.CascadeClassifier(cascPath)

    video_capture = cv2.VideoCapture(0)

    while True:
        # 一帧一帧的采集视频
        ret, frame = video_capture.read()
        imgsize = frame.shape
        frame = cv2.resize(frame,(int(imgsize[1]/1.2), int(imgsize[0]/1.2)))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #人脸检测,
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        # 在脸部画方块
        icount = 0

        ishat = 'person'


        for (x, y, w, h) in faces:
            y0 = abs(y-int(h/2))
            myimg = frame[y:(y+h),x:(x+w)]
            headimg0 = frame[y:(y+h)*1.2,x:(x+w)]
            headimg = headimg0.copy()
            cv2.rectangle(frame, (x-5,y-5), (x+w+5, y+h+5), (0, 255, 0), 2)
            icount = icount + 1
            print w*h



        #把日期和人数写成字幕
        s = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        s = s + ' Person:%s   emotion:%s' % (personname, happys)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,s,(10,30), font, 1,(255,255,255),2)


        # 显示视频
        cv2.imshow('Video', frame)


        if cv2.waitKey(1) & 0xFF == ord('s'):

            cv2.imwrite('myface.jpg', headimg)
            print 'Save img!',s

            t = threading.Thread(target=facecognitive, args=())
            t.start()

        if cv2.waitKey(1) & 0xFF == ord('t'):
            print frame.shape
            cv2.imwrite('mytxt.jpg',frame[50:600,1:1000] )
            print 'Save txt!',s
            t = threading.Thread(target=ocrcognitive, args=())
            t.start()

        if cv2.waitKey(1) & 0xFF == ord('e'):

            print 'Email txt!',s
            t = threading.Thread(target=demo, args=())
            t.start()


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 完成后,释放资源
    video_capture.release()
    cv2.destroyAllWindows()

def ocrcognitive():
    r = getocr()
    ocr(r)



def facecognitive():
    global personname
    global happys

    print 'face upload...'
    uploadimg('myface.jpg')
    print 'face cognitive...'
    img_url = 'http://221.193.242.133:5113/gaoshine/myface.jpg'
    r = faceron(img_url)
    print r['isIdentical'],r['confidence']
    if r['confidence']> 0.6:
        personname ='GaoSheng'
        login('gaoshine')
    else:
        personname ="Who?"

    ishappy,happiness, neutral = emotion(img_url)
    print ishappy, happiness, neutral
    if  happiness > 0.4:
        happys = 'happiness'
        wx()
    else:
        happys = 'neutral'

def demo():
    time.sleep(1)
    #r = graphApi.get_mail()
    #print type(r[0])
    readmail('Hello,I am in BeiJing AI Hackathon!')

    time.sleep(5)
    login('gaoshine')
    time.sleep(5)
    home()


if __name__ == '__main__':
    personname ="Who?"
    happys = 'unkown?'
    #runface()
    #uploadimg('myface.jpg')
    demo()
