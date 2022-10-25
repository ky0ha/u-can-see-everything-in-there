import os


def del_file(pid: str):
    file_list = list(map(lambda x: x.split('_p0.'), os.listdir(
        "C:\\Users\\25315\\Desktop\\文件\\图片\\pixiv")))

    for i in file_list:
        if pid == i[0]:
            os.remove(
                "C:\\Users\\25315\\Desktop\\文件\\图片\\pixiv\\{}_p0.{}".format(i[0], i[1]))
            print("删除成功")
            break
    else:
        print("未找到该文件")


if __name__ == '__main__':
    pid = input("输入要删除的图片id => ")
    del_file(pid)
