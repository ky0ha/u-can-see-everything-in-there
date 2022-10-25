from manimlib import *

# start	圆弧起始点
# end	圆弧终点
# angle	圆弧的角度

class test(Scene):
    def construct(self):
        arc = ArcBetweenPoints(
            start=np.array([0, 2, 0]),
            end=np.array([0, -2, 0]),
            angle=PI,
            fill_color=BLUE_A,          # 填充颜色
            stroke_color=GREEN,         # 轮廓颜色
            stroke_width=8,             # 轮廓粗细
            gloss=1.0                   # 反光度
        )
        self.add(arc)

if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")