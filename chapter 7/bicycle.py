# from examples in 7.1-7.2...

class Tire:
    def __repr__(self):
        return "a rubber tire"

class Frame:
    def __repr__(self):
        return "an aluminum frame"

class Bicycle:
    def __init__(self):
        self.front_tire = Tire()
        self.back_tire = Tire()
        self.frame = Frame()

    def print_specs(self):
        print(f"Frame: {self.frame}")
        print(f"Front Tire: {self.front_tire} back tire: {self.back_tire}")

if __name__ == "__main__":
    bike =  Bicycle()
    bike.print_specs()