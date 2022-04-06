import turtle as t
from datetime import datetime as dt
import random
colormap =[0,0,0]
# import time
pen = t.Turtle()
wt = t.Turtle()
p = t.Turtle()
# t.bgcolor('sky blue')
def skip(step,pen=pen):
    pen.penup()
    pen.forward(step)
    pen.pendown()
def drawClock(radius=100):
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(7)
    pen.pencolor('blue')
    t.tracer(False)
    pen.home()
    for i in range(60):
        skip(radius)
        if i % 5 ==0:
            pen.forward(20)
            skip(-radius-20)
        else:
            pen.dot(5)
            skip(-radius)
        pen.right(6)
    t.tracer(True)

def writeDate():
    t2=t.Turtle()
    t2.hideturtle()
    nt=dt.now()
    date =nt.strftime('%Y-%m-%d')
    weekday = nt.strftime('%A')
    # print('date: {0} \n weekday:{1}'.format(date,weekday))
    t2.pencolor('gray')
    t2.setheading(0)
    skip(60,t2)
    t2.write(weekday, align="center", font=("Courier", 14, "bold"))
    skip(-20,t2)
    t2.write(date, align="center", font=("Courier", 14, "bold"))
def makePoint(pointName, len):  # 钟的指针，时针、分针、秒针
    t.penup()
    t.home()
    t.begin_poly()
    t.back(0.1 * len)
    t.forward(len * 1.1)
    t.end_poly()
    poly = t.get_poly()
    t.register_shape(pointName, poly)  # 注册为一个shape

def drawPoint():
    nt = dt.now()
    t.tracer(False)
    p.clear()
    p.hideturtle()
    # draw second
    p.penup()
    p.home()
    p.pendown()
    p.setheading(360 / 60 * nt.second)
    # p.pencolor('red')
    p.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    p.pensize(1)

    skip(140,p)
    p.backward(160)

    # draw minute
    p.penup()
    p.home()
    p.pendown()
    p.setheading(360 / 60 * nt.minute)
    p.pencolor('black')
    p.pensize(3)
    skip(120,p)
    p.backward(135)
    # draw hour
    p.penup()
    p.home()
    p.pendown()
    p.setheading(360 / 12 * nt.hour + 30 / 60 * nt.minute)
    p.pencolor('black')
    p.pensize(5)
    skip(80,p)
    p.backward(90)
    t.tracer(True)
    # time.sleep(0.8)
    # t.tracer(False)
    # p.clear()
    # for _ in range(24):
    #     p.undo()
    t.tracer(True)
#     t.ontimer(drawPoint, 100)
# def writeTime():


    wt.clear()
    wt.hideturtle()
    t.tracer(False)
    wt.penup()
    wt.home()
    # wt.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    # wt.setheading(random.randint(0,360))
    # wt.forward(random.randint(180,300))
    wt.setheading(180)
    wt.forward(100)
    wt.pendown()
    nt = dt.now()
    if nt.second<10:
        ntsec = '0'+str(nt.second)
    else:
        ntsec =str(nt.second)
    # ntsec = [x if nt.second<10 x='0'+str(nt.second) else: x=str( nt.second)]
    nowtime =str(nt.hour)+":"+str(nt.minute)+":"+ntsec
    print(nowtime)
    wt.write(nowtime, align="center", font=("Courier", 34, "bold"))
    t.tracer(True)
    t.update()
    t.ontimer(drawPoint,900)

if __name__ == '__main__':
    t.colormode(255)
    t.mode('logo')
    # pen.tracer(False)
    drawClock(160)

    writeDate()
    # writeTime()

    drawPoint()
    # realTime()
    # t.tracer(True)
    t.done()