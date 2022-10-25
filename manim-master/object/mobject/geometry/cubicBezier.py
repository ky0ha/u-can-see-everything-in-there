from manimlib import *

# a0	第一个锚点
# h0	第一个手柄
# h1	第二个手柄
# a1	第二个锚点

class test(Scene):
    def construct(self):
        curve = CubicBezier(
            a0=np.array([-2, 1, 0]),
            h0=np.array([-1, 0, 0]),
            h1=np.array([1, 0, 0]),
            a1=np.array([2, 1, 0])
        )
        self.add(curve)

if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")