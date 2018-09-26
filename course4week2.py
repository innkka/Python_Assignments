# sqlite

import sqlite3
import re

#1. Give a name to the future sql file, task.sqlite
connection = sqlite3.connect('task.sqlite')

#2. create a handle to the sql file
cur = connection.cursor()

#3. if the file already exist, delete it (?)
cur.execute('DROP TABLE IF EXISTS Counts')

#4. if not, create a table within the file with 2 columns (attributes): org and count
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

#5. define a name to a text file mbox.txt
fname1 = 'mbox.txt'
fname2 = 'mbox_test.txt'

#6. create a handle to that text file
file_handle = open(fname1)

#7. read the text file
for line in file_handle:

    #8. finds lines that start with "From" and print them
    if not line.startswith('From: '): continue
    line = line.strip()
    print(line)

    #9. extract domain from emails and print it
    org = re.findall('@(.*)', line)
    org = org[0]
    print(org)
    print('')

    #10. insert the domain into the table... ??? START HERE

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()

    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))

connection.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()



    #1. extract domain with split('@') or regex -- V
    #2. add a line with the domain if there is no such line + count '1'
    #3.  if there is a line with the domain name, add 1 to the existing count
    #4. order according to counts
    #5. find the largest count (first or last row in the table)





    #addr = 'monty@python.org'
    #uname, domain = addr.split('@' )
    #print(domain)
    #print('')
