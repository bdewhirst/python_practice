class Tire:
    def __repr__(self):
        return 'A rubber tire'


class FancyTire(Tire):
    # narrow/shallow hierarchy
    # doesn't depend on other objects
    # uses or specializes (specializes) all behavior of parent class
    def __repr__(self):
        return 'A fancy tire'


class Frame:
    def __repr__(self):
        return 'A bicycle frame'


class AluminumFrame(Frame):
    def __repr__(self):
        return 'An aluminum frame'


class CarbonFiberFrame(Frame):
    # narrow/shallow hierarchy
    # doesn't depend on other objects
    # uses or specializes (specializes) all behavior of parent class
    def __repr__(self):
        return 'A carbon fiber frame'


class Bicycle:
    def __init__(self, front_tire, back_tire, frame):
        self.front_tire = front_tire
        self.back_tire = back_tire
        self.frame = frame

    def print_specs(self):
        print(f'Frame: {self.frame}')
        print(f'Front tire: {self.front_tire}, back tire: {self.back_tire}')


if __name__ == '__main__':
    # each example demonstrates Likov substitutability-- you can use the child in place of the parent class
    bike = Bicycle(Tire(), Tire(), AluminumFrame())
    bike.print_specs()

    bike = Bicycle(FancyTire(), FancyTire(), CarbonFiberFrame())
    # example debug code from a PyCharm breakpoint set on the above line:
    # `print(type(bike))`
    # `print(type(bike.front_tire))`, etc.

    # `print(isinstance(FancyTire, Tire))`  # False
    # `print(isinstance(FancyTire(), Tire))`  # True
    # `print(isinstance(bike, Bicycle))`  # True
    # `print(isinstance(bike, Tire))`  # False
    # `print(issubclass(Tire, Tire))`  # True-- classes are considered subclasses of themself
    # `print(issubclass(FancyTire, Tire))`  # True
    # `print(issubclass(Tire, FancyTire))`  # False
    bike.print_specs()