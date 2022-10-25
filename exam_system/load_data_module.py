import pymysql
import pandas as pd

data = pd.read_excel("C:\\Users\\25315\\Desktop\\test_result.xls")
print(data)
eno = list(data.loc[:,"eno"])
cno = list(data.loc[:,"cno"])
sno = list(data.loc[:,"sno"])
grade = list(data.loc[:,"grade"])

dbhost = 'localhost'
dbuser = 'root'
dbpass = '123456'
dbname = 'test_db'

db = pymysql.connect(host=dbhost, user=dbuser, passwd=dbpass, database=dbname)
cursor = db.cursor()
# cursor.execute("SELECT * FROM test_tb")
# data = cursor.fetchall()
# print (data)
sql = "insert into test_db.test_result(`eno`,`cno`,`sno`,`grade`) values "
for index,value in enumerate(sno):
    sql = sql + "({},{},{},{}),".format(eno[index], cno[index], sno[index], grade[index])
sql = sql[:-1] + ";"
    
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
else:
    print("Insert values Successful! ٩(๑>◡<๑)۶ ")
db.close()