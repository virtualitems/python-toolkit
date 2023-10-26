"""
Demostración del principio de sustitución de Liskov.
"""


from abc import ABC, abstractmethod


class Notification(ABC):
    """
    Clase abstracta para notificaciones.
    """
    @abstractmethod
    def notify(self, message):
        """
        Envía el mensaje por el canal de notificaciones.
        """

class Email(Notification):
    """
    Clase concreta para notificaciones por email.
    """
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Enviado "{message}" para {self.email}')


class SMS(Notification):
    """
    Clase concreta para notificaciones por SMS.
    """
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Enviado "{message}" para {self.phone}')


class Contact:
    """
    Clase que representa un contacto.
    """
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    """
    Gestor de notificaciones.

    @property notification (Notification) Canal de notificación a utilizar.
    """
    def __init__(self):
        self.notification = None

    def send(self, message):
        """Envía el mensaje por el canal de notificaciones."""

        if self.notification is None:
            raise Exception('No hay canal de notificación')

        self.notification.notify(message)


def main():
    """Función principal"""

    # información de contacto
    contact = Contact('John Doe', 'john@doe.com', '+1 234 567 890')

    # gestor de notificaciones
    notification_manager = NotificationManager()

    # envío a SMS
    sms_notification = SMS(contact.phone)
    notification_manager.notification = sms_notification
    notification_manager.send('Hi John')

    # envío a email
    email_notification = Email(contact.email)
    notification_manager.notification = email_notification
    notification_manager.send('Hello John')

    # la clase NotificationManager puede funcionar
    # con cualquier clase que implemente la interfaz Notification.


if __name__ == '__main__':
    main()
