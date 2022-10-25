import pymysql
from pymysql.constants import CLIENT
import sys

pid = sys.argv


def del_sql(pid: str):
    dbhost = 'localhost'
    dbuser = 'root'
    dbpass = 'Sh123456!'
    dbname = 'pixiv'

    db = pymysql.connect(host=dbhost, user=dbuser, passwd=dbpass,
                         database=dbname, client_flag=CLIENT.MULTI_STATEMENTS)
    cursor = db.cursor()

    sql = """
    delete from info where pid={};
    alter table info drop id;
    alter table info add id int unsigned not null first;
    alter table info modify column id int unsigned not null auto_increment, add primary key( id );
    """.format(pid)

    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return True
    except:
        db.rollback()
        print(db.Error)
        db.close()
        return False


if __name__ == '__main__':
    s = input("要删除的图片的pid ：")
    del_sql(s)
