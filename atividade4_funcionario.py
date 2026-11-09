class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def promover(self, novo_cargo, aumento):
        self.cargo = novo_cargo
        self.salario += aumento
        print(f"{self.nome} foi promovido para {self.cargo} com um aumento de R${aumento:.2f}. Novo salário: R${self.salario:.2f}")

if __name__ == "__main__":
    funcionario = Funcionario(nome="João", cargo="Analista", salario=3000.00)
    funcionario.promover(novo_cargo="Gerente", aumento=1000.00)