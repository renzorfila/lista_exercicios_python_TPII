class TV:
    def Ligar(self):
        print("A TV está ligada.")

class ArCondicionado:
    def Ligar(self):
        print("O ar-condicionado está ligado com temperatura de 20 graus.")

def ligar_aparelho(aparelho: {ligar}):
    aparelho.Ligar()

if __name__ == "__main__":
    ligar_aparelho(TV())
    ligar_aparelho(ArCondicionado())
    
