from manimlib import *

class test(Scene):
    def construct(self):
        bubble = Bubble(
            file_name="C:\\Users\\25315\\Desktop\\文件\\code\\onlyVS\\images\\bubble.svg",
            fill_opacity=0,
            stroke_color=WHITE,
            stroke_width=5
        )
        self.add(bubble)

if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")