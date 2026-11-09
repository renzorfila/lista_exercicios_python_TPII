class Lampada:
    def __init__(self, cor):
        self.cor = cor
        self.ligada = False

    def acender(self):
        self.ligada = True
        print(f"A lâmpada está acessa e sua cor é {self.cor}.")

if __name__ == "__main__":
    lampada = Lampada("branca")
    print(lampada.cor)
    lampada.acender()
