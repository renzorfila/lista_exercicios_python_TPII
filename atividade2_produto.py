class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def valor_total_estoque(self):
        return self.preco * self.quantidade_estoque

if __name__ == "__main__":
    p1 = Produto(nome="Notebook", preco=3000, quantidade_estoque=10)
    p2 = Produto(nome="Smartphone", preco=1500, quantidade_estoque=14)
    print(f"Produto 1: {p1.nome}, com valor total em estoque de: R$ {p1.valor_total_estoque()}")
    print(f"Produto 2: {p2.nome}, com valor total em estoque de: R$ {p2.valor_total_estoque()}")
