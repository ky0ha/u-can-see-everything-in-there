from manimlib import *

class obj(Scene):
    def construct(self):
        t1 = Text("python和js的字符串", font_size=60)
        t2 = Text("f\"\"和``用法的简单介绍", color=YELLOW).next_to(t1, DOWN).shift(DOWN*0.5)
        
        self.add(VGroup(t1, t2))

if __name__ == '__main__':
    from os import system
    system(f"manimgl {__file__} obj")