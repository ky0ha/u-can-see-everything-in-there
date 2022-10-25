from manimlib import *
from math import sin, cos

class heart(Scene):
    CONFIG = {
        # 'circle_color': '#1514EA', # color blue
        # 'line_color': '#E71905', # color red
        'circle_color': BLUE, # color blue
        'line_color': RED, # color red
        'node_color': PINK,
        'line_width': 3,
        'node_num': 200,

        'show_node_id': True,

        'circle_r': 3.4,
        'node_r': 0.032,

        'circle_loc': LEFT * 2.5 + UP * 0.1,
    }
    
    def create_all(self):
    
        n = self.node_num
        self.circle = Circle(radius=self.circle_r, color=self.circle_color, stroke_width=2 * self.line_width).move_to(self.circle_loc)

        self.node_group = VGroup()
        # self.node_id = VGroup()
        self.line_group = VGroup()
        delta_a = TAU / n

        for i in range(n):
            vector_i = np.array([-np.sin(delta_a * (i + 1) + TAU / 2), np.cos(delta_a * (i + 1) + TAU / 2), 0]) * self.circle_r
            node_i = Circle(radius=self.node_r, color=self.node_color, fill_color=self.node_color, fill_opacity=1).move_to(self.circle.get_center() + vector_i)
            # if n%10==0:
                # print(n)
            self.node_group.add(node_i)
            # if self.show_node_id:
                # text_i = Text('%d' % (i + 1), color=self.node_color).scale(0.36).move_to(self.circle.get_center() + vector_i * 1.06)
                # self.node_id.add(text_i)

        for i in range(1, n+1):
            # if n%10==0:
            #     print(n)
            line_i = Line(self.node_group[i - 1].get_center(), self.node_group[(2 * i - 1) % n + 1 - 1].get_center(),
                          color=self.line_color, stroke_width=self.line_width)
            self.line_group.add(line_i)

        self.all_objects = VGroup(self.circle, self.node_group, self.line_group)
    
    def construct(self):
        def Cardioid(self=self):
            axes = Axes()
            func = ParametricCurve(
                lambda t: np.array([
                    2*sin(t)-sin(2*t),
                    2*cos(t)-cos(2*t),
                    0
                ])+axes.c2p(0, 0),
                t_range=[0, 2*PI],
                color=RED
            )
            t = Tex(r"x^{2}+y^{2}+ax = a\sqrt{x^{2}+y^{2}}").to_edge(UR)
            t1 = Text("笛卡尔心形线")
            t2 = Text("实在是太难搞了这个东西，仓促之下显得并不亮眼，但是爱你哦~月月~")
            t3 = Text("虽然难以入眼，但是这是我能给你的很特别的东西").next_to(t2, DOWN)
            self.play(Write(t1))
            self.wait(1)
            self.play(ReplacementTransform(t1, t2))
            self.play(Write(t3))
            self.wait(1)
            self.play(FadeOut(VGroup(t2, t3)))
            self.wait(1)
            self.play(Write(t))
            self.play(Write(axes))
            self.play(ShowCreation(func), run_time=5)
            self.play(ApplyMethod(func.set_fill, color=RED, opacity=0.6))
            # self.embed()
            self.play(FadeOut(VGroup(axes, func, t)))
        
        Cardioid()
        
        def Cardioid_by_Line(self=self):
            # bg_rect = Rectangle(fill_color=self.bg_color, fill_opacity=1).scale(20)
            # self.add(bg_rect)
            # self.wait(0.25)

            # self.anim()

            self.create_all()
            t1 = Text("将第i个点和第2i个点连接").to_edge(UR)
            t2 = Text("2i大于n对n取余").next_to(t1, DOWN)
            self.play(Write(VGroup(t1, t2)))
            self.wait(1)
            self.play(FadeOut(VGroup(t1, t2)))
            self.play(ShowCreation(self.circle), run_time=1.25)
            self.wait(0.4)

            # for i in range(self.node_num):
            #     self.play(FadeIn(self.node_group[i]), run_time=0.002)
            #     # if self.show_node_id:
            #     #     self.play(Write(self.node_id[i]), run_time=0.002)
            # self.wait()

            for i in range(self.node_num):
                self.play(ShowCreation(self.line_group[i]), run_time=0.002)
                # self.wait(0.0)
            
            # self.play(ReplacementTransform(self.all_objects))
            
            # self.embed()
        
        Cardioid_by_Line()
        
