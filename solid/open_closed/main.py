"""
Demostración del principio de abierto a la extención y cerrado a la modificación.
"""


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


class ResourceJSON:
    """
    Representación de un recurso en formato JSON.

    @property resource (Resource) Recurso a envolver.
    """

    def __init__(self, resource):
        self.resource = resource
        self.encoded = ResourceJSON.encode(resource)

    @classmethod
    def encode(cls, resource):
        """
        Codifica un recurso en formato JSON.

        @param resource (Resource) Recurso a codificar.
        @return (str) Recurso codificado en formato JSON.
        """
        return f'{{"name": "{resource.name}"}}'


class ResourceXML:
    """
    Representación de un recurso en formato XML.

    @property resource (Resource) Recurso a envolver.
    """

    def __init__(self, resource):
        self.resource = resource
        self.encoded = ResourceXML.encode(resource)

    @classmethod
    def encode(cls, resource):
        """
        Codifica un recurso en formato XML.

        @param resource (Resource) Recurso a codificar.
        @return (str) Recurso codificado en formato XML.
        """
        return f'<resource><name>{resource.name}</name></resource>'


def main():
    """Función principal"""

    resource = Resource('recurso 1')

    resource_json = ResourceJSON(resource)
    print('Recurso como JSON: ', resource_json.encoded)

    resource_xml = ResourceXML(resource)
    print('Recurso como XML: ', resource_xml.encoded)

    # en caso de agregar más formatos de representación,
    # se crean clases nuevas en vez de modificar las existentes.


if __name__ == '__main__':
    main()
