from manimlib import *

# inner_radius	内环半径，默认为1
# outer_radius	外环半径，默认为2
# fill_opacity	填充色透明度，默认为1
# stroke_width	轮廓线粗细，默认为0
# color	颜色，默认为0

class test(Scene):
    def construct(self):
        annulus = Annulus(
            inner_radius=2,
            outer_radius=3,
            color=BLUE,
            fill_opacity=0.8
        )
        self.add(annulus)

if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")