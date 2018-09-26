name = input("Enter file:")

try:
    handle = open(name)

except:
    print('enter a valid file name')
    quit()


emailCounts = dict()

for i in handle:
    line = i.strip()
    lineList = line.split()

    if len(lineList) <= 1 : continue
    if lineList[0] != 'From' : continue

    email = lineList[1]

    emailCounts[email] = emailCounts.get(email, 0) + 1

emailValues = emailCounts.values()
emailValuesMax = max(emailValues)

for k,v in emailCounts.items():
    if v == emailValuesMax:
        print(k, v)
