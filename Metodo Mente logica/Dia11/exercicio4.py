numeros1 = input("Digite números separados por espaço para o primeiro conjunto de numeros: ").split()
numeros2 = input("Digite números separados por espaço para o segundo conjunto de numeros: ").split()

conjunto1 = set(numeros1)
conjunto2 = set(numeros2)

uniao = conjunto1.union(conjunto2)
intersecao = conjunto1.intersection(conjunto2)

print(f"A união dos conjuntos é {uniao} e a interseção dos conjuntos é {intersecao}")
