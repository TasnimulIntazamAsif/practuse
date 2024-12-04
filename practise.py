import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create and customize the turtle
t = turtle.Turtle()
t.pensize(5)
t.color("blue")
t.speed(3)

# Function to draw 'H'
def draw_H():
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.backward(100)

# Function to draw 'e'
def draw_e():
    t.penup()
    t.goto(-120, 0)
    t.pendown()
    t.right(90)
    t.circle(30, 360)
    t.penup()
    t.goto(-120, 30)
    t.pendown()
    t.right(90)
    t.forward(30)

# Function to draw 'l'
def draw_l():
    t.penup()
    t.goto(-60, 100)
    t.pendown()
    t.right(90)
    t.forward(100)

# Function to draw 'o'
def draw_o():
    t.penup()
    t.goto(30, 0)
    t.pendown()
    t.circle(30)

# Draw the word "Hello"
draw_H()
draw_e()
draw_l()
draw_l()
draw_o()

# Hide the turtle and keep the window open
t.hideturtle()
screen.mainloop()
