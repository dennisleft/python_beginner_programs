#make circle using squares
import turtle
circle_squares=turtle.Turtle()
#change speed
circle_squares.speed(0)
#color
circle_squares.pencolor('red')
'''
start-go
right-go
right-go
right-go
angle 126-go



'''

def circles(length,r_angle,angle):
    for c in range(100):
        circle_squares.forward(length)
        circle_squares.right(r_angle)
        circle_squares.forward(length)
        circle_squares.right(r_angle)
        circle_squares.forward(length)
        circle_squares.right(r_angle)
        circle_squares.forward(length)
        circle_squares.right(angle)
        

circles(50,90,125)
print('press any ENTER to exit')
input()
