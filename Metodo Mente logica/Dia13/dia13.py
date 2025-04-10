# como trabalhar com arquivos em python

# uma forma de ler o arquivo todo
with open('dados.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# ler o arquivo linha por linha
with open('dados.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())

# escrever em um arquivo
with open('saida.txt', 'w') as arquivo:
    arquivo.write("Nova linha \n")
    arquivo.write("Nova linha 2 \n")

# Quando não há o arquivo ele cria o arquivo
# Quando o arquivo já existe o write sobrescreve ele

# Adicionar conteudo - append - a
with open('saida.txt', 'a') as arquivo:
    arquivo.write("Nova linha 3 \n")
    
# r - read - ler
# w - write - escrever
# a - append - adicionar

# CSV - comma separeted values
import csv

with open("contatos.csv", "w", newline='') as arquivo_csv:
    # cabeçalho (colunas)
    # dados
    # dados
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['Nome', 'Profissão', 'Idade'])
    escritor.writerow(['Giovani', 'Programador', 27])
    escritor.writerow(['Roberta', 'Advogada', 29])
    escritor.writerow(['Erika', 'Quimica', 44])

# json - javascript object notation (APIs)

import json

dados = {
    'Nome': 'Giovani',
    'Idade': 27,
    'Profissão': 'Programador'
}

with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo, indent=4)
