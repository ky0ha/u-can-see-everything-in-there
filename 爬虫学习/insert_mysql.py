import pymysql

dbhost = 'localhost'
dbuser = 'root'
dbpass = '123456'
dbname = 'test_db'

db = pymysql.connect(host=dbhost, user=dbuser, passwd=dbpass, database=dbname)
cursor = db.cursor()

sql = '''INSERT INTO employee
    (first_name, last_name, age, sex, income)
    VALUES
    ('Mac', 'Su', 20, 'M', 5000)
'''

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
else:
    print("Insert values Successful! :>")
    
db.close()