class Curve_by_RotatingVectors(Scene):
    
    CONFIG = {
        # 'bg_color': WHITE,
        'circle_color': BLUE,
        'circle_num': 14,
        'circle_width': 1.,
        'curve_color': RED_B,
        'curve_width': 4,

        'scale_all': 5,

        'arrow_color': PINK,

        'center_loc': ORIGIN,

        "arrow_config": {
            "buff": 0,
            "max_tip_length_to_length_ratio": 0.35,
            "tip_length": 0.15,
            "max_stroke_width_to_length_ratio": 10,
            "stroke_width": 2,
        },

        'dt': 1/29,
        'run_time': 32,
        'speed': 1,

        # 'f_list': [1, 2],
        # 'a_list': [2, 1],
        # 'p_list': [0, PI],

    }

    def construct(self):

        # bg_rect = Rectangle(fill_color=self.bg_color, fill_opacity=1).scale(20)
        # self.add(bg_rect)
        # self.wait(0.25)

        t = Text("傅里叶变换绘制图形")
        self.play(Write(t))
        self.wait(1)
        self.play(FadeOut(t))
        self.wait(0.5)
        self.setup_all()
        self.anim_follow_EndPoint()
        self.wait(2)

    def set_frequency(self, f_list):
        self.frequency_list = np.array(f_list[0: self.circle_num])

    def set_amplitude(self, a_list):
        self.amplitude_list = np.array(a_list[0: self.circle_num]) * self.scale_all

    def set_phase(self, p_list):
        if p_list == 0:
            self.phase_list = np.array([0 for i in range(self.circle_num)])
        else:
            self.phase_list = np.array(p_list[0: self.circle_num])

    def curve_func(self, t):
        return np.array([16 * np.sin(t) ** 3, 13 * np.cos(t) - 5 * np. cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t), 0]) + UP * 1.6

    def curve_complex_func(self, t):
        return complex(self.curve_func(t)[0], self.curve_func(t)[1])

    def get_freqs(self):
        n = self.circle_num
        all_freqs = list(range(n // 2, -n // 2, -1))
        all_freqs.sort(key=abs)
        return all_freqs

    def get_coefficients_of_path(self, path, n_samples=10000, freqs=None):
        if freqs is None:
            freqs = self.get_freqs()
        dt = 1 / n_samples
        ts = np.arange(0, 1, dt)
        samples = np.array([
            path.point_from_proportion(t)
            for t in ts
        ])
        samples -= self.center_loc
        complex_samples = samples[:, 0] + 1j * samples[:, 1]

        result = []
        for freq in freqs:
            riemann_sum = np.array([
                np.exp(-TAU * 1j * freq * t) * cs
                for t, cs in zip(ts, complex_samples)
            ]).sum() * dt
            result.append(riemann_sum)

        return result

    def my_path(self, point_list):

        my_path = Polygon(*point_list)
        my_path.set_height(5.6)
        my_path.shift(UP)
        path = my_path.family_members_with_points()[0]
        path.set_fill(opacity=0)
        path.set_stroke(WHITE, 1)

        return path

    def setup_all(self):

        sample_n = 100
        path = [self.curve_func(i * 2 * PI/sample_n) for i in range(sample_n)]
        my_path = self.my_path(path)
        self.frequency_list = self.get_freqs()
        amplitudes = self.get_coefficients_of_path(my_path)
        self.amplitude_list = [abs(a) for a in amplitudes]

        self.phase_list = np.log(amplitudes).imag - PI / 2
        # self.phase_list = [0 for a in amplitudes]
        # print('phase:', self.phase_list)

        n = self.circle_num
        self.center_list = np.zeros((n + 1, 3)) + self.center_loc

        for i in range(n):
            v_i = np.array([np.sin(self.phase_list[i]), np.cos(self.phase_list[i]), 0]) * self.amplitude_list[i]
            self.center_list[i + 1: n + 2] += v_i

        self.always_continually_update = True

    def set_arrow(self):
        self.arrows = VGroup()

        for i in range(self.circle_num):
            # print('i = %d' % i)
            arrow_i = Vector(self.center_list[i+1] - self.center_list[i], color=self.arrow_color, **self.arrow_config).shift(self.center_list[i])
            #.put_start_and_end_on(self.center_list[i], self.center_list[i+1])
            # print(type(arrow_i))
            self.arrows.add(arrow_i)
            # print(len(self.arrows))

    def arrow_anim(self):
        self.set_arrow()
        self.play(ShowCreation(self.arrows), run_time=1.2)
        # self.play(ShowCreation(self.arrows.get_family()[0]), run_time=1.2)
        self.wait(0.5)
        n = self.circle_num
        dt = 1/14.9
        step_n = 120
        speed = 1
        d_theta = 2 * PI / step_n / n * speed

        for j in range(step_n + 1):
            # print('center_points:')
            # print(self.center_list)
            self.center_list = np.zeros((n + 1, 3)) + self.center_loc
            for i in range(self.circle_num):
                v_i = np.array([np.sin(self.phase_list[i] + d_theta * j * self.frequency_list[i]), np.cos(self.phase_list[i] + d_theta * j * self.frequency_list[i]), 0]) * self.amplitude_list[i]
                self.center_list[i + 1: n + 2] += v_i
                self.arrows[i].put_start_and_end_on(self.center_list[i], self.center_list[i+1])
            self.wait(dt)
        self.wait(0.25)

    def set_circles(self):
        self.circles = VGroup()
        for i in range(self.circle_num):
            circle_i = Circle(radius=self.amplitude_list[i], color=self.circle_color, stroke_width=self.circle_width).move_to(self.center_list[i])
            self.circles.add(circle_i)

    def circle_arrow_anim(self):

        self.set_arrow()
        self.set_circles()

        # self.play(ShowCreation(self.arrows), ShowCreation(self.circles), run_time=1.8)

        for i in range(self.circle_num):
            self.play(FadeIn(self.arrows[i]), FadeIn(self.circles[i]), run_time=0.32)

        #self.wait(0.5)
        # c1 = Circle(radius=1 * self.scale_all, color=self.circle_color, stroke_width=self.circle_width)
        # self.play(ShowCreation(c1), run_time=0.8)
        self.wait()

        n = self.circle_num
        dt = self.dt
        step_n = int(self.run_time/dt)
        speed = self.speed
        d_theta = 4 * PI / step_n * speed
        self.lines = VGroup()

        line_start = self.center_list[-1]
        # line_end = self.center_list[-1]
        for j in range(step_n + 1):
            # print('center_points:')
            # print(self.center_list)
            self.center_list = np.zeros((n + 1, 3)) + self.center_loc
            for i in range(self.circle_num):
                # print('i = %d' % i)
                v_i = np.array([np.sin(self.phase_list[i] + d_theta * j * self.frequency_list[i]), np.cos(self.phase_list[i] + d_theta * j * self.frequency_list[i]), 0]) * self.amplitude_list[i]
                self.center_list[i + 1: n + 2] += v_i
                self.arrows[i].put_start_and_end_on(self.center_list[i], self.center_list[i+1])
                self.circles[i].move_to(self.center_list[i])
            line_end = self.center_list[-1]
            line_j = Line(line_start, line_end, color=self.curve_color, stroke_width=self.curve_width)
            self.lines.add(line_j)
            self.add(line_j)
            line_start = self.center_list[-1]
            self.wait(dt)
            # if j == int(step_n/2):
            #     self.play(ShowCreation(self.circles[0]), ShowCreation(self.arrows[0]), run_time=1)
            #     self.play(FadeOut(c1), run_time=1)
            #     self.wait(0.9)
            # elif j > int(step_n/2):

        self.wait(0.25)

    def anim_follow_EndPoint(self):

        self.set_arrow()
        self.set_circles()

        self.add(self.arrows, self.circles)

        # move_vector = ORIGIN - self.center_list[-1]
        # self.arrows.shift(move_vector)
        # self.circles.shift(move_vector)

        n = self.circle_num
        dt = self.dt
        step_n = int(self.run_time/dt)
        speed = self.speed
        d_theta = 4 * PI / step_n * speed
        self.lines = VGroup()

        line_start = self.center_list[-1]

        s = 5

        for j in range(step_n + 1):
            # print('center_points:')
            # print(self.center_list)
            self.center_list = np.zeros((n + 1, 3)) + self.center_loc
            for i in range(self.circle_num):
                # print('i = %d' % i)
                v_i = np.array([np.sin(self.phase_list[i] + d_theta * j * self.frequency_list[i]), np.cos(self.phase_list[i] + d_theta * j * self.frequency_list[i]), 0]) * self.amplitude_list[i]
                self.center_list[i + 1: n + 2] += v_i
                self.arrows[i].put_start_and_end_on(self.center_list[i], self.center_list[i+1])
                self.circles[i].move_to(self.center_list[i])
            line_end = self.center_list[-1]
            line_j = Line(line_start, line_end, color=self.curve_color, stroke_width=self.curve_width)

            move_vector = ORIGIN - self.center_list[-1]
            self.arrows.shift(move_vector)
            self.circles.shift(move_vector)
            self.lines.shift(line_start - line_end)
            line_j.shift(move_vector)

            self.lines.add(line_j)
            self.add(line_j)

            self.arrows.scale(1, about_point=s, about_edge=ORIGIN)
            self.circles.scale(1, about_point=s, about_edge=ORIGIN)
            self.lines.scale(1, about_point=s, about_edge=ORIGIN)

            self.wait(dt)
            # VGroup.scale()
            self.arrows.scale(1, about_point=1/s, about_edge=ORIGIN)
            self.circles.scale(1, about_point=1/s, about_edge=ORIGIN)
            self.lines.scale(1, about_point=1/s, about_edge=ORIGIN)

            line_start = self.center_list[-1]

        self.wait(0.25)

if __name__ == '__main__':
    from os import system
    system(f"manimgl {__file__} heart")