import csv
import pymysql

dbhost = 'localhost'
dbuser = 'root'
dbpass = '123456'
dbname = 'pixiv'

db = pymysql.connect(host=dbhost, user=dbuser, passwd=dbpass, database=dbname)
cursor = db.cursor()
sql_sechma = "insert into info (pid, author, uid, original, local) values "

with open("C:\\Users\\25315\\Desktop\\文件\\图片\\pixiv\\file\\new_info.csv", 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    for i in r:
        try:
            temp_command = sql_sechma + \
                "('{}', '{}', '{}', '{}', '{}')".format(
                    i[0], i[1], i[2], i[3], i[4])
            print(temp_command)
            cursor.execute(temp_command)
            db.commit()
        except:
            db.rollback()
            print(db.Error)

db.close()
