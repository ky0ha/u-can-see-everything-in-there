from tkinter import *
from socket import *
from tkinter.ttk import Scrollbar

class MY_GUI:
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
        self.host = ''
        self.port = 5000
        self.bufsize = 1024
        self.addr = (self.host, self.port)
    
    def set_init_window(self):
        self.init_window_name.title("服务端")
        
        self.text_frame = Frame(self.init_window_name)
        self.text_frame.pack(side=LEFT, padx=50, pady=50, expand=YES)
        
        self.ybar = Scrollbar(self.text_frame, orient='vertical')
        self.message_text = Text(self.text_frame, yscrollcommand=self.ybar.set)
        self.message_text.grid(row=0, column=0)
        self.ybar['command'] = self.message_text.yview
        self.ybar.grid(row=0, column=1, sticky='ns')
        
        self.start_listening_button = Button(self.init_window_name, text="启动监听", command=self.start_listenling)
        self.start_listening_button.pack(side=RIGHT, padx=50, pady=50, expand=YES)
    
    def start_listenling(self):
        udpServer = socket(AF_INET, SOCK_DGRAM)
        udpServer.setblocking(False)
        udpServer.bind(self.addr)
        # udpServer.settimeout(0.0)
        
        self.message_text.insert(END, "start listening...\n")
        while True:
            try:
                self.init_window_name.update()
                data, _ = udpServer.recvfrom(self.bufsize)
                data = data.decode(encoding='utf-8')
                self.message_text.insert(END, data+'\n')
            except:
                pass
    
def gui_start():
    init_window = Tk()
    ZMJ_PORTAL = MY_GUI(init_window)
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()


gui_start()