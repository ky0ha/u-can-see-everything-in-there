from tkinter import *
import json
import tkinter.font as tkFont
import os
from tkinter import ttk, messagebox

init_size, init_address = 0, 0

class disk_partition:
    size = 0
    address = 0
    flag = ''

    def __init__(self, size, address, flag):
        super().__init__()
        self.size = size
        self.address = address
        self.flag = flag
    
class MY_GUI:
    DISK_LIST = []
    def __init__(self, init_window_name):
        super().__init__()
        self.init_window_name = init_window_name
    
    def __read_config(self):
        global init_size, init_address
        path = os.path.abspath(os.path.dirname(__file__))
        with open(path + "//config//config.json", 'r', encoding='utf-8') as json_file:
            try:
                a = json.load(json_file)
            except:
                print("读取配置文件config.json失败")
                #self.message_error06()
            globals().update(a)
            json_file.close()
    
    def set_init_window(self):
        self.init_window_name.title("模拟可变分区存储算法")
        self.init_window_name.geometry("1024x768+100+100")
        # self.__read_config()

        self.main_title_label = Label(self.init_window_name, text="模拟可变分区存储算法", font=tkFont.Font(family='KaiTi', size=30, weight=tkFont.BOLD))
        self.main_title_label.pack()
        self.data_showinfo_label = Label(self.init_window_name, text="分区表：", font=tkFont.Font(family='KaiTi', size=25))
        self.data_showinfo_label.pack(side='top', anchor='w', expand='no')

        s = ttk.Style()
        s.configure("Treeview", rowheifht=30)
        s.configure("Treeview.Heading", font=(None, 15))
        columns = ("id", "size", "address", "station")
        self.data_showinfo_treelist = ttk.Treeview(self.init_window_name, show='headings', columns=columns, selectmod=BROWSE)
        self.data_showinfo_treelist.column("id",width=80, anchor='center')
        self.data_showinfo_treelist.column("size",width=100,  anchor='center')
        self.data_showinfo_treelist.column("address",width=100,  anchor='center')
        self.data_showinfo_treelist.column("station",width=150,  anchor='center')
        self.data_showinfo_treelist.heading("id", text="分区号")
        self.data_showinfo_treelist.heading("size", text="大小（KB）")
        self.data_showinfo_treelist.heading("address", text="起始（KB）")
        self.data_showinfo_treelist.heading("station", text="状态")
        self.data_showinfo_treelist.pack(side='top', fill='x', expand='no')

        self.memory_allocation_button = Button(self.init_window_name, text="内存分配", bd=3, font=tkFont.Font(family='KaiTi', size=20, weight=tkFont.BOLD))
        self.memory_allocation_button.pack()
        self.memory_release_button = Button(self.init_window_name, text="内存去配", bd=3, font=tkFont.Font(family='KaiTi', size=20, weight=tkFont.BOLD))
        self.memory_release_button.pack()
        self.exit_button = Button(self.init_window_name, text='退出程序', bd=3, font=tkFont.Font(family='KaiTi', size=20, weight=tkFont.BOLD), command=self.exit_program)
        self.exit_button.pack()
    
    def exit_program(self):
        flag = messagebox.askyesno(title="退出程序", message="确认退出程序？")
        if flag:
            self.init_window_name.destroy()
    
    # def memory_release(self, target):
        

def gui_start():
    init_window = Tk()
    ZMJ_PORTAL = MY_GUI(init_window)
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()

gui_start()