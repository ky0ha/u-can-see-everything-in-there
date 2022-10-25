import qrcode, tkinter, os
import tkinter.font as tkFont
from tkinter.ttk import Separator, Combobox
import tkinter.messagebox
from PIL import Image, ImageTk
from tkinter import filedialog, dialog

class MY_GUI:
    # 设置类属性 _cnf 来存储在 tkinter 中修改的各类二维码参数的内容并直接作用于创建二维码
    _cnf = {
        "QR_cnf":{
            "version" : 1,
            "error_correction" : qrcode.constants.ERROR_CORRECT_L,
            "box_size" : 10,
            "border" : 4,},
        'image_cnf':{
            "fill_color" : 'black',
            "back_color" : 'white',}
        }
    
    # 初始化
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
    
    # 窗口控件设置
    def set_init_window(self):
        # 标题和窗口大小
        self.init_window_name.title("QR码生成")
        self.init_window_name.geometry("1024x768+100+100")
        
        # 主标题
        self.init_data_label = tkinter.Label(self.init_window_name, text='QR码生成器', font=tkFont.Font(family='KaiTi', size=50, weight=tkFont.BOLD))
        self.init_data_label.pack(pady=50)
        
        # 待转化的文本输入框
        self.text_input_box = tkinter.Frame(self.init_window_name)
        self.text_input_box.pack(pady=10)
        self.text_input_label = tkinter.Label(self.text_input_box, text='请输入要转化成QR码的字符串文本：', font=tkFont.Font(family='KaiTi', size=20))
        self.text_input_label.pack(side='left')
        self.text_input_entry = tkinter.Entry(self.text_input_box, border=4, width=60)
        self.text_input_entry.pack(side='right')
        
        # self.sep = Separator(self.init_window_name, orient='horizontal')
        # self.sep.pack(expand=True, padx=10, fill='x')
        
        # 高级选项、保存二维码、生成二维码三个按钮的设置
        self.button_box = tkinter.Frame(self.init_window_name)
        self.button_box.pack(pady=20, fill='x')
        self.anthor_model_button = tkinter.Button(self.button_box, text='高级选项', font=tkFont.Font(family='KaiTi', size=15), command=self.set_conf)
        self.anthor_model_button.pack(side='left', expand=True)
        self.anthor_model_button = tkinter.Button(self.button_box, text='保存二维码', font=tkFont.Font(family='KaiTi', size=15), command=self.save_image)
        self.anthor_model_button.pack(side='left', expand=True)
        self.start_button = tkinter.Button(self.button_box, text='生成二维码', font=tkFont.Font(family='KaiTi', size=15), command=self.start)
        self.start_button.pack(side='right', expand=True)

        # 二维码预览
        self.show_image_label = tkinter.Label(self.init_window_name, text='二维码预览', font=tkFont.Font(size=25))
        self.show_image_label.pack(pady=20)
        self.show_image = tkinter.Label(self.init_window_name, image=None)
        self.show_image.pack(expand=True)

    # 高级选项，设置二维码的生成参数，利用弹窗进行设置
    def set_conf(self):
        pw = popup_display(self.init_window_name)
        self.init_window_name.wait_window(pw)
        print(self._cnf)
    
    # 生成二维码
    def start(self):
        qr = qrcode.QRCode(**self._cnf['QR_cnf'])
        qr.make(fit=True)
        qr.add_data(self.text_input_entry.get())
        self.qrimg = qr.make_image(**self._cnf['image_cnf'])
        img = ImageTk.PhotoImage(self.qrimg)
        self.show_image.configure(image=img)
        self.show_image.image = img
    
    # 将生成的二维码保存到指定位置
    def save_image(self):
        path = filedialog.asksaveasfilename(title=u'保存文件', initialdir=(os.path.expanduser(os.path.abspath(os.path.dirname(__file__)))), defaultextension='.png', initialfile='QR_code', filetypes=(("PNG 图片文件", "*.png"), ("所有文件", "*.*")))
        self.qrimg.save(path)

