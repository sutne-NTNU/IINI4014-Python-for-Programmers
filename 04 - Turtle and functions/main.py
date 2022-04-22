import turtle as Turtle
from colour import Color


# the way i am drawing the circle makes it very ineffeicient to utelize a generator as i i am using
# the index of the point in the list in order to know where to draw the line, and the generator doesnt
# have indeces, so i made this small example to demonstrate how they work instead
def cube_generator(nums):
    for num in nums:
        yield num ** 3


def main():
    for cube in cube_generator([1, 2, 3, 4, 5]):
        print(cube)  # [1, 8, 27, 64, 125]

    # Drawing the outer circle
    points = drawCircle()

    # Drawing with different multipliers
    turtle = Turtle.Turtle()
    turtle.hideturtle()
    for i in range(0, 900, 1):
        # multiplier increases more and more
        multiplier = (i / 150) ** 2
        # Draw the lines
        drawLines(turtle, points, multiplier)
        # Display the current multiplier in the window
        write(turtle, text=('Multiplier: %.2f' % multiplier))
        # refresh/show the drawing
        refreshDrawing()
        # Clear the lines before next multiplier
        turtle.clear()
    Turtle.done()


# Setting circle size
CIRCLE_RADIUS = 200
NUMBER_OF_POINTS = 150

# Turning off refresh for every turtle update eg. i manually have to update the screen with Turtle.update()
# This basically means i dont have to wait for the turtle to draw.
Turtle.tracer(0, 0)
# setting background colour to dark gray
Turtle.bgcolor("#252930")
# Creating a colorgradient to make the drawing a bit more interesting
colors = list(Color("#fc0303").range_to(Color("#fc035a"), round(NUMBER_OF_POINTS * 3)))
# colors = list(Color("#fc0303").range_to(Color("#fc035a"), NUMBER_OF_POINTS - 1))
# keeps track of current colour-index
COLOR = 0


# Refreshes the drawing
def refreshDrawing():
    Turtle.update()


# Draw outer circle and return array of all the points along the circumference
def drawCircle():
    # uses its own turtle as i only need to draw the points once
    turtle = Turtle.Turtle()
    turtle.hideturtle()
    turtle.pencolor("#686D78")
    turtle.up()
    turtle.setpos(0, -CIRCLE_RADIUS)
    points = []
    for i in range(0, NUMBER_OF_POINTS):
        turtle.dot()
        points.append((turtle.pos()))
        turtle.up()
        turtle.circle(CIRCLE_RADIUS, 360 / NUMBER_OF_POINTS)
        turtle.down()
    return points


def drawLines(turtle, points, multiplier):
    changeColour(turtle)  # change colour of each multiplier
    for starting_point in range(0, len(points)):
        # changeColour(turtle)  # change colour of each line

        start = points[starting_point]
        finish = points[round((starting_point * multiplier)) % len(points)]
        # example: start = 4, multiplier = 2
        # draws line from pointnr 4 to pointnr 8

        turtle.up()
        turtle.goto(start)
        turtle.down()
        turtle.goto(finish)


# Changes the pencolor to the next in the gradiant
def changeColour(turtle):
    global COLOR
    turtle.pencolor(str(colors[COLOR]))
    COLOR = (COLOR + 1) % len(colors)


# Writes the given text above the top of the circle
def write(turtle, text):
    turtle.up()
    turtle.goto(0, CIRCLE_RADIUS + 10)
    turtle.color('white')
    turtle.write(text, font=("", 24, ""), align='center')


if __name__ == "__main__":
    main()
