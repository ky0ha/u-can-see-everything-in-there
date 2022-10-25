from manimlib import *

class test(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(YELLOW, opacity=0.5)
        circle.set_stroke(BLUE)
        square = Square()
        square.set_fill(BLUE, opacity=0.7)
        square.set_stroke(RED)

        self.play(FadeIn(circle))

        # 进入交互模式
        self.embed()

if __name__ == '__main__':
    from os import system
    system(f"manimgl {__file__} test")