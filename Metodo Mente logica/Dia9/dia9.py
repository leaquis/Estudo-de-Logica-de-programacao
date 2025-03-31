# encoding: utf-8

# manipulação de strings

mensagem = "Isso é um texto"

print(mensagem)

# concatenação

primeiro_nome = "Giovani"
sobrenome = "Ramos"

print(primeiro_nome + " " + sobrenome)

nome_completo = primeiro_nome + " " + sobrenome

print(f"Olá, {nome_completo}")

# repetir
decoracao = "-" * 10

print(decoracao + " MENU " + decoracao)

# indexação
texto = "Python"

print(texto[3])

# fatiamento - slicing
frase = "Aprender Python é legal!"

print(frase[9:])
print(frase[9:15])  # começa no indice indicado e vai até -1 do indice final

# comprimento de uma string
print(len(frase))

# outra maneira de formatação
cidade = "São Paulo"

msg = "Eu moro em {}".format(cidade)
print(msg)

# mudar a case da string
texto = "Programação é Muito Legal"
print(texto.lower())
print(texto.upper())
print(texto.title())

# limpeza de espaços em branco
msg_com_espaco = "               Eu quero falar com o suporte                "
print(msg_com_espaco.strip())

# substituição
frase2 = "Eu gosto de Java"
nova_frase = frase2.replace("Java", "Python")

print(nova_frase)

# encontrando substring

texto2 = "Onde está a minha chave?"

posicao = texto2.find("chave")

print(f"A posição é {posicao}")


posicao2 = texto2.find("key")

print(f"A posição é {posicao2}")

# valor de -1 significa que não foi encontrado
if posicao2 == -1:
    print("Palavra não encontrada!")
