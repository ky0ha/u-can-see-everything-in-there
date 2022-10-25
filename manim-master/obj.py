from manimlib import *

class Hello_World(Scene):
    def construct(self):
        checkmark = Checkmark()
        exmark = Exmark()
        exmark.next_to(checkmark, DOWN)
        self.add(checkmark, exmark)

if __name__ == '__main__':
    from os import system
    system("manimgl C:\\Users\\25315\\Desktop\\文件\\code\\onlyVS\\python\\manim-master\\obj.py Hello_World")