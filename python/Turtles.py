import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("orange")
    brad.speed(100)

    for x in range (0, 36):
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        
        brad.right(10)

    brad.right(45)
    brad.forward(200)

    for x in range (0, 36):
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        
        brad.right(10)
    
    brad.right(120)
    brad.forward(200)

    for x in range (0, 36):
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        
        brad.right(10)
    brad.right(60)
    brad.forward(200)

    for x in range (0, 36):
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        
        brad.right(10)



    window.exitonclick()

draw_square()