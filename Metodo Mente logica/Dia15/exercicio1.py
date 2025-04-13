# criar a classe retangulo que recebe largura e altura
# criar o metodo que calcula a area
# criar o metodo que calcula o perimetro

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcArea(self):
        area = self.largura * self.altura
        print(f"A area do retangulo é {area}")
    
    def calcPerimetro(self):
        perimetro = 2 * (self.largura + self.altura)
        print(f"O perimetro do retangulo é {perimetro}")


retangulo1 = Retangulo(10, 5)    

retangulo1.calcArea()
retangulo1.calcPerimetro()
