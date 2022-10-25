import tkinter as tk
import random
from tkinter import ttk
from tkinter.font import Font
import os

# 获取代码运行位置的绝对路径，以便于可以在不修改代码的情况下移植
root_path = os.path.abspath(os.path.dirname(__file__))

window = tk.Tk()
window.title('my window')
##窗口尺寸
window.geometry('1024x768')

# 自定义左上角程序图标
window.iconbitmap(root_path+'\\bitbug_favicon.ico')

#新建画布
canvas=tk.Canvas(window,bg='light blue',height=570,width=1024)

title_label = tk.Label(window, text='使用键盘方向键或者按钮控制选中的图形进行移动，使用鼠标右键解除输入框的选中', font=Font(family='KaiTi', size=16))
title_label.pack(padx=3, pady=3)

#画线
# x0,y0,x1,y1=50,50,80,80
x0, y0, x1, y1 = (random.randint(100, 570) for _ in range(4))
line=canvas.create_line(x0,y0,x1,y1)
#画⚪
x0 = random.randint(0, 570)
oval=canvas.create_oval(x0,x0,x0+50,x0+50,fill='red')
#画一个扇形
x0 = random.randint(0, 570)
arc = canvas.create_arc(x0+50, x0+50, x0, x0, start=0, extent=90)
#画一个矩形
x0 = random.randint(0, 570)
rect = canvas.create_rectangle(x0, x0-70, x0+50, x0-70+50)   
canvas.pack()

target_from_menu = rect
#创建菜单
menubar=tk.Menu(window)
menuitem = tk.Menu(menubar)
menubar.add_cascade(label='Select', menu=menuitem)
menuitem.add_command(label='line')
menuitem.add_command(label='oval')
menuitem.add_command(label='arc')
menuitem.add_command(label='rect')
window.config(menu=menubar)

# 移动方向设置
UP, DOWN, LEFT, RIGHT = 'up', 'down', 'left', 'right'

# 移动动作函数
def moveup(event=None):
    global canvas
    target = eval(choice_item_combobox.get())
    step = int(select_step_entry.get())
    canvas.move(target,0,-step)
    # print(event)
def movedown(event=None):
    target = eval(choice_item_combobox.get())
    step = int(select_step_entry.get())
    canvas.move(target,0,step)
def moveleft(event=None):
    target = eval(choice_item_combobox.get())
    step = int(select_step_entry.get())
    canvas.move(target,-step,0)
    # print(event)
def moveright(event=None):
    target = eval(choice_item_combobox.get())
    step = int(select_step_entry.get())
    canvas.move(target,step,0)
# def moveleftup(event=None):
#     global canvas
#     target = eval(choice_item_combobox.get())
#     step = int(select_step_entry.get())
#     canvas.move(target,-step,-step)
# def moverightup(event=None):
#     global canvas
#     target = eval(choice_item_combobox.get())
#     step = int(select_step_entry.get())
#     canvas.move(target,step,-step)
# def moveleftdown(event=None):
#     global canvas
#     target = eval(choice_item_combobox.get())
#     step = int(select_step_entry.get())
#     canvas.move(target,-step,step)
# def moverightdown(event=None):
#     global canvas
#     target = eval(choice_item_combobox.get())
#     step = int(select_step_entry.get())
#     canvas.move(target,step,step)

# 创建 frame 容器用以容纳选择图形的下拉框和步长的输入框
select_frame = tk.Frame(window)
select_frame.pack(side='left', expand='yes')

# 选择图形的下拉框
choice_item_label = tk.Label(select_frame, text='选择要移动的框体：', font=Font(family='KaiTi', size=16))
choice_item_label.pack(side='top', anchor='c', expand='no', padx=5, pady=4)
choice_item_combobox = ttk.Combobox(select_frame, state='readonly')
choice_item_combobox['values'] = ['line', 'oval', 'arc', 'rect']
choice_item_combobox.current(3)
choice_item_combobox.pack(side='top', anchor='c', expand='no', padx=5, pady=4)

# 步长输入框
select_step_label = tk.Label(select_frame, text='输入单次移动的步长：', font=Font(family='KaiTi', size=16))
select_step_label.pack(side='top', anchor='c', expand='no', padx=5, pady=4)
select_step_entry = tk.Entry(select_frame, highlightcolor='blue', highlightthickness=1)
select_step_entry.insert(0, '5')
select_step_entry.pack(side='top', anchor='c', expand='no', padx=5, pady=4)

# 创建 frame 容器用以通过 grid 布局以九宫格的形式对四个方向按钮进行布局
move_frame = tk.Frame(window)
move_frame.pack(side='left', expand='yes')
bl=tk.Button(move_frame,text='←',height=2,width=5,command=moveleft)
bl.grid(column=0, row=1)
bu=tk.Button(move_frame,text='↑',height=2,width=5,command=moveup)
bu.grid(column=1, row=0)
bd=tk.Button(move_frame,text='↓',height=2,width=5,command=movedown)
bd.grid(column=1, row=2)
br=tk.Button(move_frame,text='→',height=2,width=5,command=moveright)
br.grid(column=2, row=1)

# 键盘监听事件的绑定
window.bind('<Up>', moveup)
window.bind('<Down>', movedown)
window.bind('<Left>', moveleft)
window.bind('<Right>', moveright)
# window.bind('<Up-Right>', moverightup)
# window.bind('<Down-Right>', moverightdown)
# window.bind('<Up-Left>', moveleftup)
# window.bind('<Down-Left>', moveleftdown)

# 右键强制失焦
def un_focus(event=None):
    window.focus_force()
window.bind('<Button-3>', un_focus)

##显示出来
window.mainloop()