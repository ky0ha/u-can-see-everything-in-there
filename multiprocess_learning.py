from multiprocessing import Process
import os
def pro(n):
    child_pid = os.getpid()
    parent_pid = os.getpid()
    print("子进程id:{}; 父进程id:{}".format(child_pid, parent_pid))
    print("我是子进程，输出的结果为：{}".format(n*n))

if __name__=="__main__":
    print('主进程id:', os.getpid())
    for i in range(10):
        p = Process(target=pro, args=(1,))
        p.start()
        p.join()
    print("我是父进程")