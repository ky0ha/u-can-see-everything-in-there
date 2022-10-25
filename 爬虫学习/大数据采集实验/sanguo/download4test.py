import os
from tkinter import *
from tkinter import messagebox

class MY_GUI:
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
        self.root_path = os.path.abspath(os.path.dirname(__file__))
        from sanguo import books
        self.books = books
    
    def set_init_window(self):
        self.init_window_name.title("三国演义下载器 201926205073杨斌")
        self.init_window_name.geometry('1192x600')
        
        self.init_data_label = Label(self.init_window_name, text="三国演义下载器")
        self.init_data_label.pack(fill='x', expand='yes')
        
        self.data_listbox = Listbox(self.init_window_name)
        self.data_listbox.pack(fill='x', expand='yes')
        for i in list(self.books.keys())[2::10]:
            self.data_listbox.insert("end", i)
        
        self.download_button = Button(self.init_window_name, text="下载此章", command=self.download_from_listbox)
        self.download_button.pack(fill='x', expand='yes')
        
        self.text = StringVar()
        self.show_text_label = Label(self.init_window_name, textvariable=self.text)
        self.show_text_label.pack(fill='x', expand='yes')
    
    def download_from_listbox(self):
        url = self.books[self.data_listbox.get('active')]
        self.text.set(url)
        messagebox.showinfo(title='提示', message='获取下载连接成功！')

def gui_start():
    init_window = Tk()
    ZMJ_PORTAL = MY_GUI(init_window)
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()

gui_start()