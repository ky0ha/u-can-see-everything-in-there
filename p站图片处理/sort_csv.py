import csv

root_path = "C:\\Users\\25315\\Desktop\\文件\\图片\\pixiv\\"
file_path = root_path+"file\\"

ls = []
with open(file_path+"new_info.csv", 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    for i in f:
        temp = list(i.split(','))
        temp[-1] = temp[-1][:-1]
        ls.append(temp)

ls.sort(key=lambda x: eval(x[0]))
for i in ls:
    print(i)

with open(file_path+"new_info_sorted.csv", 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerows(ls)
