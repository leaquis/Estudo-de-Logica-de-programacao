# dicionarios = objetos em outras linguagens

pessoa = {
    "nome": "Giovani",
    "profissao": "Suporte Técnico de TI",
    "idade": 27
}

print(pessoa['nome'])

print(f"Olá, o meu nome é {pessoa['nome']}, tenho {pessoa['idade']} anos de idade e a minha profissão é {pessoa['profissao']}")


# adição e atualização
pessoa['nota'] = 10
pessoa['profissao'] = "Programador"

print(pessoa)

# remoção
del pessoa['nota']

print(pessoa)

# conjunto (set)
lista = [1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 7, 7]

lista_unica = set(lista)

print(lista)

print(lista_unica)

lista_unica.add(8)
lista_unica.add(6)

lista_unica.remove(2)

print(lista_unica)


# união de conjuntos
lista_b = {1, 2, 3, 9, 10}

uniao = lista_unica.union(lista_b)

print(uniao)

# interseção

intersecao = lista_unica.intersection(lista_b)

print(intersecao)

# diferença

diferenca = lista_unica.difference(lista_b)

print(diferenca)


texto = "banana maçã laranja banana maçã banana"
palavras = texto.split()
contagem = {}
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
print(contagem)
