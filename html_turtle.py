"""
file: html_turtle.py
description: Understanding dataclass structures, queues, and HTML/CSS code within Python
language: Python3
author: Savannah Alfaro
"""
# Import & Set Up Workspace
import turtle as tt


# Define Functions
def default_color():
    """
    Sets the color of the turtle to default (black).
    :return: None
    """
    tt.color("black")


def font_options_box():
    """
    Draws the font options box (top-gray box).
    :return: None
    """
    tt.penup()
    tt.goto(0, 225)
    tt.pendown()

    tt.color("gray")
    tt.begin_fill()
    tt.fd(200)
    tt.right(90)
    tt.fd(70)
    tt.right(90)
    tt.fd(400)
    tt.right(90)
    tt.fd(70)
    tt.right(90)
    tt.fd(200)
    tt.end_fill()
    default_color()


def button(color):
    """
    Draws a single button on the font options box.
    :param color: color of the turtle
    :return: None
    """
    tt.color(color)
    tt.begin_fill()
    tt.circle(13)
    tt.end_fill()


def button_reposition():
    """
    Repositions the turtle to create a new button.
    :return: None
    """
    tt.up()
    tt.fd(33)
    tt.down()


def window_buttons():
    """
    Draws all the buttons on the font options box.
    :return: None
    """
    tt.up()
    tt.goto(-200, 175)
    tt.down()
    button_reposition()
    button("red")
    button_reposition()
    button("yellow")
    button_reposition()
    button("green")
    default_color()


def exit_box():
    """
    Draws the exit box (bottom-gray box).
    :return: None
    """
    tt.penup()
    tt.goto(0, -105)
    tt.pendown()

    tt.color("gray")
    tt.begin_fill()
    tt.fd(200)
    tt.right(90)
    tt.fd(100)
    tt.right(90)
    tt.fd(400)
    tt.right(90)
    tt.fd(100)
    tt.right(90)
    tt.fd(200)
    tt.end_fill()
    default_color()


def start_window():
    """
    Sets up the window, draws the font options box with buttons, draws the "Font Options" writing.
    :return: None
    """
    tt.speed(0)
    tt.hideturtle()
    tt.setup(400, 450)

    font_options_box()
    window_buttons()

    tt.color("cyan")
    tt.penup()
    tt.goto(0, 175)
    tt.pendown()
    tt.write("Font Options", False, align="center", font=("Verdana", 18, "normal"))

    tt.penup()
    tt.goto(-100, 100)
    tt.pendown()
    default_color()


def exit_window():
    """
    Draws the "Please click anywhere in the box to exit window" writing.
    :return: None
    """
    exit_box()

    tt.color("cyan")
    tt.penup()
    tt.goto(0, -150)
    tt.pendown()
    tt.write("Please click anywhere in", False, align="center", font=("Verdana", 16, "normal"))
    reposition()
    tt.write("the box to exit window", False, align="center", font=("Verdana", 16, "normal"))
    default_color()

    print("\nPlease click anywhere in the box to exit the window and continue.\n")
    tt.Screen().exitonclick()


def reposition():
    """
    Repositions the turtle to draw another line of text.
    :return: None
    """
    tt.up()
    tt.right(90)
    tt.fd(30)
    tt.left(90)
    tt.down()


def turtle_font():
    """
    Draws all the types of fonts line-by-line.
    :return: None
    """
    tt.write("Arial", False, align="left", font=("Arial", 16, "normal"))
    reposition()
    tt.write("Comic Sans MS", False, align="left", font=("Comic Sans MS", 16, "normal"))
    reposition()
    tt.write("Lucida Grande", False, align="left", font=("Lucida Grande", 16, "normal"))
    reposition()
    tt.write("Tahoma", False, align="left", font=("Tahoma", 16, "normal"))
    reposition()
    tt.write("Verdana", False, align="left", font=("Verdana", 16, "normal"))
    reposition()
    tt.write("Helvetica", False, align="left", font=("Helvetica", 16, "normal"))
    reposition()
    tt.write("Times New Roman", False, align="left", font=("Times New Roman", 16, "normal"))


def draw_textbox():
    """
    Calls all the start_window, turtle_font, and exit_window functions to draw the textbox.
    :return: None
    """
    start_window()
    turtle_font()
    exit_window()
