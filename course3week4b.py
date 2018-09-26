# reading from the web using urllib and BeautifulSoup 

#  http://py4e-data.dr-chuck.net/known_by_Fikret.html
#  http://py4e-data.dr-chuck.net/known_by_Danyil.html

import urllib.request, urllib.parse, urllib.error
import re
#from bs4 import BeautifulSoup

url = input('enter the URL ')

#while len(url) != 0:

keyLine = 18 # change it!
stepCount = 0

for loops in range(1,8):

    stepCount += 1
    print('step no.', stepCount)

    file_handle = urllib.request.urlopen(url)
    lineCount = 0

    for line in file_handle:

        currentline = (line.decode().strip())

        reference = re.findall('http:.+?html', currentline)  # finds a link

        if len(reference) == 0: continue

        url = reference[0]
        print(url)
        lineCount += 1
        print(lineCount)

        if lineCount == keyLine: break


    #print(url)

    print('***')
    print(url)
