class Email:
    def __init__(self, remetente, destinatario, assunto):
        self.remetente = remetente
        self.destinatario = destinatario
        self.assunto = assunto

    def enviar(self):
        print(f"Enviando email de {self.remetente} para {self.destinatario} com o assunto '{self.assunto}'.")

if __name__ == "__main__":
    email = Email(remetente="Renzo Orfila", destinatario="David Walison", assunto="Reunião de Projeto")
    email.enviar()
    