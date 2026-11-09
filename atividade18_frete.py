class FreteSedex:
    def calcular_preco(self, peso):
        return 15.00 + peso * 8.00


class FreteTransportadora:
    def calcular_preco(self, peso):
        return 30.00 + peso * 3.00


def exibir_frete(frete, peso):
    preco = frete.calcular_preco(peso)
    print(f"{type(frete).__name__} para {peso}kg: R${preco:.2f}")


if __name__ == "__main__":
    exibir_frete(FreteSedex(), 5)
    exibir_frete(FreteTransportadora(), 5)
    exibir_frete(FreteSedex(), 20)
    exibir_frete(FreteTransportadora(), 20)