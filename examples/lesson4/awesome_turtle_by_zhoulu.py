# coding:utf-8
import turtle as t


def moveM(tempX,tempY):
    t.pu()  # 提笔
    t.goto(tempX,tempY)  # 画笔前往坐标
    t.pd()  # 下笔
wn = t.Screen()
t.pensize(8)
t.colormode(255)  # 设置GBK颜色范围为0-255
t.color((0, 0, 0))  # 设置画笔颜色
t.fillcolor(255,230,0)#填充颜色
t.setup(600,700)  # 设置主窗口
t.speed(10)#速度

#####身体
t.begin_fill()
moveM(130,170)

t.seth(90) # 笔的角度为90°
a = 5.5
for i in range(60):
    if  0<i<30:
        a = a+0.07

        t.lt(3) #向左转3度
        t.fd(a) #向前走a的步长
    else:
        a = a - 0.07
        t.lt(3)
        t.fd(a)
b = 6
t.rt(7)
for i in range(30):
    t.lt(0.4)
    t.fd(b)
c = 5.5
t.lt(4)

for i in range(23):
        t.lt(3)
        t.fd(c)
t.lt(5)
for i in range(28):
        t.lt(0.5)
        t.fd(4)
for i in range(23):
        t.lt(2.8)
        t.fd(4)
t.lt(13.5)
for i in range(31):
    t.lt(0.4)
    t.fd(7)
t.seth(0)
t.end_fill()
########左眼
t.fillcolor('white')
t.begin_fill()
moveM(-50,130)
t.circle(50)
t.end_fill()

t.fillcolor('black')
t.begin_fill()
moveM(-45,155)
t.circle(20)
t.end_fill()

t.pencolor(1,1,1)
t.color('white')
t.begin_fill()
moveM(-40,170)
t.circle(8)
t.end_fill()


#######右眼
t.color((0, 0, 0),'white')
t.begin_fill()
moveM(50,130)
t.circle(50)
t.end_fill()


t.color((0, 0, 0),'black')
t.begin_fill()
moveM(45,155)
t.circle(20)
t.end_fill()

t.pencolor(1,1,1)
t.color('white')
t.begin_fill()
moveM(50,170)
t.circle(8)
t.end_fill()
#########左眼睛框
t.pencolor(0,0,0)
moveM(100,165)
t.forward(30)
moveM(100,169)
t.forward(29)
moveM(100,173)
t.forward(29)
moveM(100,177)
t.forward(29)
moveM(100,180)
t.forward(29)
moveM(100,183)
t.forward(28)

#########右眼睛框

moveM(-122,183)
t.fd(20)
moveM(-122,180)
t.fd(20)
moveM(-122,176)
t.fd(20)
moveM(-122,172)
t.fd(20)
moveM(-122,169)
t.fd(20)
moveM(-122,165)
t.fd(20)

#嘴巴
moveM(-10,70)
t.fd(0.1)
t.begin_fill()
moveM(-10,70)
for i in range(32):
    t.lt(1.2)
    t.fd(2.5)
moveM(-10,70)
t.rt(87)
for i in range(33):
    t.lt(4)
    t.fd(3)
t.end_fill()

#################################

moveM(-125,-5)
t.fd(0.1)
t.begin_fill()

t.fillcolor(70,130,180)
moveM(-125,-5)
t.rt(82)
t.fd(30)
t.lt(90)
t.fd(33)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(40)
t.lt(90)
t.fd(31)
t.rt(90)

cc = -1.5
for i in range(28):
    cc = cc - 0.1
    t.lt(cc)
    t.fd(4.4)
t.rt(7.5)
t.fd(100)
dd = 1.5
for i in range(30):
    dd = dd + 0.09
    t.rt(dd)
    t.fd(4.4)
t.end_fill()


######背带

moveM(-130,55)
t.begin_fill()
t.rt(125)
t.fd(70)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(60)
t.end_fill()
moveM(-90,25)
t.circle(4)

moveM(134,55)
t.begin_fill()
t.lt(75)
t.fd(70)
t.lt(90)
t.fd(20)
t.lt(90)
t.fd(55)
t.end_fill()
moveM(105,6)
t.circle(4)

moveM(-20,6)
t.rt(45)
t.fd(55)
t.rt(90)
t.fd(25)
for i in range(45):
        t.rt(4)
        t.fd(2)
t.fd(22)
moveM(10,-70)
t.rt(180)
t.fd(30)
moveM(-90,-30)
for i in range(10):
    t.rt(6)
    t.fd(4)
moveM(100,-30)
t.lt(80)
for i in range(10):
    t.lt(6)
    t.fd(4)

###胳膊左
t.fillcolor(255,230,0)
moveM(-130,35)
t.begin_fill()
t.rt(130)
for i in range(7):
    t.lt(6)
    t.fd(8)
t.lt(30)
for i in range(6):
    t.lt(8)
    t.fd(8)
t.lt(147)
for i in range(6):
    t.rt(8)
    t.fd(12)
t.end_fill()
t.rt(210)
moveM(-135,-10)
t.fd(5)

###胳膊右
moveM(138,30)
t.begin_fill()
t.lt(95)
for i in range(7):
    t.rt(6)
    t.fd(6)
for i in range(6):
    t.rt(15)
    t.fd(6.5)
t.rt(100)
t.fd(60)
t.end_fill()
moveM(138,-5)
t.rt(135)
t.fd(5)
########脚
moveM(18,-105)
t.fillcolor(0,0,0)
t.begin_fill()
t.rt(45)
t.fd(40)
for i in range(3):
    t.lt(30)
    t.fd(2)
for i in range(3):
    t.lt(1)
    t.fd(15)
for i in range(3):
    t.lt(30)
    t.fd(3)
t.fd(12)
for i in range(9):
    t.lt(10)
    t.fd(3)
t.rt(90)
t.fd(8)
t.end_fill()

moveM(4,-105)
t.begin_fill()
t.rt(185)
t.fd(40)
for i in range(3):
    t.rt(30)
    t.fd(2)
for i in range(3):
    t.lt(1)
    t.fd(15)
for i in range(3):
    t.rt(30)
    t.fd(3)
t.fd(12)
for i in range(9):
    t.rt(10)
    t.fd(3)
t.lt(90)
t.fd(8)
t.end_fill()
######头发
moveM(5,285)
t.rt(60)
for i in range(15):
    t.rt(5)
    t.fd(6)
moveM(0,285)
t.rt(190)
for i in range(15):
    t.lt(5)
    t.fd(6)
moveM(10,285)
t.rt(180)
for i in range(10):
    t.rt(5)
    t.fd(6)
moveM(-5,285)
t.rt(180)
for i in range(10):
    t.lt(5)
    t.fd(6)
wn.exitonclick()