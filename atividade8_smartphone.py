class Smartphone:
    def __init__(self, marca, modelo, capacidade_bateria):
        self.marca = marca
        self.modelo = modelo
        self.capacidade_bateria = capacidade_bateria
    
    def carregar(self, minutos):
        print(f"O smartphone {self.marca} {self.modelo} está carregando por {minutos} minutos.")

if __name__ == "__main__":
    smartphone1 = Smartphone(marca="Samsung", modelo="Galaxy S21", capacidade_bateria=4000)
    smartphone2 = Smartphone(marca="Apple", modelo="iPhone 17 Pro Max", capacidade_bateria=5300)

    smartphone1.carregar(minutos=30)
    smartphone2.carregar(minutos=45)
    