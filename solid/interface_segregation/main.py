"""
Demostración del principio de segregación de interfaces.
"""


from abc import ABC, abstractmethod


class Flyable(ABC):
    """
    interface para las entidades que pueden volar.
    """
    @abstractmethod
    def fly(self):
        """
        Método abstracto para volar.
        """


class Swimable(ABC):
    """
    interface para las entidades que pueden nadar.
    """
    @abstractmethod
    def swim(self):
        """
        Método abstracto para nadar.
        """


class Animal:
    """
    Entidad que representa un animal.
    """

    def __init__(self, name):
        """
        @param name (str) Nombre del animal.
        """
        self.name = name

    def eat(self):
        """
        El animal come.
        """
        print(f'{self.name} está comiendo.')

    def sleep(self):
        """
        El animal duerme.
        """
        print(f'{self.name} está durmiendo.')


class Fish(Animal, Swimable):
    """
    Entidad que representa un pez.
    """

    def swim(self):
        """
        El pez nada.
        """
        print(f'{self.name} está nadando.')


class Bird(Animal, Flyable):
    """
    Entidad que representa un ave.
    """

    def fly(self):
        """
        El ave vuela.
        """
        print(f'{self.name} está volando.')


def main():
    """Función principal"""

    dog = Fish('koi')
    dog.eat() # el pez es un animal, puede comer
    dog.sleep() # el pez es un animal, puede dormir
    dog.swim() # el pez es apto para nadar

    parrot = Bird('parrot')
    parrot.eat() # el ave es un animal, puede comer
    parrot.sleep() # el ave es un animal, puede dormir
    parrot.fly() # el ave es apta para volar

    # cada clase implementa una interfaz especializada en una tarea específica


if __name__ == '__main__':
    main()
