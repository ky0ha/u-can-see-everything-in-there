from manimlib import *

class test(Scene):
    def construct(self):
        points = [
            np.array([-2, 1, 0]),
            np.array([-1, 0, 0]),
            np.array([1, 0, 0]),
            np.array([2, 1, 0])
        ]
        names = ["a0", "h0", "h1", "a1"]
        
        # 创建坐标轴
        axes = Axes(
            x_range=(-2, 2),
            y_range=(0, 1.2)
        )
        axes.add_coordinate_labels()
        self.play(Write(axes))
        # 将三阶贝塞尔曲线的三条外边画出来，并加上*names的标注
        for i, _ in enumerate(points):
            if i < len(points) - 1:
                text = self.write_word(names[i], axes.c2p(points[i][0], points[i][1]))
                self.play(
                    ShowCreation(axes.get_graph(
                        function=self.get_line_func(points[i], points[i + 1]),
                        x_range=(points[i][0], points[i + 1][0]),
                        color=BLUE)),
                    Write(text)
                )

        text = self.write_word(names[-1], axes.c2p(points[-1][0], points[-1][1]))
        self.play(Write(text))

        group = VGroup(*self.get_mobjects())

        # 改变坐标轴的位置
        self.play(group.animate.scale(0.6).to_corner(UL), run_time=2)

        # 设定变化参数t，初值为0
        t = ValueTracker(0)
        # 显示数字
        formula = Tex(r"B_n(t)=\sum_{k=0}^n\binom{n}{k}t^k(1-t)^{n-k}P_k", font_size=56)
        text, number = label = VGroup(
            Tex("t = ", font_size=64),
            DecimalNumber(0, num_decimal_places=2, include_sign=False)
        )
        label.arrange(RIGHT)
        formula.move_to(np.array([0, -2, 0]))
        label.move_to(np.array([3, 2, 0]))
        f_always(number.set_value, t.get_value)
        self.play(FadeIn(text), FadeIn(number), Write(formula))

        # 跟踪的点
        point = Dot(axes.c2p(points[0][0], points[0][1]), color=RED)
        # 跟踪的线
        l1 = Line(
            start=axes.c2p(points[0][0], points[0][1]),
            end=axes.c2p(points[1][0], points[1][1]),
            color=RED_B
        )

        l2 = Line(
            start=axes.c2p(points[1][0], points[1][1]),
            end=axes.c2p(points[2][0], points[2][1]),
            color=RED_B
        )

        l3 = Line(
            start=axes.c2p(points[0][0], points[0][1]),
            end=axes.c2p(points[1][0], points[1][1]),
            color=GREEN
        )

        # 创建TracedPath对象，它代表点的中心出现过的地方的集合
        tracer = TracedPath(point.get_center)
        tracer.set_stroke(YELLOW, width=3, opacity=1)
        self.play(ShowCreation(tracer))
        
        self.play(Write(point), Write(l1), Write(l2), Write(l3))
        
        # 增加updater，画出Dot的轨迹
        point.add_updater(self.bezier_curve(axes, t, *points))
        l1.add_updater(self.updater1(axes, t, points[0], points[1], points[2]))
        l2.add_updater(self.updater1(axes, t, points[1], points[2], points[3]))
        l3.add_updater(self.updater2(axes, t, *points))

        self.play(t.animate.set_value(1), run_time=5)
        

    def write_word(self, words, position=ORIGIN):
        t = Tex(words, color=GREEN_B)
        t.move_to(position)
        return t

    def get_line_func(self, point1, point2):    # 两点确定的直线方程
        if point1[0] == point2[0]:
            return lambda x : point1[0]
        else:
            k = (point2[1] - point1[1]) / (point2[0] - point1[0])
            b = point1[1] - k * point1[0]
            return lambda x : k * x + b
    
    def bezier_curve(self, axes : Axes, t : ValueTracker, a0, h0, h1, a1):
        bf = lambda x : a0 * pow(1 - x, 3) + 3 * h0 * x * (1 - x) * (1 - x) + 3 * h1 * x * x * (1 - x) + a1 * pow(x, 3)
        def func(point : Dot):      # 传入updater的闭包函数
            p = bf(t.get_value())
            point.move_to(axes.c2p(p[0], p[1]))
        return func
    
    def updater1(self, axes : Axes, t : ValueTracker, p1, p2, p3):
        def func(line : Line):
            x = t.get_value()
            s1 = (1 - x) * p1 + x * p2 
            s2 = (1 - x) * p2 + x * p3 
            line.set_points_by_ends(
                start=axes.c2p(s1[0], s1[1]),
                end=axes.c2p(s2[0], s2[1])
            )
            return line
        return func 
    
    def updater2(self, axes : Axes, t : ValueTracker, a0, h0, h1, a1):
        def func(line : Line):
            x = t.get_value()
            s1 = (1 - x) * (1 - x) * a0 + 2 * x * (1 - x) * h0 + x * x * h1
            s2 = (1 - x) * (1 - x) * h0 + 2 * x * (1 - x) * h1 + x * x * a1
            line.set_points_by_ends(
                start=axes.c2p(s1[0], s1[1]),
                end=axes.c2p(s2[0], s2[1])
            )
            return line
        return func 

if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")