from manimlib import *

class font(Scene):
    def construct(self):
        text1 = Text("This is ITALIC", slant=ITALIC)    # 意大利斜体
        text2 = Text("This is BOLD", weight=BOLD)       # 粗体
        text3 = Text("This is OBLIQUE", slant=OBLIQUE)  # 斜体
        text2.next_to(text1, DOWN)
        text3.next_to(text2, DOWN)
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.wait()

if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} font")