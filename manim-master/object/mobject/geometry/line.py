from manimlib import *

# start	起始点，默认为LEFT
# end	终点，默认为RIGHT
# buff	内收缩系数，默认为0。取值范围为0-0.5，取值越大，实线越短
# path_arc	弯曲程度，默认为0。值越大，弯曲程度越大

# dash_length	虚线块的长度，默认为DEFAULT_DASH_LENGTH，也就是0.05
# dash_spacing	虚线块之间的间隔，默认为None
# positive_space_ratio	虚线块与间隔的比例，默认为0.5

class test(Scene):
    def construct(self):
        l1 = Line(
            start=LEFT * 3,
            end=RIGHT * 3,
            buff=0,
            path_arc=0,
            color=GREEN
        )
        l2 = DashedLine(
            start=LEFT * 3,
            end=RIGHT * 3,
            dash_length=0.05,
            dash_spacing=0.1,
            positive_space_ratio=0.5,
            color=BLUE
        )
        l2.next_to(l1, DOWN * 2)
        self.add(l1, l2)

if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")