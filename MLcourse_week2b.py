# ML Course - Assignment 1 - Linear Regression with 1 var

# as cvs (results are destored, don't know why. probably because the original file is txt and not csv)
import csv
# ex1data1.txt

#%precision 2

fname = input("Enter file name: ")

try:
    file_handle = open(fname)

except:
    print('enter a valid file name')
    quit()

with open ('ex1data1.txt') as csvfile:
    data = list(csv.DictReader(csvfile))

count = 0

for line in data:
    print(line)
    print(type(line))
    count += 1

print('lines = ', count)
#print(data)
#print(type(data))
#print(len(data))
