#Peça ao usuário um número inteiro positivo N e calcule a soma de todos os números de 1 a N.
numero = int(input("Digite um numero positivo e maior que zero:"))
contagem = 0
soma = 0

if numero == 0:
    print("O numero tem que ser maior que zero!")
elif numero > 0:
    for contagem in range(1, numero + 1):
        soma += contagem
        print(soma)
else:
    print("O numero tem que ser positivo")