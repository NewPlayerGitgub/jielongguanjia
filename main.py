import requests
import json
false = False
true = True

if __name__ == '__main__':
    url = 'https://h-api.jielong.co/api/Thread/EditCheckInRecord'

    headers = {
            'Accept-Encoding' : 'gzip, deflate, br',
            'Accept-Language' : 'zh-CN,zh;q=0.9,en;q=0.8',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'Content-Type' : 'application/json',
            'Connection' : 'keep-alive',
            'Host' : 'h-api.jielong.co',
            'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOm51bGwsIm9wZW5JZCI6Im9vcm9FNXBJRHlTRkh3NVkzUWQxN1lsWFRGT1EiLCJpc3MiOiJhcGkuamllbG9uZy5jbyIsImF1ZCI6ImNsaWVudC5qaWVsb25nLmNvIiwiaWF0IjoxNjY4NTAxODc3LCJleHAiOjE2Njg3NjEwNzd9.VunTUKcNA697uU5nWtZbHcjpkOnCG1o1EdzAgqipVho
',#authorization填这里
    }

    data = {"Id":0,"ThreadId":86934414,"Number":"","Signature":"aaa","RecordValues":[],"DateTarget":"","IsNeedManualAudit":false,"MinuteTarget":-1,"IsNameNumberComfirm":false,"IsInvisible":false,"IsCurrentUser":true}#data填这里

    r = requests.post(url = url,headers = headers,json = data)
    print(r.json())
