from manimlib import *

# vmob	需要绘制切线的VMobject形体对象
# alpha	指定切点到起点的长度比上vmob整体的轮廓线长度
# length	切线长度，默认为1
# d_alpha	近似切线的割线的两个点分别到切点的距离，默认为1e-6，值越小，得到的切线越精准

class test(Scene):
    def construct(self):
        circle = Circle(
            radius=3,
            color=BLUE,
            fill_opacity=0.5
        )
        line = TangentLine(
            vmob=circle,
            alpha=0.5,
            length=4
        )
        self.play(Write(circle))
        self.wait()
        self.play(Write(line))


if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")