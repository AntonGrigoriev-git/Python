# Интерфейсы для адаптации
class Telephone:
    def send_sms(self, text: str):
        print(f'Send a text: {text}')


class Email:
    def send_email(self, subject: str, body: str):
        print(f'Send email with subject: {subject}, body: {body}')


class PublicAddressSystem:
    def broadcast(self, message: str):
        print(f'Broadcast: {message}')


# Целевой интерфейс
class Alert:
    def send_alert(self, message: str):
        raise NotImplementedError('Должен быть переопределен')
    

# Адаптеры
class TelephoneAdapter(Alert):
    def __init__(self, adapt: Telephone):
        self.adapt = adapt

    def send_alert(self, message: str):
        self.adapt.send_sms(message)


class EmailAdapter(Alert):
    def __init__(self, adapt: Email):
        self.adapt = adapt

    def send_alert(self, message: str):
        subject = 'Alert notification'
        body = message
        self.adapt.send_email(subject, body)


class PublicAddressSystemAdapter(Alert):
    def __init__(self, adapt: PublicAddressSystem):
        self.adapt = adapt

    def send_alert(self, message: str):
        self.adapt.broadcast(message)

    
# Клиентский код, использует новый интерфейс
def combine_alerts(alert_sms: Alert, alert_email: Alert, alert_broadcast: Alert, message: str):
    alert_sms.send_alert(message)
    alert_email.send_alert(message)
    alert_broadcast.send_alert(message)

old_telephone = Telephone()
old_email = Email()
old_public_address_system = PublicAddressSystem()

adapter_telephone = TelephoneAdapter(old_telephone)
adapter_email = EmailAdapter(old_email)
adapter_public_address_system = PublicAddressSystemAdapter(old_public_address_system)

combine_alerts(adapter_telephone, adapter_email, adapter_public_address_system, 'Alarm!')