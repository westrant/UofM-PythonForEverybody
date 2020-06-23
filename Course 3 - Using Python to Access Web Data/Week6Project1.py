import urllib.request, urllib.parse, urllib.error
import ssl
import json

url = 'http://py4e-data.dr-chuck.net/comments_392839.json'

data = urllib.request.urlopen(url).read()
info = json.loads(data)

sum = 0

for item in info["comments"]:
    sum = sum + item["count"]

print(sum)
