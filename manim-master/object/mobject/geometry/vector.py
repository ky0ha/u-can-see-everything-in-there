from manimlib import *

# start	起点坐标，默认为np.array([-1, 0, 0])
# end	终点坐标，默认为np.array([1, 0, 0])
# fill_color	填充的颜色，默认为GREY_A
# fill_opacity	填充颜色的透明度，默认为1
# stroke_width	轮廓线的粗细，默认为0
# buff	收缩系数，默认为0.25
# thickness	厚度，默认为0.05
# tip_width_ratio	箭头长方体和头的宽度比，默认为5
# tip_angle	头三角形的夹角默认为60度

# 向量类Vector是Arrow的派生类，与Arrow不同的是

# Vector的起点默认是原点
# Vector的buff是0，也就是不会收缩
# Vector输入的代表方向的numpy数组可以是二维的，也可以是三维的，但是Arrow的start和end必须是三维的。

class test(Scene):
    def construct(self):
        colors = [BLUE, RED, GREEN]
        vectors = [
            np.array([1, 0]),
            np.array([1, 1]),
            np.array([1, 3]),
            np.array([-2, 1]),
            np.array([-1, -1])
        ]
        
        temp_vec, temp_text = None, None
        for index, v in enumerate(vectors):
            if not self.get_mobjects():     # 检查Scene画布上有没有放实体，没有就放，你也可以通过temp_vec是否为None来等价判断，这个地方只是单纯想让你知道有get_mobjects这个方法
                temp_vec = Vector(
                    direction=v,
                    fill_color=colors[index % len(colors)]
                )
                temp_text = Tex(f"({v[0]}, {v[1]})")
                temp_text.move_to(np.hstack((v, 0)) * 1.2)      # move_to的参数必须是三维向量
                self.add(temp_vec, temp_text)
            else:
                cur_vec = Vector(
                    direction=v,
                    fill_color=colors[index % len(colors)]
                )
                cur_text = Tex(f"({v[0]}, {v[1]})")
                cur_text.move_to(np.hstack((v, 0)) * 1.2)
                self.play(
                    ReplacementTransform(temp_vec, cur_vec),
                    ReplacementTransform(temp_text, cur_text)
                )
                temp_vec = cur_vec
                temp_text = cur_text

if __name__=='__main__':
    from os import system
    system(f"manimgl {__file__} test")