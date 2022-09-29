# from examples in 7.1-7.2...

class Tire:
    def __repr__(self):
        return "a rubber tire"


class Frame:
    def __repr__(self):
        return "an aluminum frame"

class CarbonFrame:
    def __repr__(self):
        return "a carbon fiber frame"

class Bicycle:
    def __init__(self, front_tire, back_tire, frame):
        self.front_tire = front_tire
        self.back_tire = back_tire
        self.frame = frame

    def print_specs(self):
        print(f"Frame: {self.frame}")
        print(f"Front Tire: {self.front_tire} back tire: {self.back_tire}")

if __name__ == "__main__":
    # bike =  Bicycle(Tire(), Tire(), Frame())
    # bike.print_specs()
    cff_bike =  Bicycle(Tire(), Tire(), CarbonFrame())
    cff_bike.print_specs()