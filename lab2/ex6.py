import turtle

def dragon_curve(length, depth, t):
    if depth == 0:
        t.forward(length)
    else:
        t.right(45)
        dragon_curve(length * 0.7, depth - 1, t)
        t.left(90)
        dragon_curve(length * 0.7, depth - 1, t)
        t.right(45)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    myWin.bgcolor("white")
    
    t.speed(0)
    t.color("blue")
    t.width(2)
    
    t.up()
    t.goto(-200, 0)
    t.down()
    
    dragon_curve(200, 10, t)
    
    myWin.exitonclick()

if __name__ == "__main__":
    main()
