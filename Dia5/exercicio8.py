#Exiba os primeiros N termos da série de Fibonacci.
#A série de Fibonacci começa com 0 e 1, e cada termo subsequente é a soma dos dois anteriores.
#Exemplo: 0, 1, 1, 2, 3, 5, 8, 13...

numero = int(input("Digite um numero positivo e maior que zero: "))

termo1 = 0
termo2 = 1
contador = 0

if numero <= 0:
    print("O numero tem que ser maior que 0")
else:
    print("Série Fibonacci:")
    while contador < numero:
        print(termo1)
        proximo_termo = termo1 + termo2
        termo1 = termo2
        termo2 = proximo_termo
        contador += 1

