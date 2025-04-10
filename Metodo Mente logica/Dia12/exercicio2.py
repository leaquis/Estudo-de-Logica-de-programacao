def leitorDeArquivos():
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
        print("Arquivo lido!")
        print(conteudo)
    finally:
        print("Operação finalizada")
        if 'arquivo' in locals():
            arquivo.close()
            print("Arquivo fechado!")
