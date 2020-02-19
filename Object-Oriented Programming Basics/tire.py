# https://docs.python.org/3/tutorial/classes.html#classes
# https://docs.python.org/3.7/library/doctest.html

import math

class Tire:
    """
    Tire represents a tire that we would use with an automobile.
    """

    def __init__(self, tire_type, width, ratio, diameter, brand='', construction='R'):
        self.tire_type = tire_type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction

    def __repr__(self):
        """
        Represents the tires information in the standard notation present on the side of the tire
        Example: P215/65R15
        """
        return (f"{self.tire_type}{self.width}/{self.ratio}{self.construction}{self.diameter}")

    def circumference(self):
        """
        The circumference of the tire in inhes.

        >>> tire = Tire('P', 205, 65, 15)
        >>> tire.circumference()
        80.1
        """

        total_diameter  = self.side_wall_inches() * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def side_wall_inches(self):
        return (self.width * (self.ratio / 100)) / 25.4


class SnowTire(Tire):
    def __init__(self, tire_type, width, ratio, diameter, chain_thickness, brand='', construction='R'):
        super().__init__(tire_type, width, ratio, diameter, brand, construction)
        self.chain_thickness = chain_thickness

    def circumference(self):
        """
        Circumference of the tire w/ snow chains in inches.

        >>> tire = SnowTire('P', 205, 65, 15, 2)
        >>> tire.circumference()
        92.7
        """

        total_diameter = (self.side_wall_inches() + self.chain_thickness) * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def __repr__(self):
        return super().__repr__() + " (snow)"