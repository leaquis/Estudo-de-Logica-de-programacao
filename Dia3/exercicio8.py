#Crie um programa que solicita um número inteiro ao usuário e verifica se ele é par ou ímpar.

numero = int(input("Digite um numero: "))

resto = numero % 2

if resto == 0:
    print("O numero é par!")
else:
    print("O numero é impar!")
