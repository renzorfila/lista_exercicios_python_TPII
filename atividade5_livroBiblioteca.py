class LivroBiblioteca:
    def __init__(self, titulo, autor, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado com sucesso.")
        else:
            print(f"O livro '{self.titulo}' não está disponível para empréstimo.")

if __name__ == "__main__":
    livro = LivroBiblioteca(titulo="1984", autor="George Orwell", disponivel=True)
    livro.emprestar()
    livro.emprestar()  