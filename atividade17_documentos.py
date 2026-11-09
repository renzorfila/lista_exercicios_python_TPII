class DocumentoPDF:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def imprimir(self):
        print(f"Documento PDF: {self.titulo} por {self.autor}.")

class DocumentoWord:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def imprimir(self):
        print(f"Documento Word: {self.titulo} por {self.autor}.")

def processar_impressao(documento):
    documento.imprimir()

if __name__ == "__main__":
    pdf = DocumentoPDF(titulo="Relatório Anual", autor="João Silva")
    word = DocumentoWord(titulo="Carta de Apresentação", autor="Maria Oliveira")

    processar_impressao(pdf)
    processar_impressao(word)