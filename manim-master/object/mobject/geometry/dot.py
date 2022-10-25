from manimlib import *

# radius	点的半径，默认值为0.08
# stroke_width	轮廓线的粗细，默认为0
# fill_opacity	填充的透明度，默认为1
# color	颜色，默认为WHITE

class test(Scene):
    def construct(self):
        colors = [BLUE, YELLOW, RED]
        for i in range(-2, 3):
            for j in range(-2, 3):
                d = Dot(
                    point=np.array([i, j, 0]),
                    color=colors[(i + j) % len(colors)]
                )
                self.add(d)

if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")