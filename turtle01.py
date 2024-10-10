import turtle


t = turtle.Turtle()

def drawSpiral(t,lineLen):
    if lineLen > 0:
        t.forward(lineLen)
        t.right(90)
        drawSpiral(t,lineLen - 5)
drawSpiral(t,100)
turtle.done()






# # 创建一个海龟对象
# t = turtle.Turtle()

# # 让海龟向前移动 100 个单位
# t.forward(100)

# # 完成绘图
# turtle.done()
