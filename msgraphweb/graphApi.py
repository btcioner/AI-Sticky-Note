# -*- coding: utf-8 -*-
import json
import uuid
import urllib
import re
import requests


def get_mail():
    token_url = 'http://localhost:5000/get_token'
    get_mail_url = 'https://graph.microsoft.com/v1.0/me/messages'
    tokenRes = urllib.request.urlopen(token_url)
    token = str(tokenRes.readline())
    #tokenp = re.compile(r'b\'(.*)\'')
    #token = re.findall(tokenp,token)
    token = token[2:]
    token = token[:-1]
    #print(token)
    headers = {'User-Agent' : 'python_tutorial/1.0',
               'Authorization' : 'Bearer {0}'.format(token),
               'Accept' : 'application/json',
               'Content-Type' : 'application/json'}
    request_id = str(uuid.uuid4())
    instrumentation = {'client-request-id' : request_id,
                       'return-client-request-id' : 'true'}
    headers.update(instrumentation)
    mailReq = urllib.request.Request(get_mail_url,headers=headers)
    mailRes = urllib.request.urlopen(mailReq)
    #print(mailRes.read())
    mail = str(mailRes.read())
    patternSubject = re.compile(r'subject":"(.*?)"')
    subjectAll = re.findall(patternSubject,mail)
    return subjectAll
   
def get_event():
    token_url = 'http://localhost:5000/get_token'
    get_event_url = 'https://graph.microsoft.com/v1.0/me/events'
    tokenRes = urllib.request.urlopen(token_url)
    token = str(tokenRes.readline())
    #tokenp = re.compile(r'b\'(.*)\'')
    #token = re.findall(tokenp,token)
    token = token[2:]
    token = token[:-1]
    headers = {'User-Agent' : 'python_tutorial/1.0',
               'Authorization' : 'Bearer {0}'.format(token),
               'Accept' : 'application/json',
               'Content-Type' : 'application/json'}
    request_id = str(uuid.uuid4())
    instrumentation = {'client-request-id' : request_id,
                       'return-client-request-id' : 'true'}
    headers.update(instrumentation)
    eventReq = urllib.request.Request(get_event_url,headers=headers)
    eventRes = urllib.request.urlopen(eventReq)
    event = str(eventRes.read())
    patternSubject = re.compile(r'subject":"(.*?)"')
    subjectAll = re.findall(patternSubject,event)
    patternStartTime = re.compile(r'start":{"dateTime":"(.*?)"')
    startTimeAll = re.findall(patternStartTime,event)
    patternEndTime = re.compile(r'end":{"dateTime":"(.*?)"')
    endTimeAll = re.findall(patternEndTime,event)
    result = zip(subjectAll,startTimeAll)
    return list(result)

def creat_event(subject,startTime):
    post_data = {}
    post_data = {
        'subject': subject,
        'body':{
                "contentType": "HTML",
                "content": "Does late morning work for you?"
                },
        'start':{
                "dateTime": startTime,
                "timeZone": "China Standard Time"
                 },
        'end':{
                "dateTime": startTime,
                "timeZone": "China Standard Time"
              },
        "location":{
                "displayName":"SYNCED"
              },
        "attendees": [
              {
                "emailAddress": {
                "address":"xthkeer@gmail.com",
                "name": "xthkeer"
              },
             "type": "required"
              }
            ]
    }   
    #data = urllib.parse.urlencode(values).encode(encoding='UTF8')
    #post_data = urllib.parse.urlencode(post_data).encode(encoding='UTF8')
    print (post_data)
    token_url = 'http://localhost:5000/get_token'
    creat_event_url = 'https://graph.microsoft.com/v1.0/me/events'
    tokenRes = urllib.request.urlopen(token_url)
    token = str(tokenRes.readline())
    #tokenp = re.compile(r'b\'(.*)\'')
    #token = re.findall(tokenp,token)
    token = token[2:]
    token = token[:-1]
    headers = {'User-Agent' : 'python_tutorial/1.0',
               'Prefer' : 'China',
               'Authorization' : 'Bearer {0}'.format(token),
               'Accept' : 'application/json',
               'Content-Type' : 'application/json',
               'Content-Length' : '600'}
    request_id = str(uuid.uuid4())
    instrumentation = {'client-request-id' : request_id,
                       'return-client-request-id' : 'true'}
    headers.update(instrumentation)
    creatEventRes = requests.post(url=creat_event_url,
                             headers=headers,
                             data=json.dumps(post_data),
                             verify=False,
                             params=None)
    print(creatEventRes.text)
    
if __name__ == '__main__':
    print(get_mail())
    print(get_event())
    #creat_event('a','2017-06-28T12:00:00')
    #get_mail()



