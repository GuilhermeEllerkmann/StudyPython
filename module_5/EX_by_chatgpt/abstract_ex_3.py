# Exercício 3: Sistema de Notificação
# Descrição: Elabore uma classe abstrata Notificador com um método abstrato enviar_notificacao. 
# Esta classe servirá como base para diferentes tipos de notificadores. 
# Implemente classes derivadas como NotificadorEmail, NotificadorSMS e NotificadorPush, 
# onde cada classe fornece sua própria implementação do método enviar_notificacao, detalhando como a notificação é enviada.
from abc import ABC, abstractmethod

class Notification(ABC):
    
    def __init__(self, msg):
        self._msg = msg

    @abstractmethod
    def send_notification(self) -> bool:
        pass

class EmailNotification(Notification):
    _type_of_notification = 'Email'

    def send_notification(self) -> bool:
        print(f'{self._msg}. (Type of notification = {self._type_of_notification})')
        return True

class SmsNotification(Notification):
    _type_of_notification = 'SMS'

    def send_notification(self) -> bool:
        print(f'{self._msg}. (Type of notification = {self._type_of_notification})')
        return True

class PushNotification(Notification):
    _type_of_notification = 'Push'

    def send_notification(self) -> bool:
        print(f'{self._msg}. (Type of notification = {self._type_of_notification})')
        return True

def notificador(notificador: Notification) -> bool:
    check_notification = notificador.send_notification()

    if check_notification:
        return('Notificacao enviada')
    else:
        return('Notificacao nao enviada')

upa = notificador(SmsNotification('rola'))
print(upa)