class popup_display(tkinter.Toplevel):
    # 弹窗类，同来修改设置信息
    # 初始化，并集成父类，便于在子类对父类属性进行修改
    def __init__(self, parent):
        super().__init__()
        self.init_window_name = self
        self.parents = MY_GUI
        self.set_init_window()
    
    # 窗口设置
    def set_init_window(self):
        # 标题和窗口大小
        self.init_window_name.title("开发者选项")
        self.init_window_name.geometry('800x600+200+200')
        
        # 参数说明信息部分
        self.tip_info_label = tkinter.LabelFrame(self.init_window_name, font=tkFont.Font(family='KaiTi', size=12))
        self.tip_info_label.pack(pady=10)
        self.version_info = tkinter.Label(self.tip_info_label, text='version：值为1~40的整数，控制二维码的大小（最小值是1，是个12×12的矩阵）。 如果想让程序自动确定，将值设置为 0， 默认为1')
        self.version_info.pack(padx=10, pady=2.5)
        self.error_correction_info = tkinter.Label(self.tip_info_label, text='error_correction：控制二维码的错误纠正功能。(低容错有7%容错率，中容错有15%，高容错有30%， 默认为低容错')
        self.error_correction_info.pack(padx=10, pady=2.5)
        self.fill_color_info = tkinter.Label(self.tip_info_label, text='fill_color_info：二维码的前景色，二维码本身的颜色， 默认为黑色')
        self.fill_color_info.pack(padx=10, pady=2.5)
        self.back_color = tkinter.Label(self.tip_info_label, text='back_color：二维码的背景色， 默认为白色')
        self.back_color.pack(padx=10, pady=2.5)
        
        # version 参数设置部分
        self.version_frame = tkinter.Frame(self.init_window_name)
        self.version_frame.pack(expand=True)
        # self.version = Combobox(self.init_window_name, state='readonly')
        # self.version['values'] = ['line', 'oval', 'arc', 'rect']
        # self.version.current(3)
        self.version_label = tkinter.Label(self.version_frame, text='version : ')
        self.version_label.pack(side='left')
        self.version_entry = tkinter.Entry(self.version_frame)
        self.version_entry.insert(0, '1')
        self.version_entry.pack(side='right')
        
        # 容错率参数设置部分
        self.error_correction_frame = tkinter.Frame(self.init_window_name)
        self.error_correction_frame.pack(expand=True)
        self.error_correction_label = tkinter.Label(self.error_correction_frame, text='容错率 ： ')
        self.error_correction_label.pack(side='left')
        self.error_correction_combobox = Combobox(self.error_correction_frame, state='readonly')
        self.error_correction_combobox['values'] = ['低容错', '中容错', '高容错']
        self.error_correction_combobox.current(0)
        self.error_correction_combobox.pack(side='right')
        
        # 前景色参数设置部分
        self.fill_color_frame = tkinter.Frame(self.init_window_name)
        self.fill_color_frame.pack(expand=True)
        self.fill_color_label = tkinter.Label(self.fill_color_frame, text='二维码颜色 ： ')
        self.fill_color_label.pack(side='left')
        self.fill_color_combobox = Combobox(self.fill_color_frame, state='readonly')
        self.fill_color_combobox['values'] = ['红', '黑', '蓝', '黄', '紫', '粉', '绿', '白']
        self.fill_color_combobox.current(1)
        self.fill_color_combobox.pack(side='right')
        
        # 背景色参数设置部分
        self.back_color_frame = tkinter.Frame(self.init_window_name)
        self.back_color_frame.pack(expand=True)
        self.back_color_label = tkinter.Label(self.back_color_frame, text='背景颜色颜色 ： ')
        self.back_color_label.pack(side='left')
        self.back_color_combobox = Combobox(self.back_color_frame, state='readonly')
        self.back_color_combobox['values'] = ['红', '黑', '蓝', '黄', '紫', '粉', '绿', '白']
        self.back_color_combobox.current(7)
        self.back_color_combobox.pack(side='right')
        
        # 确认修改配置的按钮
        self.confrim_button = tkinter.Button(self.init_window_name, text='确认设置', command=self.confrim)
        self.confrim_button.pack(expand=True)
        
        # 用来凑位置
        self.empty_label = tkinter.Label(self.init_window_name, font=tkFont.Font(size=40)).pack(expand=True)

    def confrim(self):
        # 确认按钮调用函数
        # version 的设置
        version = self.version_entry.get()
        if version.isdecimal():
            version = int(version)
            if version==0:
                self.parents._cnf['QR_cnf']['version'] = None
            elif version<=40 and version>0:
                self.parents._cnf['QR_cnf']['version'] = version
            else:
                print(f"version out of range [0, 40] : {version}")
        else:
            print('version is not decimal')
        
        # 容错率的设置
        if self.error_correction_combobox.get()=='低容错':
            self.parents._cnf['QR_cnf']['error_correction'] = qrcode.constants.ERROR_CORRECT_L
        elif self.error_correction_combobox.get()=='中容错':
            self.parents._cnf['QR_cnf']['error_correction'] = qrcode.constants.ERROR_CORRECT_M
        elif self.error_correction_combobox.get()=='高容错':
            self.parents._cnf['QR_cnf']['error_correction'] = qrcode.constants.ERROR_CORRECT_H
        else:
            print(self.error_correction_combobox.get())
        
        # 前景色和背景色设置
        colorbet = {'红':'red', '黑':'black', '蓝':'blue', '黄':'yellow', '紫':'purple', '粉':'pink', '绿':'green', '白':'white'}
        fill_color = self.fill_color_combobox.get()
        back_color = self.back_color_combobox.get()
        if fill_color in colorbet and back_color in colorbet:
            self.parents._cnf['image_cnf']['fill_color'] = colorbet[fill_color]
            self.parents._cnf['image_cnf']['back_color'] = colorbet[back_color]
        
        # 弹出设置成功的反馈框
        tkinter.messagebox.showinfo('成功', '成功修改配置！')
        
        # 摧毁弹窗
        self.init_window_name.destroy()
        return

# 运行窗口
def gui_start():
    init_window = tkinter.Tk()
    ZMJ_PORTAL = MY_GUI(init_window)
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()

gui_start()