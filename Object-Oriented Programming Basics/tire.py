# https://docs.python.org/3/tutorial/classes.html#classes
# https://docs.python.org/3.7/library/doctest.html

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