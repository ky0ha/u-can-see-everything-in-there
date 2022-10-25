from manimlib import *

# start	圆弧起始点
# end	圆弧终点
# angle	圆弧的角度

class test(Scene):
    def construct(self):
        arrow = CurvedArrow(
            start_point=UP * 2,
            end_point=DOWN * 2,
            angle=TAU / 4.             # 45度
        )
        arrow.set_color(color=RED)

        d_arrow = CurvedDoubleArrow(
            start_point=UP * 2,
            end_point=DOWN * 2,
            angle=TAU / 4.             # 45度
        )
        d_arrow.set_color(color=GREEN)
        d_arrow.next_to(arrow, RIGHT)   # 双头箭头在单箭头的右边

        self.add(arrow, d_arrow)

if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")