from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Guau!"

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Miau!"

# Uso
perro = Perro("pepe", 5)
gato = Gato("pepito", 3)

print(perro.hablar())
print(gato.hablar())
