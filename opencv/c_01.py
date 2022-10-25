import csv

points = []

with open('C:\\Users\\25315\\Desktop\\EdgeContour1.csv', 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    for row in r:
        points.append(row)

print(points)
