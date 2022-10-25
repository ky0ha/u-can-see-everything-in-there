import re

lyric = {}
with open('C:\\Users\\25315\\Desktop\\金雅中 - Maria.lrc', 'r', encoding='utf-8') as f:
    text = f.readlines()
    for i in text:
        # if i[0] == '[':
        #     cursor = 0
        #     while True:
        #         cursor += 1
        #         if i[cursor] == ']':
        #             break
        #         elif i==100:
        #             raise Exception('指针i的大小超过了阈值100')
        #     info = i[1:cursor].split(':')
        #     if info[0].isdecimal():
        #         # lyric[info[0]] = lyric.setdefault(info[0], i[cursor+1:]).append(i[cursor+1:])
        #         if lyric.get(i[1:cursor])==None:
        #             lyric[i[1:cursor]] = [i[cursor+1:].replace('\n', '')]
        #         else:
        #             lyric[i[1:cursor]].append(i[cursor+1:].replace('\n', ''))
        index = re.search(r'\d{2}:\d{2}.\d*', i)
        if index!=None:
            left, right = index.span()
            if lyric.get(i[left:right])==None:
                lyric[i[left:right]] = [i[right+1:].replace('\n', '')]
            else:
                lyric[i[left:right]].append(i[right+1:].replace('\n', ''))
                    
for key, value in lyric.items():
    print(key, value)

with open('C:\\Users\\25315\\Desktop\\文件\\code\\onlyVS\\python\\歌词处理\\test', 'w', encoding='utf-8') as f:
    for key, value in lyric.items():
        f.write(f'[{key}]{value[0]}\n')
        try:
            f.write(f'{value[1]}\n')
        except IndexError:
            continue