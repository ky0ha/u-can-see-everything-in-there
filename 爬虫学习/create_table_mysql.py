import pymysql

dbhost = 'localhost'
dbuser = 'root'
dbpass = '123456'
dbname = 'test_db'

db = pymysql.connect(host=dbhost, user=dbuser, passwd=dbpass, database=dbname)
cursor = db.cursor()
cursor.execute("USE test_db;")
cursor.execute("DROP TABLE IF EXISTS employee;")

sql = '''CREATE TABLE `employee`(
    `id` INT(10) NOT NULL AUTO_INCREMENT,
    `first_name` CHAR(20) NOT NULL,
    `last_name` CHAR(20) DEFAULT NULL,
    `age` INT(11) DEFAULT NULL,
    `sex` CHAR(1) DEFAULT NULL,
    `income` FLOAT DEFAULT NULL,
    PRIMARY KEY (`id`)
    )ENGINE = InnoDB DEFAULT CHARSET=utf8mb4;'''

cursor.execute(sql)
print ("Created table Successful! :>")
db.close()