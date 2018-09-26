# json

# address example: South Federal University
# Universidade do Minho

import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import re

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

location = input('enter the location ')
#file_handle = urllib.request.urlopen(location)
#print(location)

url = serviceurl + urllib.parse.urlencode({'address': location})  # encoding the address into readable url

print(url)

print('Retrieving', url)
connection = urllib.request.urlopen(url)
data = connection.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
    print(json.dumps(js, indent = 4))
    print('')
    print(js['results'][0]['place_id'])
    #place_id =
except:
    js = None
