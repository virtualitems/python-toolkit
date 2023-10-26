"""
Demostración del principio de inversión de dependencias.
"""

from abc import ABC, abstractmethod

class Repository(ABC):
    """
    Representación un repositorio de datos.
    """

    @abstractmethod
    def get_data(self):
        """
        Obtiene los datos del repositorio.
        """


class InMemoryRepository(Repository):
    """
    Repositorio de datos SQL.

    @property data (list) Datos del repositorio.
    """

    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data


def list_all_data(repository):
    """
    Caso de uso para listar todos los datos.

    @param repository (Repository) Repositorio de datos.
    """
    for item in repository.get_data():
        print(item)


def main():
    """Función principal"""

    # datos de prueba
    data = [
        {'id': 1, 'name': 'name 1'},
        {'id': 2, 'name': 'name 2'},
        {'id': 3, 'name': 'name 3'},
    ]

    repository = InMemoryRepository(data)
    list_all_data(repository)

    # la función list_all_data depende de una abstracción de Repository
    # puede operar aún cuando no se conozca la implementación

    # lineas de dependencia:
    # sin interface: list_all_data -> InMemoryRepository
    # con interface: list_all_data -> Repository <- InMemoryRepository
    # como se puede notar, la dependencia con InMemoryRepository es inversa


if __name__ == '__main__':
    main()
