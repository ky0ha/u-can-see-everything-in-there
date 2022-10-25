import requests, os, random
from tkinter import *
from bs4 import BeautifulSoup
from tkinter import messagebox

class MY_GUI:
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
        self.root_path = os.path.abspath(os.path.dirname(__file__))
        from sanguo import books
        self.books = books
    
    def set_init_window(self):
        self.init_window_name.title("三国演义下载器")
        self.init_window_name.geometry('1192x600')
        
        self.init_data_label = Label(self.init_window_name, text="三国演义下载器")
        self.init_data_label.pack(fill='x', expand='yes')
        
        self.data_listbox = Listbox(self.init_window_name)
        self.data_listbox.pack(fill='x', expand='yes')
        for i in self.books.keys():
            self.data_listbox.insert("end", i)
        
        self.download_button = Button(self.init_window_name, text="下载此章", command=self.download_from_listbox)
        self.download_button.pack(fill='x', expand='yes')
        
        self.text = StringVar()
        self.show_text_label = Label(self.init_window_name, textvariable=self.text)
        self.show_text_label.pack(fill='x', expand='yes')
    
    def download_from_listbox(self):
        USER_AGENTS = [
            "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1"
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
            "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
            "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
            "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12 "
        ]
        # proxies = ["http://27.22.85.58:8100",
        #            "http://14.126.30.69:8888",
        #            "http://120.26.160.120:7890",
        #            "http://121.13.252.58:41564"]
        url = self.books[self.data_listbox.get('active')]
        headers = {'User-Agent': random.choice(USER_AGENTS)}
        re = requests.get(url=url, headers=headers, verify=False)
        re.encoding = re.apparent_encoding
        print(re.raise_for_status)
        text = re.text
        data = BeautifulSoup(text, 'html.parser')
        result = data.find('div', {"class":"chapter_content"})
        # result = data.find('p')
        # print(result.get_text())
        with open(self.root_path+'\\file.txt', 'w', encoding='utf-8') as f:
            f.write(self.data_listbox.get('active'))
            f.write(result.get_text())
        messagebox.showinfo(title='提示', message='下载成功！')
        self.text.set(result.get_text()[:101])

def gui_start():
    init_window = Tk()
    ZMJ_PORTAL = MY_GUI(init_window)
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()

gui_start()