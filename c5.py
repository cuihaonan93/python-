import urllib.request
import io
import sys
import re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

url_1 = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
digit = "63579"
def getdata(digit):
    url = url_1 + digit
    req = urllib.request.Request(url)
    webPage=urllib.request.urlopen(req)
    global data
    data = webPage.read()
    data = data.decode('utf-8')
    return data

i = 1
while i:
    getdata(digit)
    digit = re.findall(r'\d+',data)
    if digit:
        digit = digit[len(digit)-1]
        print(i,digit)
        i += 1
    else:
        print(data)
        i = 0
