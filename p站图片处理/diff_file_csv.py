import csv
import os
import shutil


root_path = "C:\\Users\\25315\\Desktop\\文件\\图片\\pixiv\\"
temp_path = root_path+"temp\\"
file_path = root_path+"file\\"

file_list = sorted(os.listdir(temp_path))

record_list = []
with open(file_path+"new_info_sorted.csv", 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    for i in r:
        record_list.append(list(i[-1].split('/'))[-1])
    record_list = sorted(record_list)

distinct_count = 0

for i in range(max(len(file_list), len(record_list))):
    if record_list[i] != file_list[i]:
        print("{}\tdifferent in => {}\t{}".format(
            i, record_list[i], file_list[i]))
    else:
        try:
            shutil.move(temp_path+file_list[i], root_path)
        except shutil.Error:
            distinct_count += 1
            print("重复："+record_list[i])
