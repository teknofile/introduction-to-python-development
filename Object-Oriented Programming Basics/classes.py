# https://docs.python.org/3/tutorial/classes.html#classes

class Car:
    """
    Car modesl a car w/ tires and an engine
    """

    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    
    def description(self):
        print(f"A car with an {self.engine} engine, and {self.tires} tires")