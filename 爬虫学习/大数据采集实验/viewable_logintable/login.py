import tkinter as tk
from tkinter import Variable, messagebox  # import this to fix messagebox error
import pickle
from tkinter.constants import END
import datetime, os

# 获取代码运行位置的绝对路径，以便于可以在不修改代码的情况下移植
root_path = os.path.abspath(os.path.dirname(__file__))

# 窗口标题和名称设定
window = tk.Tk()
window.title('Welcome to sky Python')
window.geometry('450x300')

# 自定义左上角程序图标
window.iconbitmap(root_path+'\\bitbug_favicon.ico')

# 设置欢迎图片
# welcome image
canvas = tk.Canvas(window, height=200, width=500)
# image_file = tk.PhotoImage(file='C:\\Users\\25315\\Desktop\\文件\\code\\onlyVS\\python\\爬虫学习\\大数据采集实验\\viewable_logintable\\welcome.gif')
image_file = tk.PhotoImage(file=root_path+'\\welcome.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# 设置输入框标题信息
# user information
user_name_label = tk.Label(window, text='User name: ')
user_name_label.place(x=50, y=150)
user_pwd_label = tk.Label(window, text='Password: ')
user_pwd_label.place(x=50, y=185)

# 设置输入框
var_usr_name = tk.StringVar()
# var_usr_name.set('admin')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=170, y=150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=170, y=185)

# 如果存在 cookie 即在上一次运行程序的时候勾选了 remember me 选框，则读取 cookie 信息，并自动填充用户名和密码
cookied = False
try:
    with open(root_path+'\\cookie', 'rb') as cookie:
        cookie_info = pickle.load(cookie)
        var_usr_name.set(cookie_info['user_name'])
        var_usr_pwd.set(cookie_info['password'])
    cookied = True
except:
    pass

# 初始化 cookie
with open(root_path+'\\cookie', 'wb') as cookie:
    pickle.dump({}, cookie)

# 设置显示/隐藏密码的勾选框
def show_password():
    flag = v.get()
    if flag:
        entry_usr_pwd.config(show='')
    else:
        entry_usr_pwd.config(show='*')
v = tk.IntVar()
show_pwd_checkbutton = tk.Checkbutton(window, variable=v, text='show password', command=show_password)
show_pwd_checkbutton.place(x=320, y=185)

# 设置 remember me 的勾选框
cookie_v = tk.IntVar()
remember_me_checkbutton = tk.Checkbutton(window, text='remember me', variable=cookie_v)
remember_me_checkbutton.place(x=260, y=210)
# 如果存在 cookie 信息，则继续默认勾选 remember me
if cookie_info!={}:
    cookie_v.set(1)

# 登录方法
def usr_login():
    # 获取输入框的用户名和密码
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()

    # 读取用户账号密码存储信息
    with open(root_path+'\\usrs_info.pickle', 'rb') as usr_file:
        usrs_info = pickle.load(usr_file)
        print(usrs_info, usr_name)
    # 如果输入的用户名存在，则进行登录判断和 cookie 的判断（cookie 判断和预期不符，已经注释掉了，预期是如果 cookie 的账号七天没有登录，则需要重新输入密码）
    if usr_name in usrs_info:
        # if cookied:
        #     if (datetime.datetime.now()-cookie_info['last_login']).hour>=23:
        #         messagebox.showwarning(message='this account has been remember but expired, coz over 7 days not login. pls re-entry password for this account!')
        #         entry_usr_pwd.delete(0, END)
        
        # 判断用户名和密码是否相符
        if usr_pwd == usrs_info[usr_name]:
            messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
            # 如果勾选了记住我，则写入 cookie
            if cookie_v.get():
                with open(root_path+'\\cookie', 'wb') as cookie:
                    pickle.dump({'user_name':usr_name, 'password':usr_pwd, 'last_login':datetime.datetime.now()}, cookie)
        else:
            messagebox.showerror(message='Error, your password is wrong, try again.')
    else:
        messagebox.showerror(message=f"user named '{usr_name}' not exists, pls check ur user name or sign with!")

def usr_sign_up():
    # user information
    # 初始化各个控件的信息，比如，清空输入的用户名，隐藏记住我勾选框
    entry_usr_name.delete(0, END)
    remember_me_checkbutton.place_forget()
    
    # 设置确认密码的输入框和标题
    confirm_pwd_label = tk.Label(window, text='Confrim Password: ')
    confirm_pwd_label.place(x=50, y=220)
    var_confirm_pwd = tk.StringVar()
    entry_confirm_pwd = tk.Entry(window, textvariable=var_confirm_pwd, show='*')
    entry_confirm_pwd.place(x=170, y=220)
    
    # 设置确认密码的密码隐藏/显示勾选框
    def show_confirm_password():
        flag = v_confirm.get()
        if flag:
            entry_confirm_pwd.config(show='')
        else:
            entry_confirm_pwd.config(show='*')
    
    v_confirm = tk.IntVar()
    show_conf_pwd_checkbutton = tk.Checkbutton(window, variable=v_confirm, text='show password', command=show_confirm_password)
    show_conf_pwd_checkbutton.place(x=320, y=220)
    
    # 设置返回按钮的方法
    def back():
        global btn_login, btn_sign_up
        # 初始化各个控件信息，并隐藏部分控件
        confirm_pwd_label.place_forget()
        show_conf_pwd_checkbutton.place_forget()
        entry_confirm_pwd.place_forget()
        btn_login.config(text='Login', command=usr_login)
        btn_sign_up.config(text='Sign up', command=usr_sign_up)
        remember_me_checkbutton.place(x=260, y=210)
        
        # btn_login = tk.Button(window, text='Login', command=usr_login)
        # btn_login.place(x=170, y=250)
        # btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
        # btn_sign_up.place(x=270, y=250)
    
    # 注册方法
    def register():
        # 获取用户名、密码、确认密码
        usr_name = var_usr_name.get()
        usr_pwd = var_usr_pwd.get()
        confirm_pwd = var_confirm_pwd.get()
        
        # 判断密码和确认密码是否相同
        if usr_pwd==confirm_pwd and usr_pwd!='':
            # 读取用户表信息
            try:
                with open(root_path+'\\usrs_info.pickle', 'rb') as r_usr_file:
                    usrs_info = pickle.load(r_usr_file)
            except:
                usrs_info = {}
            # 如果用户名已被注册，则终止本次注册表单的提交，并发出错误提示
            if usr_name in usrs_info:
                messagebox.showerror(message=f'account {usr_name} exists! cant sign one more time!')
                return
            # 写入新用户信息
            with open(root_path+'\\usrs_info.pickle', 'wb') as w_usr_file:
                usrs_info.update({f'{usr_name}': f'{usr_pwd}'})
                pickle.dump(usrs_info, w_usr_file)
            messagebox.showinfo(title='successful!', message='now u r registered successfully! pls back to login!')
            # 清空密码输入框
            entry_usr_pwd.delete(0, END)
            # 初始化各个控件为登录表单状态
            back()
        else:
            messagebox.showerror(message='may ur pwd not be allow or pwd not same as confirm pwd! pls try again!')
    
    global btn_login, btn_sign_up
    
    # 将各个控件状态初始化为注册表单状态
    btn_sign_up.config(text='Back', command=back)
    btn_login.config(text='Sign up', command=register)
    # entry_usr_name.delete(0, END)
    entry_usr_pwd.delete(0, END)
    # btn_login = tk.Button(window, text='Back', command=back)
    # btn_login.place(x=170, y=250)
    # btn_sign_up = tk.Button(window, text='Sign up', command=register)
    # btn_sign_up.place(x=270, y=250)

# 设置登录、注册按钮
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=170, y=250)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=250)

window.mainloop()
