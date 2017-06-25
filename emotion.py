########### Python 2.7 #############
import httplib, urllib, base64
import json
from json import *

def emotion(imgUrl):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '5893c7d109784f3c88b53e92ed329678',
    }


    params = urllib.urlencode({
    })

    # Replace the example URL below with the URL of the image you want to analyze.
    body = "{ 'url': '%s' }" % imgUrl

    try:
        # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
        #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the
        #   URL below with "westcentralus".
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        #r = json.loads(data)
        #print(data)
        conn.close()
        r = json.loads(data)
        d =r[0]
        print d
        happiness = d["scores"]['happiness']
        neutral =  d["scores"]['neutral']
        print happiness, neutral
        if ( happiness > 0.4) or ( neutral > 0.4):
            ishappy = True
        else:
            ishappy = False
        print ishappy

        return ishappy, happiness, neutral
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

if __name__ == '__main__':

    imgUrl = 'http://221.193.242.133:5113/gaoshine/myface.jpg'
    ishappy,happiness, neutral = emotion(imgUrl)
    print ishappy, happiness, neutral








