from manimlib import *

# radius	圆弧半径，默认为1
# arc_center	圆弧所在圆的圆心，默认为ORIGIN，也就是np.array([0, 0, 0])，即原点

class test(Scene):
    def construct(self):
        arc = Arc(
            start_angle=0,  # 起始位置角度
            angle=PI,   # 弧的角度，为180度
            radius=3,   # 半径为3个像素点
            arc_center=ORIGIN + LEFT    # 弧的中心坐标，为(0, 0)向左移动一个单位长度
        )
        
        # 轮廓颜色为淡绿色，粗细为5个像素点，透明度为0.9
        arc.set_stroke(color=GREEN_A, width=5, opacity=0.9)
        
        self.add(arc)

if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")