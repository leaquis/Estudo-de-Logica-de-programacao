# algoritmos - para resolver problemas complexos de forma perfomatica

# recursão - funcao chama ela mesma para resolver problemas
def contar_regressivamente(n):
    if n <= 0:
        print("Fim!")
    else: 
        print(n)
        contar_regressivamente(n - 1)


# recursão é como se fosse um loop só que com funções
contar_regressivamente(10)



#fatorial -> multiplicação de um numero e os seus antecessores
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


print(fatorial(5))


# pesquisa binaria recursiva

# lista -> procurar um numero
# divide a lista em 2 e procura o numero nas partes
# inicio -> onde eu quero começar a busca
#fim -> até qual indice eu quero fazer a busca
def pesquisa_binaria(lista, alvo, inicio=0, fim= None):
    if fim is None:
        fim = len(lista) - 1

    if inicio > fim:
        return -1
    
    meio = (inicio + fim) // 2

    if lista[meio] == alvo:
        return meio
    elif lista[meio] < alvo:
        return pesquisa_binaria(lista, alvo, meio + 1, fim)
    else:
        return pesquisa_binaria(lista, alvo, inicio, fim - 1)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(f"Indice do elemento 7: {pesquisa_binaria(lista, 7)}")
