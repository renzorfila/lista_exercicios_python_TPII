class Eletrodomestico:
    def __init__(self, voltagem, preco):
        self.voltagem = voltagem
        self.preco = preco

class Microondas(Eletrodomestico):
    def __init__(self, voltagem, preco, potencia_watts):
        super().__init__(voltagem, preco)
        self.potencia_watts = potencia_watts

    def exibir_informacoes(self):
        print(f"Microondas - Voltagem: {self.voltagem}V, Preço: R${self.preco:.2f}, Potência: {self.potencia_watts}W")

if __name__ == "__main__":
    microondas = Microondas(voltagem=220, preco=499.99, potencia_watts=800)
    microondas.exibir_informacoes()