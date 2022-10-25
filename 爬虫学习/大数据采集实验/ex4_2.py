# 运行函数10000次，统计单个字符，两个一样或两个连续的字符（如aa,ab,dc），
# 三个一样或三个连续的字符（如aaa,abc,gfe），...，五个一样或五个连续的个数，
# 不能重复统计，并用matplotlib画出来

from ex4_1 import *
import matplotlib.pyplot as plt
import re

string = ''.join(rand_alphabet(10000))
print(string)

same = {}
left, right = 0, 1
while right<10000:
    if right-left==5:
        same[f'{right-left}'] = same.setdefault(f'{right-left}', 0) + 1
        left = right
        right+=1
    elif string[left]==string[right]:
        right+=1
    else:
        if right-left>1:
            same[f'{right-left}'] = same.setdefault(f'{right-left}', 0) + 1
        left = right
        right+=1
print(same)

unique = {}
left, right = 0, 1
flag = 0
while right<10000:
    if right-left==5:
        unique[f'{right-left}'] = unique.setdefault(f'{right-left}', 0) + 1
        flag = 0
        left = right
        right+=1
    elif (ord(string[right-1])-ord(string[right])==1 or ord(string[right-1])-ord(string[right])==-1) and flag==0:
        flag = ord(string[right-1])-ord(string[right])
        right+=1
    elif ord(string[right-1])-ord(string[right])==flag and flag!=0:
        right+=1
    else:
        if right-left>1:
            unique[f'{right-left}'] = unique.setdefault(f'{right-left}', 0) + 1
        flag = 0
        left = right
        right+=1
print(unique)







# def is_adjacent_or_same(string, schema='double'):
#     result = False
#     way = ''
#     if len(string)>5:
#         return False
#     if schema=='double':
#         if string[0]==string[1] or abs(ord(string[0])-ord(string[1]))==1:
#             result = True
#     else:
#         for i in range(1, len(string)):
#             if way:
#                 if way=='positive':
#                     if ord(string[i])-ord(string[i-1])==1:
#                         result = True
#                     else:
#                         result = False
#                         break
#                 elif way=='nagetive':
#                     if ord(string[i-1])-ord(string[i])==1:
#                         result = True
#                     else:
#                         result = False
#                         break
#                 elif way=='equal':
#                     if abs(ord(string[i])-ord(string[i-1]))!=0:
#                         result = False
#                         break
#             elif abs(ord(string[i])-ord(string[i-1]))==1:
#                 if ord(string[i])-ord(string[i-1])==1:
#                     way = 'positive'
#                 else:
#                     way = 'nagetive'
#             elif string[i]==string[i-1]:
#                 way = 'equal'
#                 result = True
#             else:
#                 result = False
#                 break
#     return result        

# string = ''.join(rand_alphabet(10000))
# print(string)
# schema_list = ['single', 'double', 'triple', 'quadruple', 'quintuple']
# result = [10000, 0, 0, 0, 0]
# left, right = 0, 2
# while right<=10000:
#     try:
#         if right-left>5:
#             result[4] += 1
#             left = right-1
#             right += 1
#         elif is_adjacent_or_same(string[left:right], schema=schema_list[right-left-1]):
#             right += 1
#             continue
#     except:
#         print(string[left:right], left, right, 1)
#         result[right-left] += 1
#         break
#     else:
#         print(string[left:right], left, right, 2)
#         result[right-left-1] += 1
#         left = right-1
#         right += 1

# plt.bar(schema_list, result)
# plt.show()
    