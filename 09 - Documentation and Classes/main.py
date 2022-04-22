from circle import Circle_01, Circle_05b, Circle_06
from tire import Tire

from random import random, seed


def tutorial():
    # Tutorial
    print('Circuitous version', Circle_01.version)
    c = Circle_01(10)
    print('A circle of radius', c.radius)
    print('has an area of', c.area())


def firstCustomer():
    # Academia
    seed(8675309)  # for reproducable results
    print('Using Circuitous(tm) version', Circle_01.version)
    n = 10
    circles = [Circle_01(random()) for i in range(n)]
    print('The average area of', n, 'radnom circles')
    avg = sum([c.area() for c in circles]) / n
    print('is %.1f' % avg)


def secondCustomer():
    # Rubber sheet company
    cuts = [0.1, 0.7, 0.8]
    circles = [Circle_01(r) for r in cuts]
    for c in circles:
        print('A circle with a radius of', c.radius)
        print('has a perimeter of', c.perimeter())
        print('and a cold area of', c.area())
        c.radius *= 1.1  # if something is a variable someone will change it
        print('amd a warm area of', c.area())


def thirdCustomer():
    # Tire company
    t = Tire(22)
    print('A tire of radius', t.radius)
    print('has an inner area of', t.area())
    print('and an odometer corrected perimeter of', t.area())


def fourthCustomer():
    # National graphics company
    # dont want this
    # c = Circle(bbd_to_radius(25.1))
    c = Circle_05b.from_bbd(25.1)
    print('A circle with a bbd of 25.1')
    print('has a radius of', c.radius)
    print('and an area of', c.area())


if __name__ == '__main__':
    print('Tutorial')
    tutorial()

    print('\n\n\nFirst Customer')
    firstCustomer()

    print('\n\n\nSecond Customer')
    secondCustomer()

    print('\n\n\nThird Customer')
    thirdCustomer()

    print('\n\n\nFourth Customer')
    fourthCustomer()
