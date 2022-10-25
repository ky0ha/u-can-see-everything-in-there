import csv
import pymysql

dbhost = 'localhost'
dbuser = 'root'
dbpass = '123456'
dbname = 'pixiv'

db = pymysql.connect(host=dbhost, user=dbuser, passwd=dbpass, database=dbname)
cursor = db.cursor()

sql = "select pid, author, uid, original, local from info"
cursor.execute(sql)
data = cursor.fetchall()

with open("C:\\Users\\25315\\Desktop\\文件\\图片\\pixiv\\file\\record.csv", "w", encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['pid', 'author', 'uid', 'original', 'local'])
    for i in data:
        print(i, end='\n')
        w.writerow(i)
