from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os, winreg, re


class MY_GUI:
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    def get_desktop(self):
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders')
        self.desktop_path = winreg.QueryValueEx(key, 'Desktop')[0]

    def set_init_window(self):
        self.init_window_name.title('歌词处理')
        self.init_window_name.geometry('800x600')
        self.get_desktop()

        s = StringVar()
        s.set(f'处理后歌词文件默认保存在 {self.desktop_path}\\歌词\\ 文件夹内。')
        self.init_title_label = Label(self.init_window_name, textvariable=s)
        self.init_title_label.pack(expand=YES)
        self.choice_lyric_files_button = Button(self.init_window_name, text='选择歌词文件', command=self.choice_lyric_files)
        self.choice_lyric_files_button.pack(expand=YES)
        self.start_button = Button(self.init_window_name, text='开始处理', command=self.start)

    def choice_lyric_files(self):
        self.path_list = askopenfilenames(title='选择歌词文件', 
                                initialdir=(os.path.expanduser(os.path.abspath(os.path.dirname(__file__)))), 
                                filetypes=[('lyric source file', '*.lrc')])
        if self.path_list == '':
            showerror(title='错误', message='未选择任何文件！')
        else:
            showinfo(title='成功', message='文件选择成功，点击开始处理按钮进行歌词处理。')
            self.start_button.pack(expand=YES)
        print(self.path_list)

    def start(self):
        for path in self.path_list:
            file_name = path.split('/')[-1]
            lyric = {}
            with open(path, 'r', encoding='utf-8') as f:
                text = f.readlines()
                for i in text:
                    index = re.search(r'\d{2}:\d{2}.\d*', i)
                    if index!=None:
                        left, right = index.span()
                        if lyric.get(i[left:right])==None:
                            lyric[i[left:right]] = [i[right+1:].replace('\n', '')]
                        else:
                            lyric[i[left:right]].append(i[right+1:].replace('\n', ''))
            
            if not os.path.exists(f'{self.desktop_path}/歌词'):
                os.mkdir(f'{self.desktop_path}/歌词')
            with open(f'{self.desktop_path}/歌词/{file_name}', 'w', encoding='utf-8') as f:
                for key, value in lyric.items():
                    f.write(f'[{key}]{value[0]}\n')
                    try:
                        f.write(f'{value[1]}\n')
                    except IndexError:
                        continue
            
            showinfo(title='成功', message='处理成功！文件保存在 桌面-歌词 文件夹内。')
            self.start_button.pack_forget()


def gui_start():
    init_window = Tk()
    ZMJ_PORTAL = MY_GUI(init_window)
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()


gui_start()
