import sqlite3

conn = sqlite3.connect('sqlite.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS orders(
   orderid INT PRIMARY KEY,
   date TEXT,
   userid TEXT,
   total TEXT);
""")
conn.commit()

cur.execute("""INSERT INTO users(userid, fname, lname, gender) 
   VALUES('00001', 'Alex', 'Smith', 'male');""")
conn.commit()

user = ('00002', 'Lois', 'Lane', 'Female')
cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
conn.commit()

more_users = [('00003', 'Peter', 'Parker', 'Male'), ('00004', 'Bruce', 'Wayne', 'male')]
cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", more_users)
conn.commit()

cur.execute("SELECT * FROM users;")
one_result = cur.fetchone()
print(one_result)

cur.execute("SELECT * FROM users;")
three_results = cur.fetchmany(3)
print(three_results)

cur.execute("SELECT * FROM users;")
all_results = cur.fetchall()
print(all_results)

cur.execute("DELETE FROM users WHERE lname='Parker';")
conn.commit()

cur.execute("""SELECT *, users.fname, users.lname FROM orders
    LEFT JOIN users ON users.userid=orders.userid;""")
print(cur.fetchall())

conn.close()
