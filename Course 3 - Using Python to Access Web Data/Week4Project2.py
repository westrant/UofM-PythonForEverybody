import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = "http://py4e-data.dr-chuck.net/known_by_Mhurain.html"
count = int(input("Enter count: ")) + 1
position = int(input("Enter position: ")) - 1

for i in range(0, count):  ## Loop through number of times user inputs.
    print("Retrieving: ", url)  ## Output requested in the assignment.
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position].get("href", None)  ## get the tag at the position user specifies.
