from abc import ABC, abstractmethod

class Predator(ABC):
    @abstractmethod
    def eat(self, prey):
        pass


class Bear(Predator):
    def eat(self, prey):
        print(f"Mauling {prey}!")

class Owl(Predator):
    def eat(self, prey):
        print(f"Swooping in on {prey}!")

class Chameleon(Predator):
    def eat(self, prey):
        print(f"Shooting tongue at {prey}!")

if __name__ == "__main__":
    bear = Bear()
    bear.eat("deer")
    owl = Owl()
    owl.eat("mouse")
    chameleon = Chameleon()
    chameleon.eat("fly")