from manimlib import *
class obj(Scene):
    def page1(self):
        t1 = Text("利用前两期视频的知识点可以制作一个简单的哈夫曼译码器")
        t2 = Text("并利用while循环标志变量来表示译码的进度")
        
        self.play(Write(t1))
        self.wait(0.5)
        self.play(ApplyMethod(t1.shift, UP))
        self.wait(0.5)
        self.play(Write(t2))
        self.wait(0.5)
        self.play(FadeOut(VGroup(t1, t2)))
    
    def page2(self):
        t1 = Text("通过利用while循环的循环结束标志：right到达最右侧").shift(UP*1.6)
        t2 = Text("使用right来制作一个进度条，在每次循环的时候输出right/总长度").shift(UP*0.8)
        t3 = Text("为了更加简单的处理这个进度为两位小数的百分数")
        t4 = Text("添加一个变量speed来表示当前进度的数字并输出").shift(DOWN*0.8)
        t5 = Text("接下来通过伪代码的形式来展示一下").shift(DOWN*1.6)
        
        self.play(Write(t1))
        self.wait(0.5)
        self.play(Write(t2))
        self.wait(0.5)
        self.play(Write(t3))
        self.wait(0.5)
        self.play(Write(t4))
        self.wait(0.5)
        self.play(Write(t5))
        self.wait(1)
        self.play(FadeOut(VGroup(t1, t2, t3, t4, t5)))
    
    def page3(self):
        title1 = Title("Process Bar")
        code1 = Code("""
left, right = 0, 1
result, speed = '', 0
while right<=code_len:
    speed = right*10000//code_len
    print("processing: {:.2f}%".format(speed/100))
    [loop]""").shift(UP*1.5)
        t1 = Text("利用right通过计算得出标准的speed用来表示两位小数百分数").shift(DOWN)
        t2 = Text("再通过print格式化进行输出").shift(DOWN*1.8)
        t3 = Text("[loop]表示循环译码部分的算法，与介绍内容无关", color=RED)
        
        self.play(Write(title1))
        self.wait(0.5)
        self.play(Write(code1))
        self.wait()
        self.play(Write(t1))
        self.wait(0.5)
        self.play(Write(t2))
        self.wait(0.5)
        self.play(Write(t3))
        self.wait()
        self.play(FadeOut(VGroup(t1, t2, title1, code1, t3)))
    
    def page4(self):
        t1 = Text("通过这种方式实现的进度显示会有一个严重的问题", t2c={"严重的问题":RED})
        t2 = Text("由于每次循环都会进行一次I/O操作所以速度太慢")
        
        
        self.play(Write(t1))
        self.wait(0.5)
        self.play(ApplyMethod(t1.shift, UP))
        self.wait(0.5)
        self.play(Write(t2))
        self.wait()
        self.play(FadeOut(VGroup(t1, t2)))
    
    def page5(self):
        t1 = Text("为了同时保证运行效率和用户体验").shift(UP*2.4)
        t2 = Text("需要将尽可能减少io消耗的同时还要保证进度输出流畅").shift(UP*1.6)
        t3 = Text("通过将进度划分为每1%更新一次的方式可以减少io消耗").shift(UP*0.8)
        t4 = Text("但是用户体验不好，会显得进度更新十分卡顿")
        t5 = Text("最后顺着这个思路，构建了一个每n%更新一次的进度条").shift(DOWN*0.8)
        t6 = Text("其中这里的n是一个随机数，范围在0.07%到1%").shift(DOWN*1.6)
        t7 = Text("每次进度更新n%之后输出一次进度，然后重新随机n%数值").shift(DOWN*2.4)
        
        
        self.play(Write(t1))
        self.wait(0.5)
        self.play(Write(t2))
        self.wait(0.5)
        self.play(Write(t3))
        self.wait(0.5)
        self.play(Write(t4))
        self.wait(0.5)
        self.play(Write(t5))
        self.wait(0.5)
        self.play(Write(t6))
        self.wait(0.5)
        self.play(Write(t7))
        self.wait()
        self.play(FadeOut(VGroup(t1, t2, t3, t4, t5, t6, t7)))
    
    def page6(self):
        title1 = Title("Process Bar")
        code1 = Code("""while right<=code_len:
    if count%10==0:
        self.speed = right*10000//code_len
    if self.speed%flag==0: 
        self.s.set("processing: {:.2f}%".format(self.speed/100))
        flag = random.randint(7,100)
        self.init_window_name.update()
    count+=1
    [main loop]""").next_to(title1, DOWN).to_edge(LEFT)
        t1 = Text("通过每10次循环更新一次进度speed").shift(DOWN)
        t2 = Text("当进度speed能整除flag的时候更新一次进度显示").shift(DOWN*1.8)
        t3 = Text("更新显示后随机一个新的flag实现进度条随机更新的效果").shift(DOWN*2.6)
        
        self.play(Write(title1))
        self.wait(0.5)
        self.play(Write(code1))
        self.wait()
        self.play(Write(t1))
        self.wait(0.5)
        self.play(Write(t2))
        self.wait(0.5)
        self.play(Write(t3))
        self.wait()
        self.play(FadeOut(VGroup(t1, t2, title1, code1, t3)))
    
    def page7(self):
        t1 = Text('以上就是这期视频的全部内容，如果喜欢我的视频').shift(UP*1.6)
        t2 = Text('真心请求点个关注，顺便三连一下，感谢大佬们').shift(UP*0.8)
        t3 = Text('这对我这种小up来说真的很重要，是我支持下去的动力')
        t4 = Text('视频使用manim制作').shift(DOWN*0.8)
        t5 = Text('我会将我的视频源码放在简介和评论区链接内').shift(DOWN*1.6)
        
        self.play(Write(t1))
        self.wait()
        self.play(Write(t2))
        self.wait()
        self.play(Write(t3))
        self.wait()
        self.play(Write(t4))
        self.wait()
        self.play(Write(t5))
        self.wait()
        self.play(FadeOut(VGroup(t1, t2, t3, t4, t5)))

    
    def construct(self):
        self.page1()
        self.wait()
        self.page2()
        self.wait()
        self.page3()
        self.wait()
        self.page4()
        self.wait()
        self.page5()
        self.wait()
        self.page6()
        self.wait()
        self.page7()
        self.wait()
        
        
        self.embed()




if __name__ == '__main__':
    from os import system
    system(f"manimgl {__file__} obj")