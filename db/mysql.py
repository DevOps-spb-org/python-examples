import MySQLdb

conn = MySQLdb.connect('servername', 'username', 'userpassword', 'tablename')
cursor = conn.cursor()

cursor.execute("SELECT * FROM tablename")

# Получаем данные
row = cursor.fetchone()
print(row)

# Закрываем подключение
conn.close()
