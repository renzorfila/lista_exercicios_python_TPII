class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_valor_estoque(self):
        return self.preco * self.quantidade
    
if __name__ == "__main__":
    produto1 = Produto("Notebook", 3000, 10)
    produto2 = Produto("Smartphone", 1500, 14)
    produto3 = Produto("Tablet", 2000, 5)

    print(f"Produto: {produto1.nome}, Valor total em estoque: R$ {produto1.calcular_valor_estoque()}")
    print(f"Produto: {produto2.nome}, Valor total em estoque: R$ {produto2.calcular_valor_estoque()}")
    print(f"Produto: {produto3.nome}, Valor total em estoque: R$ {produto3.calcular_valor_estoque()}")