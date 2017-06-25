# -*- coding: utf-8 -*-

import httplib, urllib, base64, json

def getocr():
    subscription_key = 'daae48cfb7aa4b4c978c14a1bab9ef2b'

    uri_base = 'westcentralus.api.cognitive.microsoft.com'

    headers = {
        # Request headers.
        'Content-Type': 'application/octet-stream',  #application/octet-stream  application/json
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    params = urllib.urlencode({
        # Request parameters. The language setting "unk" means automatically detect the language.
        'language': 'zh-Hans',
        'detectOrientation ': 'true',
    })

    # The URL of a JPEG image containing text.
    #body = "{'url':'https://www.imcia.com/6.jpg'}"

    body = open("mytxt.png", "rb").read()

    try:
        # Execute the REST API call and get the response.
        conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/ocr?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()

        # 'data' contains the JSON data. The following formats the JSON data for display.
        parsed = json.loads(data)
        r = parsed['regions'][0]['lines'][0]['words'][0]['text']

        #print (json.dumps(parsed, sort_keys=True, indent=2))
        conn.close()
        if r:
            return r

    except Exception as e:
        print('Error:')
        print(e)


if __name__ == '__main__':
    r= getocr()
    print r
