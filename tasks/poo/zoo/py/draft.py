from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome:str):
        self.nome: str = nome

    def apresentar_nome(self):
        print("Eu sou um(a) {self.nome}!")
    @abstractmethod
    def fazer_som(self):
        pass
    @abstractmethod
    def mover(self):
        pass
class Gato(Animal):
    def __init__(self, nome:str):
        super().__init__(nome)

    def fazer_som(self):
        print("miauuuu")

    def mover(self):
        print("caminhada")

class Cobra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("sssss")
    def mover(self):
        print("rastejando")

class Cabrito(Animal):
    def __init__(self, nome:str):
        super().__init__(nome)

    def fazer_som(self):
        print("béééé")
class Corvo(Animal):
    def __init__(self, nome:str):
        super().__init__(nome)

    def fazer_som(self):
        print("uuh, uuuh")

    def mover(self):
        print("voa")

def apresentar(animal: Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print(f"The Type Object: {Type(animal).__name__}")
if __name__=="_main_":
    jujuba=Gato("jujuba")
    isabeli=Cobra("isinha")
    lupi=Cabrito("lupi")
    krovy= Corvo("krovy")
