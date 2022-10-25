from manimlib import *

# width	长轴，默认为2
# height	短轴，默认为1

class test(Scene):
    def construct(self):
        ellipse = Ellipse(
            width=4,            # 长轴为4, 也就是a = 2
            height=2            # 短轴为2，也就是b = 1    
        )
        ellipse.set_fill(color=GREEN_B, opacity=0.9)
        
        circle = Circle(
            radius=2,
            color=BLUE
        )

        self.add(circle)
        self.add(ellipse)

if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")