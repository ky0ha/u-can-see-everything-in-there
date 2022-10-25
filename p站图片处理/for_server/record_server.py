import csv


def write_record():
    f1 = open("C:\\Users\\25315\\Desktop\\文件\\图片\\pixiv\\file\\new_info.csv",
              'r', encoding='utf-8')
    f2 = open("C:\\Users\\25315\\Desktop\\文件\\图片\\pixiv\\file\\server_record.csv",
              'a', encoding='utf-8', newline='')
    w = csv.writer(f2)
    w.writerow(['pid', 'author', 'uid', 'original', 'local'])
    for i in list(csv.reader(f1))[1:]:
        i[4] = "/home/tomcat/apache-tomcat-9.0.44/webapps/blogger/image/pixiv/" + \
            i[4].split('/')[-1]
        w.writerow(i)
    f1.close()
    f2.close()


def write_new_info():
    f1 = open("C:\\Users\\25315\\Desktop\\文件\\图片\\pixiv\\file\\new_info.csv",
              'r', encoding='utf-8')
    f2 = open("C:\\Users\\25315\\Desktop\\文件\\图片\\pixiv\\file\\server_new_info.csv",
              'a', encoding='utf-8', newline='')
    w = csv.writer(f2)
    for i in list(csv.reader(f1))[1:]:
        i[4] = "/home/tomcat/apache-tomcat-9.0.44/webapps/blogger/image/pixiv/" + \
            i[4].split('/')[-1]
        w.writerow(i)
    f1.close()
    f2.close()


# write_record()
write_new_info()
