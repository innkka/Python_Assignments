fname = input("Enter file name: ")

try:
    fh = open(fname)

except:
    print('enter a valid file name')
    quit()

line = list()
count = 0

for i in fh:
    line = i.split()
    #print(line)
    length = len(line)

    if length > 1:
        if line[0] == 'From':
            email = line[1]
            print(email)
            count += 1

#if len(fname) < 1 : fname = "mbox-short.txt"


print("There were", count, "lines in the file with From as the first word")
