import requests
import json
import datetime

now = datetime.datetime.now()
print (datetime.datetime.now().strftime("%y"))

r = requests.get("http://107.167.181.179:8080/api/v1/courses/keywords")
json_data = json.loads(r.text)
ParsedValue = json_data['data']
for x in range(len(ParsedValue)):
    print(ParsedValue[x])
    url1 = "http://104.155.227.109:8080/api/v3/makeDirectory/"+str(ParsedValue[x])
    r1 = requests.get(url1)
    print(r1.text);
    url2 = "http://104.155.227.109:8080/api/v3/makeKeywordContents/"+str(ParsedValue[x])
    r2 = requests.get(url2)
    print(r2.text);
    url3 = "http://104.155.227.109:8080/api/v3/insertKeywordToSQL/"+str(ParsedValue[x])
    r3 = requests.get(url3)
    print(r3.text);
    url4 = "http://104.155.227.109:8080/api/v1/createChapterMap/"+str(ParsedValue[x])
    r4 = requests.get(url4)
    print(r4.text);
