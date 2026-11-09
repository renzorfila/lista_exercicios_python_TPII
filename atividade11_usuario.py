class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Administrador(Usuario):
    def __init__(self, nome, email, nivel_acesso):
        super().__init__(nome, email)
        self.nivel_acesso = nivel_acesso

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Email: {self.email}, Nível de Acesso: {self.nivel_acesso}")

if __name__ == "__main__":
    admin = Administrador(nome="Renzo Orfila", email="renzorfila@hotmail.com", nivel_acesso="Administrador")
    admin.exibir_informacoes()  
    