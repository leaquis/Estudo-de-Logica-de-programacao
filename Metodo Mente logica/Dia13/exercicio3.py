import json

try:
    with open('produtos.json', 'r') as arquivo:
        produtos = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
else:
    for produto in produtos:
        print(f"Nome: {produto['nome']}")
        print(f"Preço: {produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")
        print("-" * 20)
