import turtle
t = turtle.Pen()

angle = int(input("몇각형을 그릴까요? : "))

for i in range(angle) :
    t.forward(100)
    t.right((angle-2)*180/angle)