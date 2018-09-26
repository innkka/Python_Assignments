# reads url using urllib 

#  http://py4e-data.dr-chuck.net/comments_42.html
# http://py4e-data.dr-chuck.net/comments_115301.html

import urllib.request, urllib.parse, urllib.error
import re
#from bs4 import BeautifulSoup

url = input('enter the URL ')
#print(url)
file_handle = urllib.request.urlopen(url)

#tags = soup('a')

numbers = list()

for line in file_handle:

    line = line.decode().strip()
    #print(line)

    number = re.findall('[0-9]\S+?<', line)

    #number = re.findall('[0-9]*$/', line)

    #number = list(number)

    if len(number) == 0: continue
    #print(number)
    #print('number is ', type(number))

    newstring = number[0]
    #print('newstring is ', type(newstring))
    print('')
    print('newstring is', newstring)
    print('lenght of newstring is', len(newstring))

    tempnumber = str()

    for letter in newstring:
        try:
            digit = int(letter)
            tempnumber = tempnumber + letter
            print('its a digit', digit)
            print('its a tempnumber', tempnumber)
        except:
            print('its a letter', letter)

    numbers.append(int(tempnumber))

print(sum(numbers))
