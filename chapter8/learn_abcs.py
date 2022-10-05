from abc import ABC, abstractmethod


class Predator(ABC):
    @abstractmethod
    def eat(self, prey):
        pass

    def roar(self):
        print("Roar!")


class Bear(Predator):
    def eat(self, prey):
        print(f"Mauling {prey}!")


class Owl(Predator):
    def eat(self, prey):
        print(f"Swooping in on {prey}!")


class Chameleon(Predator):
    def eat(self, prey):
        print(f"Shooting tongue at {prey}!")


class Vegan(Predator):
    pass


if __name__ == "__main__":
    bear = Bear()
    bear.eat("deer")
    bear.roar()
    owl = Owl()
    owl.eat("mouse")
    chameleon = Chameleon()
    chameleon.eat("fly")
    vegan = Vegan()  # meant to throw an error
