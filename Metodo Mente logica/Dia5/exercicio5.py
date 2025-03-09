# Peça ao usuário um número inteiro e exiba a tabuada desse número de 1 a 10.
numero = int(input("Digite um numero: "))

for contagem in range(1, 11):
        resultado = numero * contagem
        print(numero, "vezes", contagem, "é igual a:", resultado)
