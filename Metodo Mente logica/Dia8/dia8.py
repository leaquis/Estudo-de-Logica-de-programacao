# encoding: utf-8

# def <=> function
def saudacao():
    print("Olá, seja bem-vindo!")


saudacao()

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
profissao = input("Qual é a sua profissão? ")


def saudacao_personalizada(nome):
    print(f"Olá {nome}, como você está?")


saudacao_personalizada(nome)


def apresentar_pessoa(nome, idade, profissao):
    print(f"Dados da Pessoa: Nome - {nome}, idade - {idade} anos, profissão - {profissao}")


apresentar_pessoa(nome, idade, profissao)


def soma (a, b):
    resultado = a + b
    return resultado


soma(5, 10)

x = 10

soma_x = x + soma(5, 10)

print(soma_x)

resultado_soma = soma(1, 99)

soma_y = 10 + resultado_soma

print(soma_y)
