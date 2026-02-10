import turtle

def tree_basic(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree_basic(branchLen - 15, t)
        t.left(40)
        tree_basic(branchLen - 15, t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(270)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree_basic(75, t)
    myWin.exitonclick()

if __name__ == "__main__":
    main()

# На мой взгляд перевернутое дерево это гора