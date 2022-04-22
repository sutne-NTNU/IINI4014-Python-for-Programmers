import random
from tkinter import *


class Dice:
    """Class that draws a dice on a tkinter canvas."""

    def __init__(self, canvas, size=100, positionX=0, positionY=0, colorDice='white', colorDots='black'):
        self.canvas = canvas
        self.size = size
        self.positionX = positionX
        self.positionY = positionY
        self.colorDice = colorDice
        self.colorDots = colorDots
        self.value = 0

    def setPosition(self, positionX, positionY):
        """Change position of a dice after the inital placement"""
        self.positionX = positionX
        self.positionY = positionY

    def setColor(self, colorDice='white', colorDots='black'):
        """Change the color of a dice, defaults to a white dice with black dots"""
        self.colorDice = colorDice
        self.colorDots = colorDots

    def setSize(self, size):
        """Get the value of the last roll"""
        self.size = size

    def getValue(self):
        """Get the value of the last roll"""
        return self.value

    def roll(self):
        """Calculates a random value from 1 to 6, and draws the resulting dice on the canvas"""
        self.value = random.randint(1, 6)
        self.draw()
        return

    def draw(self):
        """Draws the entire dice on the canvas"""
        self.canvas.create_rectangle(self.positionX, self.positionY,
                                     self.positionX + self.size, self.positionY + self.size,
                                     fill=self.colorDice, outline="")
        self.__drawDots()

    def __drawDots(self):
        """Draws all the dots in their appropriate positions"""
        gridSize = self.size / 5

        # divide dice horisontally and vertically, using relative position for the dice
        LEFT = self.positionX + gridSize
        CENTER_HORISONTAL = self.positionX + (2.5 * gridSize)
        RIGHT = self.positionX + (self.size - gridSize)

        TOP = self.positionY + gridSize
        CENTER_VERTICAL = self.positionY + (2.5 * gridSize)
        BOTTOM = self.positionY + (self.size - gridSize)

        # draw dots correspnding to value
        if self.value % 2 == 1:
            self.__drawDot(CENTER_HORISONTAL, CENTER_VERTICAL)
        if self.value >= 2:
            self.__drawDot(LEFT, TOP)
            self.__drawDot(RIGHT, BOTTOM)
        if self.value >= 4:
            self.__drawDot(RIGHT, TOP)
            self.__drawDot(LEFT, BOTTOM)
        if self.value == 6:
            self.__drawDot(LEFT, CENTER_VERTICAL)
            self.__drawDot(RIGHT, CENTER_VERTICAL)

    def __drawDot(self, centerX, centerY):
        """Draws a dot with center in (centerX, centerY)"""
        r = self.size / 9
        self.canvas.create_oval(centerX - r, centerY - r, centerX + r, centerY + r, fill=self.colorDots, outline="")
