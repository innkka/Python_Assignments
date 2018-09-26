# sql
# relational
# reading xml file
# track.py

# Library.xml

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('taskWeek4.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER
);

''')

#print('hello')

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
#print(stuff)


for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    title = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
#   count = lookup(entry, 'Play Count')
#   rating = lookup(entry, 'Rating')
    len = lookup(entry, 'Total Time')
    genre = lookup(entry, 'Genre')

    if title is None or artist is None or album is None :
        continue

    print(title, artist, album, len, genre)

    # Artist table: id, name
    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]


    # Album table: id, Artist_id, title
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]


    # Genre table: id, name
    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', (genre,) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]


    # Track table: id, title, album_id, genre_id, len
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len)
        VALUES ( ?, ?, ?, ? )''',
        (title, album_id, genre_id, len) )
    cur.execute('SELECT id FROM Track WHERE title = ? ', (title, ))

    #cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    #id = cur.fetchone()[0]

    conn.commit()
