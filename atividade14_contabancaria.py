class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def exibir_informacoes(self):
        print(f"Titular: {self.titular}, Saldo: R$ {self.saldo:.2f}")

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo, taxa_rendimentos):
        super().__init__(titular, saldo)
        self.taxa_rendimentos = taxa_rendimentos

    def calcular_juros(self):
        self.saldo += self.saldo * (self.taxa_rendimentos / 100)


if __name__ == "__main__":
    conta_poupanca = ContaPoupanca(titular="Renzo Orfila", saldo=1000.00, taxa_rendimentos=5.0)
    conta_poupanca.calcular_juros()
    conta_poupanca.exibir_informacoes()