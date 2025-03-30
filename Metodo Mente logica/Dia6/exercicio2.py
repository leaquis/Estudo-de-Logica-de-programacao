# Peça ao usuário para inserir uma lista de números (separados por espaço) e calcule:
# ● O maior número
# ● O menor número
# ● A soma dos números
# ● A média dos números

entrada = input("Digite números separados por espaço: ")
numeros = [float(num) for num in entrada.split()]
soma = 0

maior_numero = max(numeros)
menor_numero = min(numeros)

for n in numeros:
    soma += n
print("O maior numero da lista é: ", maior_numero)
print("O menor numero da lista é: ", menor_numero)
print("A soma dos numeros da lista é: ", soma)
media = soma / len(numeros)
print("E a média dos numeros da lista é: ", media)
