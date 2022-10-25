from manimlib import *

class test(Scene):
    def construct(self):
        self.add(
            DoubleArrow(
                start=np.array([-1, 2, 0]),
                end=np.array([1, 1, 0]),
                color=BLUE,
                fill_color=BLUE
            )
        )

if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")