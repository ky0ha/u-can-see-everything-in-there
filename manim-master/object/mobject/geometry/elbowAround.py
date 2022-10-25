from manimlib import *

# width	直角边的长度，默认为0.2
# angle	整体绕原点旋转的角度，默认为0

class test(Scene):
    def construct(self):
        colors = [BLUE, RED, GREEN, GREY_A]
        for i in range(4):
            self.add(Elbow(
                width=3.,
                angle=i * PI / 2.,
                color=colors[i]
            ))


if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")