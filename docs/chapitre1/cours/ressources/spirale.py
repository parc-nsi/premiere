import turtle as tt

def spirale(n):
    tt.penup()
    tt.goto(0,0)
    tt.pendown()
    c = 5
    for i in range(4):
        for j in range(4):
            tt.forward(c)
            c = 10 + c
            tt.left(90)

spirale(4)
tt.exitonclick()