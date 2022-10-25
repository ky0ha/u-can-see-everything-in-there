from manimlib import *

class obj(Scene):
    def page1(self):
        label = Text("通过rbf网络拟合sin函数", font_size=80)

        self.play(Write(label))
        self.wait(2.5)
        self.play(FadeOut(label))

    def construct(self):
        self.page1()
        
        
        self.embed()

if __name__ == '__main__':
    from os import system
    system(f"manimgl {__file__} obj")