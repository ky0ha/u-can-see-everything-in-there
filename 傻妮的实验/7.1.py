from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os


class MY_GUI:
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    def set_init_window(self):
        self.init_window_name.title("选择文件")

        self.top_frame = Frame(self.init_window_name)
        self.top_frame.pack(side=TOP, fill=X, pady=50, padx=50, expand=YES)

        self.path_value = StringVar()
        self.pic_path_shower_entry = Entry(
            self.top_frame,
            bg='white',
            width=60,
            state=DISABLED,
            textvariable=self.path_value,
            background="white"
        )
        self.pic_path_shower_entry.grid(column=0, row=0)

        self.select_dir_button = Button(
            self.top_frame, text="选择文件夹", command=self.select_file)
        self.select_dir_button.grid(column=1, row=0, padx=40, columnspan=1)
        self.search_png_button = Button(
            self.top_frame, text="检索png文件", command=self.search_file)
        self.search_png_button.grid(column=1, row=1, padx=40, pady=10, columnspan=1)

        self.tips_label = Label(self.init_window_name,
                                text='点击某一行可以直接复制该行的全路径到剪切板')
        self.tips_label.pack()

        self.treeview_frame = Frame(self.init_window_name)
        self.treeview_frame.pack(side="bottom", expand=YES, pady=40)

        self.ybar = Scrollbar(self.treeview_frame, orient='vertical')
        s = ttk.Style()
        s.configure("Treeview", rowheight=20)
        s.configure("Treeview.Heading", font=(None, 12))
        columns = ("file_name", "full_path")
        self.search_png_shower_treelist = ttk.Treeview(
            self.treeview_frame,
            show='headings',
            columns=columns,
            yscrollcommand=self.ybar.set,
            selectmod=BROWSE
        )
        self.search_png_shower_treelist.column("file_name", width=150, anchor='center')
        self.search_png_shower_treelist.column("full_path", width=500, anchor='center')
        self.search_png_shower_treelist.heading("file_name", text="文件名")
        self.search_png_shower_treelist.heading("full_path", text="全路径")
        self.search_png_shower_treelist.grid(row=0, column=0)
        self.ybar['command'] = self.search_png_shower_treelist.yview
        self.ybar.grid(row=0, column=1, sticky='ns')

        self.search_png_shower_treelist.bind(
            '<ButtonRelease-1>',
            lambda event: self.treeviewclick(event, self.search_png_shower_treelist)
        )

    def select_file(self):
        self.path = filedialog.askdirectory(title=u'选择文件夹', initialdir=r'C:\\')
        self.path_value.set(self.path)

    def search_file(self):
        self.result = []
        self.found(self.path)
        if not os.path.exists(r"C:\pngsdir"):
            os.makedirs(r"C:\pngsdir")
        f = open(r'C:\pngsdir\png.txt', 'w', encoding='utf-8')
        for i in self.result:
            self.search_png_shower_treelist.insert('', END, values=i)
            f.write(i[-1]+'\n')
        

    def found(self, path):
        file_list = os.listdir(path)
        for i in file_list:
            if os.path.isdir(path+'\\'+i):
                self.found(path+'\\'+i)
            elif os.path.isfile(path+'\\'+i):
                if i.split('.')[-1] == 'png':
                    self.result.append([i, path+'\\'+i])

    def treeviewclick(self, event, tree):
        self.init_window_name.clipboard_clear()
        strs = ""
        for item in tree.selection():
            item_text = tree.item(item, "values")
            strs += item_text[1]+"\n"  # 获取本行的第一列的数据
        self.init_window_name.clipboard_append(strs)


def gui_start():
    init_window = Tk()
    ZMJ_PORTAL = MY_GUI(init_window)
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()


gui_start()
