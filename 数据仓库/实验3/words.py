import re

# 1）从文件里找出单词列表
with open(r'C:\Users\25315\Documents\Tencent Files\253157225\FileRecv\1.txt','r') as f: words = list(set([i for line in f for i in line.strip('\n\t ?').lower().split() if re.match(r'^\d', i)==None]))
print(f"提取得到的单词表:\n {words}")

# 2）设置常用单词列表（比如小学和初中的英语词汇表）
sample_alaph = ['which', 'average', 'is', 'student', 'and', 'takes', 'the', 'of', 'ten', 'd', 'x', 'students', 'point', 'it', 'down', 'further', 'c', 'in', 'after', 'each', 'hours', 'five', 'fifth', 'minutes', 'time', 'what', 'part', 'does', 'a', 'as', 'to', 'b', 'three', 'zero', 'another']

# 3）从文件的单词列表中去除常用单词列表
[words.pop(i) for i in range(len(words)-1, -1, -1) if words[i] in sample_alaph]

# 输出结果
print(f"去除常用单词后的单词表:\n {words}")