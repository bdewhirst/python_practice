# cooperative multiinheritance exercise

class BigCat:
    def eats(self):
        return ['rodents']

class Lion(BigCat):
    def eats(self):
        return super().eats() + ['wildebeest',]  # n.b.

class Tiger(BigCat):
    def eats(self):
        return super().eats() + ['water buffalo',]    # n.b.

class Liger(Lion, Tiger):
    def eats(self):
        return super().eats() + ['rabbit', 'cow', 'pig', 'chicken',]

if __name__ == '__main__':
    lion = Lion()
    print("The lion eats", lion.eats())
    tiger = Tiger()
    print("The tiger eats", tiger.eats())
    liger = Liger()
    print("The liger eats", liger.eats())
