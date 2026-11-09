class Instrumento:
    def __init__(self, nome):
        self.nome = nome

    def tocar(self):
        print(f"{self.nome} está tocando.")


class Violao(Instrumento):
    def __init__(self):
        super().__init__("Violão")

    def tocar(self):
        print(f"{self.nome}: dedilhando as cordas, plim plim plim.")


class Bateria(Instrumento):
    def __init__(self):
        super().__init__("Bateria")

    def tocar(self):
        print(f"{self.nome}: batendo nos tambores, tum tum tá!")


if __name__ == "__main__":
    violao = Violao()
    bateria = Bateria()

    violao.tocar()
    bateria.tocar()