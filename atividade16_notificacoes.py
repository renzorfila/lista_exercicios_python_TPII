class Notificacao:
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def enviar(self):
        print(f"Enviando notificação: {self.mensagem}")

class NotificacaoEmail(Notificacao):
    def __init__(self, mensagem, destinatario):
        super().__init__(mensagem)
        self.destinatario = destinatario

    def enviar(self):
        print(f"Enviando e-mail para {self.destinatario}: {self.mensagem}")

class NotificacaoSMS(Notificacao):
    def __init__(self, mensagem, numero_telefone):
        super().__init__(mensagem)
        self.numero_telefone = numero_telefone

    def enviar(self):
        print(f"Enviando SMS para {self.numero_telefone}: {self.mensagem}")

if __name__ == "__main__":
    email = NotificacaoEmail(mensagem="Sua conta foi atualizada.", destinatario="user@example.com")
    email.enviar()
    sms = NotificacaoSMS(mensagem="Você tem uma nova mensagem.", numero_telefone="+5511999999999")
    sms.enviar()
