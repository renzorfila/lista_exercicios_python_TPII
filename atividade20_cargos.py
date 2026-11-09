class Cargo:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_bonus(self):
        return 0


class Desenvolvedor(Cargo):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)

    def calcular_bonus(self):
        return self.salario_base * 0.10


class Gerente(Cargo):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)

    def calcular_bonus(self):
        return self.salario_base * 0.20 + 1000


if __name__ == "__main__":
    dev = Desenvolvedor("Ana", 5000)
    gerente = Gerente("Bruno", 8000)

    print(f"{dev.nome}: bônus de R${dev.calcular_bonus():.2f}")
    print(f"{gerente.nome}: bônus de R${gerente.calcular_bonus():.2f}")