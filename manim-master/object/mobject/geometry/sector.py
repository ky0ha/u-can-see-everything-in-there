from manimlib import *

# inner_radius	内圈半径，默认为1
# outer_radius	外圈半径，默认为2
# angle	外圈与内圈圆弧的角度，默认为90度
# start_angle	外圈与内圈起始的极径角度，默认为0度
# fill_opacity	填充颜色的透明度，默认为1
# stroke_width	轮廓线的粗细，默认为0
# color	颜色，默认为WHITE

class test(Scene):
    def construct(self):
        annularsector = AnnularSector(
            start_angle=0,
            angle=TAU / 4.,
            inner_radius=1,
            outer_radius=3,
            color=GREEN
        )
        sector = Sector(
            start_angle=0,
            angle=TAU / 4.,
            outer_radius=3,
            color=BLUE
        )
        
        annularsector.next_to(sector, DOWN)
        self.add(annularsector, sector)

if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")