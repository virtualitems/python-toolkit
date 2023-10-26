"""
Demostración del principio de responsabilidad única.
"""


class SqlDatabase:
    """
    Acceso a la base de datos.
    """
    def save(self, resource):
        """
        @param resource (Resource) Recurso a guardar.
        """
        return print(f'{resource} fue guardado en una base de datos relacional.')


class NoSqlDatabase:
    """
    Acceso a la base de datos.
    """

    def save(self, resource):
        """
        @param resource (Resource) Recurso a guardar.
        """
        return print(f'{resource} fue guardado en una base de datos no relacional.')


class Resource:
    """
    Entidad de recurso.

    @property name (str) Nombre del recurso.
    """

    def __init__(self, name):
        """
        @param name (str) Nombre del recurso.
        """
        self.name = name.upper()

    def __str__(self):
        return self.name


def main():
    """Función principal"""

    # Éste objeto es responsable unicamente de representar un recurso.
    resource = Resource('recurso 1')

    # Éste objeto es responsable unicamente de la persistencia.
    sqlDatabase = SqlDatabase()
    sqlDatabase.save(resource)

    # La base de datos puede cambiar sin que afecte a la entidad de recurso.
    noSqlDatabase = NoSqlDatabase()
    noSqlDatabase.save(resource)


if __name__ == '__main__':
    main()
