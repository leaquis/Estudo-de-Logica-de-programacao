agenda = {}


def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    agenda[nome] = telefone
    print("Contato adicionado com sucesso!")


def buscar_contato():
    nome = input("Digite o nome do contato que você quer procurar: ")

    if nome in agenda:
        print(f"O telefone de {nome} é {agenda[nome]}")
    else:
        print("Contato não encontrado!")


def remover_contato():
    nome = input("Digite o nome do contato que você quer remover: ")

    if nome in agenda:
        del agenda[nome]
        print(f"O contato {nome} foi removido")
    else:
        print("Contato não encontrado!")


while True:
    print("\n --- Lista telefonica ---")
    print("O que você quer fazer?")
    print("1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Remover contato")
    print("4 - Sair")
    opcao = input()

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        buscar_contato()
    elif opcao == "3":
        remover_contato()
    elif opcao == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
