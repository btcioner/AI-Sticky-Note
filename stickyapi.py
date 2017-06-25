# -*- coding: utf-8 -*-
import urllib
import urllib2
import time

BASE_URL = 'http://192.168.2.111/'


def readmail(mail_txt):
    try:
        data = urllib.urlencode(mail_txt)
        url = BASE_URL
        geturl = url + '/gpio/1' + data
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

if __name__ == '__main__':
    readmail('')
    time.sleep(5)
    login('gaoshine')
    time.sleep(5)
    home()


