from dice import Dice
from tkinter import *


def createCanvas(width=650, height=300):
    # Creates a basic demo canvas
    master = Tk()
    canvas = Canvas(master, width=width, height=height, bg='green')
    canvas.pack()
    return canvas


def main():
    canvas = createCanvas()

    dice = Dice(canvas, size=50)
    dice.setPosition(20, 20)
    dice.roll()
    print("Value: ", dice.getValue())

    dice1 = Dice(canvas, positionX=100, positionY=100)
    dice1.setColor(colorDice='#3d3d3d', colorDots='#f78d1b')

    dice2 = Dice(canvas, positionX=210, positionY=100)
    dice2.setColor(colorDice='#124a1c', colorDots='white')
    dice2.setSize(50)

    dice3 = Dice(canvas, colorDice='darkblue', colorDots='magenta')
    dice3.setPosition(positionX=270, positionY=100)
    dice3.setSize(150)

    dice4 = Dice(canvas, size=25)
    dice4.setPosition(positionX=430, positionY=100)
    dice4.setColor(colorDice='#2c4b6e', colorDots='#b0f7ff')

    dice1.roll()
    dice2.roll()
    dice3.roll()
    dice4.roll()

    canvas.create_text(325, 70, text="you rolled: %d %d %d and %d" %
                                     (dice1.getValue(), dice2.getValue(), dice3.getValue(), dice4.getValue()))

    mainloop()


if __name__ == "__main__":
    main()
