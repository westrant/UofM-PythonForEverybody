import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = 'http://py4e-data.dr-chuck.net/comments_392838.xml'

data = urllib.request.urlopen(url).read()
## print('Retrieved', len(data), 'characters')
## print(data.decode())
tree = ET.fromstring(data)
counts = tree.findall('.//count')
total = 0
for count in counts:
    total = total + int(count.text)

print(total)
