from manimlib import *

# width	直角边的长度，默认为0.2
# angle	整体绕原点旋转的角度，默认为0

class test(Scene):
    def construct(self):
        e1 = Elbow(
            width=1,
            angle=0,
            color=GREEN
        )
        self.add(e1)


if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")