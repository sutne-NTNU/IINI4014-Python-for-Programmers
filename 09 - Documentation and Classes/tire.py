from circle import Circle_05b


# created by third customer

class Tire(Circle_05b):
    """Tires are circles with a corrected perimeter"""

    def perimeter(self):
        """Circumference corrected for the rubber"""
        return Circle_05b.perimeter(self) * 1.25
