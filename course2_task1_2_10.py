name = input("Enter file:")

try:
    handle = open(name)

except:
    print('enter a valid file name')
    quit()


hourCounts = dict()
hourList = list()

for i in handle:
    line = i.strip()
    lineList = line.split()

    if len(lineList) <= 1 : continue
    if lineList[0] != 'From' : continue

    time = lineList[5]
    timeList = time.split(':')
    hour = timeList[0]

    hourCounts[hour] = hourCounts.get(hour, 0) + 1

hourList = hourCounts.items()

hourListS = sorted(hourList)

for i,j in hourListS:
    print(i,j)
