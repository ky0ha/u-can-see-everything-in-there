import csv
from os import close

root_path = "C:\\Users\\25315\\Desktop\\文件\\图片\\pixiv\\"
temp_path = root_path+"temp\\"
file_path = root_path+"file\\"


addation = open(file_path+"new_info.csv", 'r', encoding='utf-8')
target = open(file_path+"record.csv", 'a', encoding='utf-8', newline='')
r = csv.reader(addation)
w = csv.writer(target)
for i in r:
    w.writerow(i)
addation.close()
target.close()
