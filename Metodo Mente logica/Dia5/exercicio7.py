#Peça ao usuário um número inteiro positivo e calcule o fatorial desse número.
#Fatorial de N (N!) é o produto de todos os números inteiros positivos de 1 até N.
#Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input("Digite um numero positivo e maior que zero: "))
multiplica = 1

if numero <= 0:
    print("O numero tem que ser maior que 0")
else:
    for contagem in range(1, numero + 1):
        multiplica *= contagem
    print(f"O fatorial de {numero} é: {multiplica}") 
