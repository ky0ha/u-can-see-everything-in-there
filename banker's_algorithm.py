from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog, dialog, ttk, messagebox
import json
import os
import pandas as pd

path1, path2, icon_path = None, None, None

class disk_table:
    '''
    储存分区对象：用于表示分区的属性以及状态
    对象属性列表：
        id：表示分区的id号，数据类型为int
        size：表示分区的大小，数据类型为int
        address：表示分区的（起始）地址，数据类型为int
        station：表示分区目前的状态，目前哪一个任务正在储存在此分区内，数据类型为string
    
    对象方法列表：
        __init__：构造函数，需要一个参数ls
                  ls为list对象，是一个存储了分区预设属性内容的列表，是直接从csv读取后格式化的列表
        __getId：从ls中获取属性id
        __getSize：从ls中获取属性size
        __getAddress：从ls中获取属性address
        change_station_to：需要一个参数new_station，用于改变对象的station属性
    '''
    id = 0
    size = 0
    address = 0
    station = '0'

    def __init__(self, ls):
        '''
        构造函数，需要一个参数ls
        ls为list对象，是一个存储了分区预设属性内容的列表，是直接从csv读取后格式化的列表
        '''
        super().__init__()
        self.id = __getId(ls[0])
        self.size = __getSize(ls[1])
        self.address = __getAddress(ls[2])
    
    def __getId(self, value):
        '''
        需要一个参数value，从ls中获取属性id
        '''
        return int(value)
    
    def __getSize(self, value):
        '''
        需要一个参数value，从ls中获取属性size
        '''
        return int(value)
    
    def __getAddress(self, value):
        '''
        需要一个参数value，从ls中获取属性address
        '''
        return int(value)

    def change_station_to(self, new_sataion):
        '''
        需要一个参数new_station，用于改变对象的station属性
        '''
        self.station = new_sataion

