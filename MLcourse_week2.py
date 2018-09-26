# ML Course - Assignment 1 - Linear Regression with 1 var
#import numpy as np
# ex1data1.txt

fname = input("Enter file name: ")

try:
    file_handle = open(fname)

except:
    print('enter a valid file name')
    quit()

for i in file_handle:
    line = i.strip()  # erases extra space between the lines
    print(line)
    print(type(line))

    line = line.split(',')
    print(line)
    print(type(line))

    for j in line:
        number = float(j)
        print(number)

    #number = line[0]
    #number = float(number)
    #print(number)
    #print(type(number))
    #print('')

# PROBLEM: reading a txt file and convert it to a matrix. Should I use NUMPY? PANDAS? 
