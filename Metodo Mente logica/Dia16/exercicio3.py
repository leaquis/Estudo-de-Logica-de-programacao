from abc import ABC, abstractmethod


class Observador(ABC):
    @abstractmethod
    def atualizar(self, mensagem):
        pass


class Notificador:
    def __init__(self):
        self.observadores = []

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def remover_observador(self, observador):
        self.observadores.remove(observador)

    def notificar(self, mensagem):
        for observador in self.observadores:
            observador.atualizar(mensagem)


class Usuario(Observador):
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, mensagem):
        print(f"{self.nome} receber a mensagem: {mensagem}")


notificador = Notificador()
usuario1 = Usuario("Giovani")
usuario2 = Usuario("Roberta")

notificador.adicionar_observador(usuario1)
notificador.adicionar_observador(usuario2)

notificador.notificar("Nova atualização disponivel.")
