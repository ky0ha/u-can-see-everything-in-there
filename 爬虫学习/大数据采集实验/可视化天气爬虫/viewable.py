from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog, dialog, ttk, messagebox

class GUI:
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
    
    def set_init_window(self):
        self.init_window_name.title("天气查询")
        self.init_window_name.geometry('1024x768+100+100')
        # self.init_window_name.iconbitmap(self.icon_path)

        self.init_title_label = Label(self.init_window_name, text='天气爬虫', font=tkFont.Font(family='KaiTi', size=30, weight=tkFont.BOLD))
        self.init_title_label.pack()
        self.empty_label = Label(self.init_window_name, text='')
        self.empty_label.pack()

        s = ttk.Style()
        s.configure("Treeview", rowheight=30)
        s.configure("Treeview.Heading", font=(None, 12))
        # s.configure("Treeview.Heading", font=tkFont.Font(size=10, weight=tkFont.BOLD))
        columns = ("date", "max_tem", "min_tem")
        self.data_showinfo_treelist = ttk.Treeview(self.init_window_name, show='headings', columns=columns, selectmod=BROWSE)
        self.data_showinfo_treelist.column("date",width=55, anchor='center')
        self.data_showinfo_treelist.column("max_tem",width=85,  anchor='center')
        self.data_showinfo_treelist.column("min_tem",width=85,  anchor='center')
        self.data_showinfo_treelist.heading("date", text="日期")
        self.data_showinfo_treelist.heading("max_tem", text="最高气温")
        self.data_showinfo_treelist.heading("min_tem", text="最低气温")
        self.data_showinfo_treelist.pack(side=TOP, fill=BOTH, expand=NO)

        self.create_searching_button = Button(self.init_window_name, text="新建查询", bd=3, font=tkFont.Font(family='KaiTi', size=20))
        self.create_searching_button.pack(side=BOTTOM)




def gui_start():
        init_window = Tk()
        ZMJ_PORTAL = GUI(init_window)
        ZMJ_PORTAL.set_init_window()
        init_window.mainloop()

gui_start()