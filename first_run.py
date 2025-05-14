import sqlite3

conn = sqlite3.connect('users.db')

cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT,
        password TEXT
    )
''')
conn.close()


#NOTE: TESTING 
# conn = sqlite3.connect('users.db')
# cursor = conn.cursor()
# cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('test', 'password'))
# conn.commit()
# conn.close()



# conn = sqlite3.connect('users.db')
# cur = conn.cursor()
# cur.execute('SELECT * FROM users')
# rows = cur.fetchall()
# conn.close()
# for row in rows:
#    print(row)
