from manimlib import *

# start	起点坐标，默认为np.array([-1, 0, 0])
# end	终点坐标，默认为np.array([1, 0, 0])
# fill_color	填充的颜色，默认为GREY_A
# fill_opacity	填充颜色的透明度，默认为1
# stroke_width	轮廓线的粗细，默认为0
# buff	收缩系数，默认为0.25
# thickness	厚度，默认为0.05
# tip_width_ratio	箭头长方体和头的宽度比，默认为5
# tip_angle	头三角形的夹角默认为60度

# 向量类Vector是Arrow的派生类，与Arrow不同的是

# Vector的起点默认是原点
# Vector的buff是0，也就是不会收缩
# Vector输入的代表方向的numpy数组可以是二维的，也可以是三维的，但是Arrow的start和end必须是三维的。

class test(Scene):
    def construct(self):
        a1 = Arrow(
            start=LEFT,
            end=RIGHT,
            fill_color=BLUE,
            fill_opacity=0.5,
            thickness=3,
            tip_width_ratio=5,
            tip_angle=PI / 2.
        )

        a2 = Arrow(
            start=LEFT * 2,
            end=RIGHT * 2,
            fill_color=GREEN,
            fill_opacity=0.8,
            thickness=3,
            tip_width_ratio=8,
            tip_angle=PI / 6.
        )

        self.add(a1)
        self.wait()
        self.play(ReplacementTransform(a1, a2))
        self.wait()

if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")