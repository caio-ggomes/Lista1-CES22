import turtle

playground = turtle.Screen()
playground.bgcolor("lightgreen")

artist = turtle.Turtle()
artist.color("violet", "violet")
artist.pensize(4) 


def draw_square(size, turt):
    for i in range(4):
        turt.forward(size)
        turt.left(90)


current_size = 20
current_position = (0, 0)

for i in range(5):
    draw_square(current_size, artist)
    current_size += 20
    artist.penup()
    artist.setpos(artist.xcor()-10, artist.ycor()-10)
    artist.pendown()

playground.mainloop()