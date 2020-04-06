import turtle


def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


playground = turtle.Screen()
playground.bgcolor("lightgreen")

artist = turtle.Turtle()
artist.color("violet", "violet")
artist.pensize(4)

draw_poly(artist, 8, 50)

playground.mainloop()