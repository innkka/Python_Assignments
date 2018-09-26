# regular expressions

import re  # importing regular expressions

name = input("Enter file:")

# 'regex_sum_42.txt'
# 'regex_sum_115299.txt'

#print('hello')

try:  # try open the file. If not in the folder, quit
    textH = open(name)

except:
    print('enter a valid file name')
    quit()

numbers = list()
count = 0
#lineCount = 0

for i in textH:
    line = i.strip()
    #lineCount += 1
    #print('line num is ', lineCount)
    number = re.findall('[0-9]\S+', line)
    number = list(number)

    if len(number) == 0: continue

    #print('the list of numbers is ', number)

    for j in number:
        try:
            numberInt = int(j)
            #print(numberInt)
            numbers.append(numberInt)
            count += 1
            #print(numbers)

        except:
            print('cant convert to an integer')


print('sum = ', sum(numbers))
print('count = ', count)
