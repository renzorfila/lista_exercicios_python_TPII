class Email:
    def __init__(self, remetente, destinatario, assunto, corpo):
        self.remetente = remetente
        self.destinatario = destinatario
        self.assunto = assunto
        self.corpo = corpo

    def enviar(self):
        print(f"E-mail enviado de {self.remetente} para {self.destinatario}")
        print(f"Assunto: {self.assunto}")
        print(f"Mensagem: {self.corpo}")
        print()

if __name__ == "__main__":
    email1 = Email(remetente="renzorfila@hotmail.com", 
    destinatario="professora@fatec.sp.gov.br", 
    assunto= "Entrega da atividade",
    corpo= "Professora, segue a atividade de POO em anexo."
    )

    email2= Email(remetente="renzorfila@hotmail.com",
    destinatario="colega@email;com",
    assunto= "Entrega da atividade",
    corpo= "Segue a atividade de POO em anexo."
    )

    email1.enviar()
    email2.enviar()