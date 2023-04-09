from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def rotate_clockwise():
    tim.right(50)


def rotate_anti_clockwise():
    tim.left(50)


def reset_tim():
    tim.reset()


screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(rotate_clockwise, "d")
screen.onkey(rotate_anti_clockwise, "a")
screen.onkey(reset_tim, "c")

screen.exitonclick()

