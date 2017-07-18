import urllib.request, json 
from pprint import pprint
link = 'https://www.hackerearth.com/chrome-extension/events/'

with urllib.request.urlopen(link) as url:
    data = json.loads(url.read().decode())
    #pprint(data)
    print(data['response'][0]['time'])

