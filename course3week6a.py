# json

import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import re

# http://py4e-data.dr-chuck.net/comments_42.json
# http://py4e-data.dr-chuck.net/comments_115304.json

url = input('enter the URL ')  # enter an url
file_handle = urllib.request.urlopen(url)  # open the url

data = file_handle.read().decode("utf-8")  # decode the data from the url

print('file_handle is ', file_handle)

jsondata = json.loads(data)  # converts string to dictionnarie

#print(jsondata)  # data is a dict
print(type(jsondata))

print('the length is', len(jsondata))

commentsData = jsondata['comments']
#print(commentsData)

allsum = 0
for i in jsondata['comments']:
    element = i
    count = element['count']
    print(element)
    print(count)
    #print(type(count))
    allsum = allsum + count

print(allsum)



#commentdata = jsondata[1]
#print(commentdata)

#commentsDict = jsondata.keys(comments)
#print(commentsDict)
#for i in jsondata:
#    print(i)




# CRAWL THROUGH THE DICT AND FIND NUMBERS
