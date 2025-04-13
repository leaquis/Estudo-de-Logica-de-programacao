# padrões de projeto

# formas de programar que vão trazer resultados benéficos para a nossa aplicação

# singleton
# garantir que uma classe tenha apenas uma instancia
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            print("Instancia singleton criada")
        return cls._instance


obj1 = Singleton()
obj2 = Singleton()


# padrão factory(fabrica)
# define uma interface para criar objetos, mas permite que subclasses decidam qual objeto criar

from abc import ABC, abstractmethod


class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass # sera implementado em uma subclasse

# fabrica de transportes, criar: carros e barcos
# a fábrica exige um método mover

class Carro(Transporte):
    def mover(self):
        print("O carro esta se movendo!")


class Barco(Transporte):
    def mover(self):
        print("O barco esta se movendo!")


class FabricaTransporte:
    def criar_transporte(self, tipo):
        if tipo == "carro":
            return Carro()
        elif tipo == "barco":
            return Barco()
        else:
            raise ValueError("Tipo de transporte desconhecido")
        

fabrica = FabricaTransporte()

Tranporte1 = fabrica.criar_transporte("carro")
Tranporte2 = fabrica.criar_transporte("barco")

Tranporte1.mover()
Tranporte2.mover()
