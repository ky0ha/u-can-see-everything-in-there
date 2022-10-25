from mimetypes import init
from tkinter import *
from socket import *
from tkinter.ttk import Scrollbar

class MY_GUI:
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
        self.host = "127.0.0.1"
        self.post = 5000
    
    def set_init_window(self):
        self.init_window_name.title("客户端")

        self.message_entry = Entry(self.init_window_name, width=60, bd=3)
        self.message_entry.grid(column=0, row=0, padx=50, pady=50)
        self.start_listening_button = Button(self.init_window_name, text="发送消息", command=self.send_msg)
        self.start_listening_button.grid(column=1, row=0, padx=50, pady=50)
    
    def send_msg(self):
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.sendto(self.message_entry.get().encode('utf-8'), (self.host, self.post))
        self.message_entry.delete(0, END)
    
def gui_start():
    init_window = Tk()
    ZMJ_PORTAL = MY_GUI(init_window)
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()


gui_start()