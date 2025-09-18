import turtle
import random

def tree_basic(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree_basic(branchLen - 15, t)
        t.left(40)
        tree_basic(branchLen - 15, t)
        t.right(20)
        t.backward(branchLen)

def tree_thickness(branchLen, t):
    if branchLen > 5:
        t.width(max(1, branchLen // 10))
        t.forward(branchLen)
        t.right(20)
        tree_thickness(branchLen - 15, t)
        t.left(40)
        tree_thickness(branchLen - 15, t)
        t.right(20)
        t.backward(branchLen)

def tree_colors(branchLen, t):
    if branchLen > 5:
        if branchLen < 20:
            t.color("green")
        else:
            t.color("brown")
        t.forward(branchLen)
        t.right(20)
        tree_colors(branchLen - 15, t)
        t.left(40)
        tree_colors(branchLen - 15, t)
        t.right(20)
        t.backward(branchLen)

def tree_random_angles(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(random.randint(15, 45))
        tree_random_angles(branchLen - 15, t)
        t.left(random.randint(15, 45))
        tree_random_angles(branchLen - 15, t)
        t.right(random.randint(15, 45))
        t.backward(branchLen)

def tree_all_enhanced(branchLen, t):
    if branchLen > 5:
        t.width(max(1, branchLen // 10))
        if branchLen < 20:
            t.color("green")
        else:
            t.color("brown")
        t.forward(branchLen)
        t.right(random.randint(15, 45))
        tree_all_enhanced(branchLen - random.randint(10, 20), t)
        t.left(random.randint(15, 45))
        tree_all_enhanced(branchLen - random.randint(10, 20), t)
        t.right(random.randint(15, 45))
        t.backward(branchLen)

def draw_tree(tree_func):
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree_func(75, t)
    myWin.exitonclick()

def main():
    print("Выберите вариант дерева:")
    print("1 - Базовое дерево")
    print("2 - С толщиной ветвей")
    print("3 - С цветами (листья)")
    print("4 - Со случайными углами")
    print("5 - Все улучшения")
    
    choice = input("Введите номер (1-5): ").strip()
    
    if choice == "1":
        draw_tree(tree_basic)
    elif choice == "2":
        draw_tree(tree_thickness)
    elif choice == "3":
        draw_tree(tree_colors)
    elif choice == "4":
        draw_tree(tree_random_angles)
    elif choice == "5":
        draw_tree(tree_all_enhanced)
    else:
        print("Неверный выбор, запускаю базовое дерево")
        draw_tree(tree_basic)

if __name__ == "__main__":
    main()
