import psycopg2

conn = psycopg2.connect(dbname='my_database', user='username')
cursor = conn.cursor()

# Выполняем запрос
cursor.execute("SELECT * FROM table_name")
row = cursor.fetchone()

# Закрываем подключение
cursor.close()
conn.close()
