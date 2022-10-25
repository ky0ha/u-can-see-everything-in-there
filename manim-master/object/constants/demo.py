from manimlib import *

class test(Scene):
    def construct(self):
        c1 = Circle()                             # 创建第一个圆形对象
        c1.set_stroke(color=RED, width=4)         # 设置c1的边属性
        c1.set_fill(color=YELLOW, opacity=0.5)    # 设置c1的填充属性

        c2 = Circle()                             # 创建第二个圆形对象
        c2.set_stroke(color=PURPLE)               # 设置c2的边属性
        c2.set_fill(color=BLUE, opacity=0.5)      # 设置c2的填充属性

        c1.next_to(c2, LEFT)                      # c1在c2的左边

        self.play(Write(c1))                      # 为c1创建Write动画，并播放
        self.play(Write(c2))                      # 为c2创建Write动画，并播放

if __name__ == '__main__':
    from os import system
    system(f"manimgl {__file__} test")