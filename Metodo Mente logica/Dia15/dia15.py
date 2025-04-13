# Orientação a objetos
# existe o paradigma procedural que lé o arquivo de cima  para baixo
# e exite o paradigma de orientado a objetos que tem classes e objetos

# calsse -> objeto
# classe é o molde do objeto
# instancio um objeto (criar um objeto)
class Pessoa:
    # caracteristicas e ações do objeto
    # nome = caracteristicas => propriedades e atributos
    # apresentar = ação => metodo
    def __init__(self, nome, idade):
        # colocar o valor do argumento no meu futuro objeto
        self.nome = nome
        self.idade = idade
    
    def apresentacao(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos de idade")

    def aniversario(self):
        self.idade += 1
        print(f"Eu fiz aniversario e agora a minha idade é {self.idade}")


pessoa1 = Pessoa("Giovani", 27)

pessoa1.apresentacao()
pessoa1.aniversario()

pessoa2 = Pessoa("Roberta", 29)

pessoa2.apresentacao()
