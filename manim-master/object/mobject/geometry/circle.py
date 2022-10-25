from manimlib import *

# color	颜色，默认为WHITE
# opacity	透明度，默认为1
# gloss	反光度，默认为0
# shadow	阴影，默认为0
# is_fixed_in_frame	是否固定在frame中，默认为False。如果为True，那么在使用相机旋转画面时，该形体不会跟着旋转

# fill_color	填充的颜色，默认为None，即不填充
# fill_opacity	填充的颜色的透明度，默认为0，即完全透明
# stroke_color	轮廓线的颜色，默认为None
# stroke_opacity	轮廓线的透明度，默认为1，即完全不透明
# stroke_width	轮廓线的粗细，默认为4
# draw_stroke_behind_fill	是否在填充后再绘制轮廓线，默认为False
# background_image_file	图形填充的图片的路径，默认为None

class test(Scene):
    def construct(self):
        c1 = Circle(
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_color=GREEN,
            stroke_opacity=0.9,
            stroke_width=8,
            gloss=1.0
        )
        
        c2 = Circle(
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_color=GREEN,
            stroke_opacity=0.9,
            stroke_width=8,
            gloss=1.0,
            shadow=1.0
        )
        
        c2.next_to(c1, RIGHT_SIDE)
        
        self.add(c1)
        self.add(c2)
    
if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")