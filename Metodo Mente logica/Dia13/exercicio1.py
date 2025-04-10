nome_arquivo = input("Digite o nome do arquivo completo: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: arquivo não encontrado")
except PermissionError:
    print("Erro: Sem permissão para ler o arquivo.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
else:
    palavras = conteudo.lower().split()
    contagem = {}

    for palavra in palavras:
        palavra = palavra.strip('.,!?";:-()')
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    for palavra, quantidade in contagem.items():
        print(f"{palavra}: {quantidade}")
