# -*- coding: utf-8 -*-


#import connectsample
import urllib3
import urllib
import uuid
import http.cookiejar

token = 'EwBAA8l6BAAU7p9QDpi/D7xJLwsTgCg3TskyTaQAAdqEX4oSmRitNHax3zVdAVgVPOsaqhhVJGsx7n8Y6/0aR6XT8pWgAR2GDbG7Wu8b0mISd0Kn+BsPRSuAxZxZ48vlkugdadhn5nU6PfTCyxrG4BK8nI3NtCErvq84JLZrjvdegOD+80c0gA45nLsoT/6N+lypxLjA1/rRlNcDJvBtHZFs1v+pXRSg08FzHuYxQ7uQL8sHckVikG5nJD9NQ09UQ18gUhJZBzIDDz30Y+w48PeSIBPZnaQuK3Tgi6LTyQ7R/ziOxN+p6IJHguJ5cmSYE5blthXaav7M3EhJkfvt6nejRvTHCyktqK8dVdYSVAGCPDNvUV3oBxQKByCLOmoDZgAACD31El637jUeEAL+xnZ7oOua7MnnskgeZKgwNZDFAs+a0zXibOg4cylRaJoskMFHHayo94i2VC/2+OGfgrAb3u7XJxWld/ncfwk5GZaTdt+9BH3imdaC/KAuCCs2H4R4b/Q+cDZGVzanQFKtDNVQRcUTEmPMWjqYw3SbsamoHuoVaYp/bzkOBsA8cw31t6jcqEdcBCAVmEhA0gEmICsJ8xYdtEhLYlCcXmbbzSmTF5OFN0jijltSgS+3fUaX033e3VlVPWY5xGhutoELSVyl6nQ9qUjGPiXNL537EvO/JaWsqmzzVfhhFdEEdETqoHZj+z/3EuIXe63KMZ5vpLUsXKVu7wpNIWUVOsaEG6AtsaYUL6YxAIsbM20XDNwD5f+hOG3Hc3sP5HYKqJkF16uy+a0Zvo/FvQjBSZvoBGWI82o2GawezGUe7HMTmQF1k/Gp4P8rND+6yLok0KY3SdPv1W+3j0ZZSalh/nOCqPLxyTqaTlLWmLdh4Fm5yK6TG7B9FuZv7VcJTh2VrPQoiWJm2dVI2pRtM2ESgw7tsE5vR8BNqaSRloFvw9hSdbWzP2twCmB8XxBQ5B0P4nXCy+4XwI3wSWlBZqniH7p70FUBbTUqk6N/Pb0cJhRFUzwtL1zvdAdutf6CY5+GYHvoFiwtd84bNr3V/HA+ayxjheNvGwsJnkMYNVUMmSGULPayYMmOCM8fTo3FVnabRSdCAg=='

#cookiename = 'cookie.txt'
if True:
#    cookie = cookielib.MozillaCookieJar(cookiename)
#    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    get_mail_url = 'https://graph.microsoft.com/v1.0/me/messages'
    url = 'http://127.0.0.1:5000/mytest'
    headers = {'User-Agent' : 'python_tutorial/1.0',
               'Authorization' : 'Bearer {0}'.format(token),
               'Accept' : 'application/json',
               'Content-Type' : 'application/json'}
    
    request_id = str(uuid.uuid4())
    instrumentation = {'client-request-id' : request_id,
                       'return-client-request-id' : 'true'}
    headers.update(instrumentation)
    
    f = urllib.request.Request(get_mail_url,headers=headers)
    res = urllib.request.urlopen(f)
    print(res.read())
    #print(f.read())
