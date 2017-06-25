'''
[{u'faceId': u'374a2eb1-877d-4730-8318-07065c8c187d', u'faceRectangle': {u'width': 227, u'top': 124, u'height': 227, u'left': 459}}]
[{u'faceId': u'26998294-5703-415f-a544-69ee2d2ce1b1', u'faceRectangle': {u'width': 140, u'top': 116, u'height': 140, u'left': 265}}]
gaoshine1:
[{u'faceId': u'e404b11f-b81f-4a52-acd2-4948b77d59d8', u'faceRectangle': {u'width': 185, u'top': 189, u'height': 185, u'left': 110}}]
gaoshine:
[{u'faceId': u'a8e746eb-a237-44d3-b862-96ee20b73a9f', u'faceRectangle': {u'width': 234, u'top': 149, u'height': 234, u'left': 66}}]
'''
import cognitive_face as CF
import json

person1Faceid = 'e404b11f-b81f-4a52-acd2-4948b77d59d8'


def faceron(imgurl):
    KEY = '8505cfe15e5c49e3b3bf973852efe464' # Replace with a valid Subscription Key here.
    CF.Key.set(KEY)

    BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/' # Replace with your regional Base URL CF.BaseUrl.set(BASE_URL)

    result = CF.face.detect(imgurl)
    faceID = result[0]['faceId']

    result =CF.face.verify(person1Faceid,faceID)
    return result

if __name__ == '__main__':
    img_url = 'http://221.193.242.133:5113/gaoshine/myface.jpg'
    r = faceron(img_url)
    print r['isIdentical'],r['confidence']




