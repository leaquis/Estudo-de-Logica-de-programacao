from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def desenhar(self):
        pass


class Circulo(Forma):
    def desenhar(self):
        print("Desenhando um círculo.")


class Quadrado(Forma):
    def desenhar(self):
        print("Desenhando um quadrado.")


class Triangulo(Forma):
    def desenhar(self):
        print("Desenhando um triângulo.")


class FabricaForma:
    def criar_forma(self, tipo):
        if tipo == "circulo":
            return Circulo()
        elif tipo == "quadrado":
            return Quadrado()
        elif tipo == "triangulo":
            return Triangulo()
        else:
            raise ValueError("Tipo de forma desconhecido.")


fabrica = FabricaForma()

forma1 = fabrica.criar_forma("circulo")
forma1.desenhar()

forma2 = fabrica.criar_forma("quadrado")
forma2.desenhar()

forma3 = fabrica.criar_forma("triangulo")
forma3.desenhar()

forma4 = fabrica.criar_forma("retangulo")
forma4.desenhar()
