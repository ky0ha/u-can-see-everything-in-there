from bs4 import BeautifulSoup
import os

root_path = os.path.abspath(os.path.dirname(__file__))

with open(root_path+"\\sanguo.html", 'r', encoding='utf-8') as f:
    text = f.read()
date = BeautifulSoup(text, 'html.parser')
menu = date.find('div', {"class":"book-mulu"}).descendants
books = {}
for i in list(menu)[1:-2:3][1:]:
    # print(i.get_text(), type(i))
    books.update({i.get_text():"https://www.shicimingju.com"+i.__getattribute__('attrs')['href']})
    # https://www.shicimingju.com/book/sanguoyanyi/113.html
    # print(i.__getattribute__('attrs'))
if __name__=='__main__':
    for key, value in books.items():
        print(f'{key} =>> {value}')