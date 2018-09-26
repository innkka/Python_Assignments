# reads XML

# http://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_115303.xml

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import re

url = input('enter the URL ')
#print(url)
file_handle = urllib.request.urlopen(url)

#data = file_handle.read()
#print(data)

# lst = comment.findall(name/comment)
#counts = tree.findall('.//count')
#print(counts)

allnumbers = list()

for line in file_handle:

    currentline = line.decode().strip()

    #findnumber = re.findall('^<cou.*([0-9].+?)', currentline)  # finds a number

    if re.findall('^<count>.*', currentline):
        findnumber = re.findall('[0-9].*?', currentline)  # finds a number

        if len(findnumber) == 0: continue

        strnumber = str()

        #print(currentline)
        #print(findnumber)

        for i in findnumber:
            #print(i)
            strnumber += i
            #print(strnumber)

        number = int(strnumber)
        allnumbers.append(number)
        #print(allnumbers)

print('')
print(sum(allnumbers))
