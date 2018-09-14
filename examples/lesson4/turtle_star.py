# coding=utf8

import turtle

# 创建画布，设置背景色
wn = turtle.Screen()
wn.bgcolor("lightgreen")

# 创建一只笔，设置好颜色和粗细
pen = turtle.Turtle()
pen.color("hotpink")
pen.pensize(5)

# 放到左上方
pen.penup()
pen.goto(-150, 100)
pen.pendown()

# TODO: 开始画画吧！

for i in xrange(5):
    pen.forward(350)
    pen.right(144)

wn.exitonclick()


