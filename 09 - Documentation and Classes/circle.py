""" Circuitious, LLC -
    An Advanced Circle Analytics Company

"""
import math


class Circle_01(object):
    """An advanced circle analytical toolkit"""

    version = '0.1'

    def __init__(self, radius):
        # Not a constructor, but an initializer (the object is already created when init is called) """
        self.radius = radius

    # version = '0.1'
    def area(self):
        """Performs quadrature on a shape of uniform radius"""
        return math.pi * self.radius ** 2.0

    # Don't add anything that isnt needed
    def perimeter(self):
        return 2.0 * math.pi * self.radius


class Circle_05b(object):
    """An advanced circle analytical toolkit"""

    version = '0.5b'

    def __init__(self, radius):
        # Not a constructor, but an initializer (the object is already created when init is called) """
        self.radius = radius

    def area(self):
        """Performs quadrature on a shape of uniform radius"""
        p = self.perimeter()
        r = p / math.pi / 2.0
        return math.pi * r ** 2.0

    # Don't add anything that isnt needed
    def perimeter(self):
        return 2.0 * math.pi * self.radius

    @classmethod  # Alternative constructor
    def from_bbd(cls, bbd):
        """Construct a circle from a bounding box diagoanl"""
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

    @staticmethod  # Clas method so you dont need an instance to call it, can just use (Circle.angle_to_grade)
    def angle_to_grade(angle):
        """Convert angle in degree to a precentage grade"""
        return math.tan(math.radians(angle)) * 100.0


class Circle_06(object):
    """An advanced circle analytical toolkit"""

    # flyweight design patern, makes instances take less memory
    __slots__ = ['diameter']
    version = '0.5b'

    def __init__(self, radius):
        # Not a constructor, but an initializer (the object is already created when init is called) """
        self.radius = radius

    def area(self):
        """Performs quadrature on a shape of uniform radius"""
        p = self.__perimeter()
        r = p / math.pi / 2.0
        return math.pi * r ** 2.0

    # Don't add anything that isnt needed
    def perimeter(self):
        return 2.0 * math.pi * self.radius

    __perimeter = perimeter

    @classmethod  # Alternative constructor
    def from_bbd(cls, bbd):
        """Construct a circle from a bounding box diagoanl"""
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

    @staticmethod  # Clas method so you dont need an instance to call it, can just use (Circle.angle_to_grade)
    def angle_to_grade(angle):
        """Convert angle in degree to a precentage grade"""
        return math.tan(math.radians(angle)) * 100.0

    @property  # can use dotted acces for method call
    def radius(self):
        """Radius of a circle"""
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0
