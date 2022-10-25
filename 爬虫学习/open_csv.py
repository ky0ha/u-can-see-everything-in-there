import csv
with open('C:\\Users\\25315\\Desktop\\learn1.csv', 'a', encoding='utf-8',newline='') as f:
    wr = csv.writer(f)
    wr.writerow(['学号', '姓名'])
    wr.writerows(['201926205073', '杨斌'] for i in range(5))
    print('writed!')
with open('C:\\Users\\25315\\Desktop\\learn1.csv', 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    for i in r:
        print(i)