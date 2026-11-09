class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def trabalhar(self):
        print(f"{self.nome} está trabalhando.")

class Gerente(Funcionario):
    def __init__(self, nome, salario, senha_sistema):
        super().__init__(nome, salario)
        self.senha_sistema = senha_sistema
        
    def gerenciar(self):
        print(f"{self.nome} está gerenciando a equipe.")
        

if __name__ == "__main__":
    gerente= Gerente(nome="Renzo Orfila", salario=5000, senha_sistema="1234")
    gerente.trabalhar()
    gerente.gerenciar()
    print(f"Nome: {gerente.nome}, Salário: {gerente.salario}, Senha do Sistema: {gerente.senha_sistema}")