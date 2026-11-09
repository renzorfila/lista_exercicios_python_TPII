class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

class Caminhao(Veiculo):
    def __init__(self, marca, ano, capacidade_carga):
        super().__init__(marca, ano)
        self.capacidade_carga = capacidade_carga
    
    def exibir_informacoes(self):
        print(f"Caminhão - Marca: {self.marca}, Ano: {self.ano}, Capacidade de Carga: {self.capacidade_carga} kg")

if __name__ == "__main__":
    caminhao = Caminhao(marca="Volvo", ano=2022, capacidade_carga=20000)
    caminhao.exibir_informacoes()