"""
Demostración del patrón de diseño Abstract Factory.
"""


from factories import AbstractFactory, VictorianFactory, ModernFactory


def client_code(factory: AbstractFactory) -> None:
    """
    Código cliente o caso de uso.
    """

    # El código funciona a través de tipos abstractos: AbstractFactory y AbstractProduct.
    # Esto permite usar cualquier implementación de factory o Product.

    chair = factory.create_chair()
    table = factory.create_table()

    print( chair.be_awesome() )
    print( table.be_awesome() )

    print(end='\n\n')

    # Un producto puede usar otro producto de la misma familia.
    print( table.be_awesome_with_chair(chair) )


if __name__ == '__main__':
    print('Estilo victoriano:')
    client_code(VictorianFactory())

    print(end='\n\n')

    print('Estilo moderno:')
    client_code(ModernFactory())
