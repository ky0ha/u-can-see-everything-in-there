from manimlib import *

class test(Scene):
    def construct(self):
        arc1 = Arc(
            start_angle=0,           # 启示位置的角度
            angle=PI / 1.5,          # 弧的角度，为120度
            radius=3,                # 半径为3个像素点
            arc_center=ORIGIN + LEFT # 弧的中心的坐标，为(0,0)向左移动一个单位长度
        )
        arc1.set_stroke(color=GREEN_A, width=5, opacity=0.9)     # 轮廓颜色为淡绿色，粗细为5个像素点，透明度为0.9
        arc1.set_fill(color=GREEN_D, opacity=0.8)

        arc2 = arc1.copy()                                      # 拷贝一份和arc1完全一样的圆弧对象
        arc2.angle = PI                                         # 弧度重新设置成180度
        arc2.set_fill(color=BLUE)                               # 设置颜色
        arc2.init_points()                                      # 重新渲染
        arc2.move_arc_center_to(ORIGIN)                         # 位置重新设置为原点

        self.play(Write(arc1))
        self.wait()
        self.play(ReplacementTransform(arc1, arc2))

if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")