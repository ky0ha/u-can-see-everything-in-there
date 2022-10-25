import pymysql

dbhost = 'localhost'
dbuser = 'root'
dbpass = '123456'
dbname = 'test_db'

db = pymysql.connect(host=dbhost, user=dbuser, passwd=dbpass, database=dbname)
cursor = db.cursor()
cursor.execute("SELECT * FROM test_db.test_tb;")
data = cursor.fetchall()
print (data)
