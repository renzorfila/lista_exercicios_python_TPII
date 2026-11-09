class Cofrinho:
    def __init__(self):
        self.__saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def ver_saldo(self):
        return self.__saldo

if __name__ == "__main__":
    cofrinho = Cofrinho()
    cofrinho.depositar(200.0)
    print(f"Saldo atual: R${cofrinho.ver_saldo():.2f}")
