class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def miar(self):
        print(f"{self.nome} está miando.")

if __name__ == "__main__":
    gato = Gato(nome="Mingau", idade=2, raca="Siamês")
    print(f"Nome: {gato.nome}, Idade: {gato.idade}, Raça: {gato.raca}")
    gato.miar()