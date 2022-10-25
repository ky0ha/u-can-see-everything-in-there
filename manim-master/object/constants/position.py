from manimlib import *

class pos(Scene):
    def construct(self):
        c1 = Circle()
        c1.set_stroke(color=RED, width=DEFAULT_STROKE_WIDTH)
        c1.set_fill(color=YELLOW, opacity=0.5)
        
        c2 = Circle()
        c2.set_stroke(color=PURPLE)
        c2.set_fill(color=BLUE, opacity=0.5)
        
        self.play(Write(c1))
        
        cs = [c2.copy() for _ in range(4)]
        position = [TOP, RIGHT_SIDE, BOTTOM, LEFT_SIDE]
        for c, p in zip(cs, position):
            c.next_to(c1, p)
            self.play(Write(c))

if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} pos")