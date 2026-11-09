class Smartphone:
    def __init__(self, marca, modelo, capacidade_bateria):
        self.marca = marca
        self.modelo = modelo
        self.capacidade_bateria = capacidade_bateria
    
    def carregar(self, minutos):
        print(f"O smartphone {self.marca} {self.modelo} está carregando por {minutos} minutos.")

if __name__ == "__main__":
    smartphone = Smartphone(marca="Samsung", modelo="Galaxy S21", capacidade_bateria=4000)
    smartphone.carregar(minutos=30)
    
