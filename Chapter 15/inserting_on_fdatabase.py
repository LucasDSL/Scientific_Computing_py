import sqlite3

conn = sqlite3.connect('music.sqlite') # Connect with the database with this name in the same folder, if there isn't one, creates one.
cur = conn.cursor() # Cursor is the handler of the connection, finds the way to manipulate the data storage in the databse, very similares to the open() method.

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('My way', 15))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))

conn.commit() # Force the data to be written inside the database 

print('Tracks: ')
cur.execute('SELECT title, plays FROM Tracks') # Doesn't read all the data in the database, but reads every time the for loop below iterates in the connection
for row in cur: 
    # Connection is open so we can use the data that is beeing passed by it.
    print(row)

cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()
conn.close()