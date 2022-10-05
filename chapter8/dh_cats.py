class BigCat:
    def eats(self):
        return ["rodents"]


class Lion(BigCat):
    def eats(self):
        return ["wildebeest"]


class Tiger(BigCat):
    def eats(self):
        return ["water buffalo"]


class Liger(Lion, Tiger):
    def eats(self):
        return super().eats() + [
            "rabbit",
            "cow",
            "pig",
            "chicken",
        ]


if __name__ == "__main__":
    lion = Lion()
    print("The lion eats", lion.eats())
    tiger = Tiger()
    print("The tiger eats", tiger.eats())
    liger = Liger()
    print("The liger eats", liger.eats())
    # before running-- should be all of the enumerated critters from tiger, lion, and liger-- and rodents? (no.)
    # ... I gather the author is about to explain inheritance priority (term of art is resolution order, but basically)