class MY_GUI:
    disk_table_list = []
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
    
    def __read_config(self):
        global path1, path2, icon_path
        path = os.path.dirname(__file__)
        with open(path + "/config/config.json", 'r', encoding='utf-8') as json_file:
            try:
                a = json.load(json_file)
            except:
                self.message_error06()
            globals().update(a)
            json_file.close()
        
        try:
            self.image_path1 = os.path.abspath(os.path.dirname(__file__)) + path1       #通过全局变量path转化为相对路径image_path
            self.image_path2 = os.path.abspath(os.path.dirname(__file__)) + path2
            self.icon_path1 = os.path.abspath(os.path.dirname(__file__)) + icon_path
        except:
            self.message_error07()
    
    def set_init_window(self):
        # screenWidth = self.init_window_name.winfo_screenwidth()
        # screenHeight = self.init_window_name.winfo_screenheight()
        
        self.init_window_name.title("固定分区模拟实验 v1.0")
        self.init_window_name.geometry("1024x768+100+100")
        # self.init_window_name.iconbitmap("")

        self.window_title_label = Label(self.init_window_name, text="固定分区模拟实验 v1.0", font=tkFont.Font(size=30, weight=tkFont.BOLD))
        self.window_title_label.pack()
        self.data_showinfo_label = Label(self.init_window_name, text="分区表:", font=tkFont.Font(size=20, weight=tkFont.BOLD))
        self.data_showinfo_label.pack(side='top', anchor='w', expand='no')
        self.clear_showinfo_list = Button(self.init_window_name, text="导入分区文件", font=tkFont.Font(size=15), bd=3, command=self.data)
        self.clear_showinfo_list.place(x=875, y=45)
        self.clear_showinfo_list = Button(self.init_window_name, text="清空表格数据", font=tkFont.Font(size=15), bd=3, command=self.clear_up_list)
        self.clear_showinfo_list.place(x=875, y=425)
        
        s = ttk.Style()
        s.configure("Treeview", rowheight=30)
        s.configure("Treeview.Heading", font=(None, 12))
        # s.configure("Treeview.Heading", font=tkFont.Font(size=10, weight=tkFont.BOLD))
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

        # info = [
        #     ['1001', '李华', '男', '2014-01-25', '广东'],
        #     ['1002', '小米', '男', '2015-11-08', '深圳'],
        #     ['1003', '刘亮', '男', '2015-09-12', '福建'],
        #     ['1004', '白鸽', '女', '2016-04-01', '湖南'],
        #     ]
        # for index, data in enumerate(info):
        #     self.data_showinfo_treelist.insert('', END, values=data)

        self.drop_down_box_label = Label(self.init_window_name, text="创建或释放任务:", font=tkFont.Font(family='KaiTi', size=25, weight=tkFont.BOLD))
        self.drop_down_box_label.pack(side='top', anchor='w', expand='no', padx=5, pady=40)
        self.create_new_mission_label = Label(self.init_window_name, text="创建任务:", font=tkFont.Font(family='KaiTi', size=20))
        self.create_new_mission_label.place(x=160, y=520)
        self.drop_mission_label = Label(self.init_window_name, text="释放任务:", font=tkFont.Font(family='KaiTi', size=20))
        self.drop_mission_label.place(x=700, y=520)
        self.drop_mission_drop_label = Label(self.init_window_name, text="任务名称:", font=tkFont.Font(family='KaiTi', size=20))
        self.drop_mission_drop_label.place(x=630, y=595)
        self.name_drop_down_box = ttk.Combobox(self.init_window_name)
        self.name_drop_down_box["values"] = self.disk_table_list
        self.name_drop_down_box.place(x=760, y=595, height=30)
        # self.resourceA_drop_down_box = ttk.Combobox(self.init_window_name)
        # self.resourceA_drop_down_box["values"] = [i for i in range(self.free_list[0]+1)]
        # self.resourceA_drop_down_box.pack(side='left',anchor='n', expand='yes')
        # self.resourceB_drop_down_box = ttk.Combobox(self.init_window_name)
        # self.resourceB_drop_down_box["values"] = [i for i in range(self.free_list[1]+1)]
        # self.resourceB_drop_down_box.pack(side='left',anchor='n', expand='yes')
        # self.resourceC_drop_down_box = ttk.Combobox(self.init_window_name)
        # self.resourceC_drop_down_box["values"] = [i for i in range(self.free_list[2]+1)]
        # self.resourceC_drop_down_box.pack(side='left',anchor='n', expand='yes')
        self.sure_to_allocate_button = Button(self.init_window_name, text="确认创建任务", bd=3, font=tkFont.Font(family='KaiTi', size=20, weight=tkFont.BOLD))
        self.sure_to_allocate_button.place(x=125, y=665)
        self.sure_to_allocate_button = Button(self.init_window_name, text="确认释放任务", bd=3, font=tkFont.Font(family='KaiTi', size=20, weight=tkFont.BOLD))
        self.sure_to_allocate_button.place(x=670, y=665)

        self.name_entry_label = Label(self.init_window_name, text="任务名：", font=tkFont.Font(family='KaiTi', size=20))
        self.name_entry_label.place(x=95, y=570)
        self.size_entry_label = Label(self.init_window_name, text="大小：", font=tkFont.Font(family='KaiTi', size=20))
        self.size_entry_label.place(x=125, y=620)
        self.name_entry = Entry(self.init_window_name, highlightcolor='red', highlightthickness=1)
        self.name_entry.place(x=200, y=570, height=30)
        self.size_entry = Entry(self.init_window_name, highlightcolor='red', highlightthickness=1)
        self.size_entry.place(x=200, y=620, height=30)

    def data(self):
        def getinput(self, fpath):
            f = pd.read_csv(fpath)
            f = f.reset_index(drop=True)
            f = f.values.tolist()
            return f

        self.fpath = filedialog.askopenfilename(title=u'选择csv文件', initialdir=(os.path.expanduser(os.path.abspath(os.path.dirname(__file__)))))
        print('打开文件：', self.fpath)

        #未选择文件时的错误弹窗提示
        if self.fpath=='':
            self.message_error01()
            return 0
        
        try:
            f = getinput(self.fpath)
            self.ls = []
            self.n = 0
            for information in f:
                self.ls.append(disk_table(information))
                self.n+=1
            self.message_showinfo()
        except:
            self.message_error02()
            return 0

    def clear_up_list(self):
        # 删除数据
        children = self.data_showinfo_treelist.get_children()  # 获取所有的数据
        flag = messagebox.askyesno('提示信息', '确认删除所有数据?')
        if flag:
            for child in children:
                self.data_showinfo_treelist.delete(child)
    
    def message_showinfo(self):
        '''
        弹窗消息提示
        '''
        top = Tk()
        top.withdraw()  # ****实现主窗口隐藏
        top.update()  # *********需要update一下
        messagebox.showinfo(title="提示", message="打开文件成功！")
        top.destroy()

    def message_error01(self):
        '''
        错误警告弹窗(下同)
        '''
        top = Tk()
        top.withdraw()
        top.update()
        messagebox.showerror(title="错误01", message="打开文件失败，请检查文件路径是否正确！错误代码：01")
        top.destroy()

    def message_error02(self):
        top = Tk()
        top.withdraw()
        top.update()
        messagebox.showerror(title="错误02", message="发生意外错误，请检查文件内容是否符合规范！错误代码：02")
        top.destroy()

    def message_error03(self):
        top = Tk()
        top.withdraw()
        top.update()
        messagebox.showerror(title="错误03", message="发生了一个预期之外的错误！错误代码：03")
        top.destroy

    def message_error04(self):
        top = Tk()
        top.withdraw()
        top.update()
        messagebox.showerror(title="错误04", message="发生了一个预期之外的错误！错误代码：04")
        top.destroy()

    def message_error05(self):
        top = Tk()
        top.withdraw()
        top.update()
        messagebox.showerror(title="错误05", message="读取数据失败！尚未选择任何文件！错误代码：05")
        top.destroy()
    
    def message_error06(self):
        top = Tk()
        top.withdraw()
        top.update()
        messagebox.showerror(title="错误06", message="读取config.json失败，缺少文件./config/config.json  ！")

    def message_error07(self):
        top = Tk()
        top.withdraw()
        top.update()
        messagebox.showerror(title="错误07", message="加载图片失败，缺少文件./resources  ！")
        
    def message_error08(self):
        top = Tk()
        top.withdraw()
        top.update()
        messagebox.showerror(title="错误08", message="发生了一个意料之外的错误：加载模式选择信息错误！错误代码：08")


        

def gui_start():
        init_window = Tk()
        ZMJ_PORTAL = MY_GUI(init_window)
        ZMJ_PORTAL.set_init_window()
        init_window.mainloop()

gui_start()