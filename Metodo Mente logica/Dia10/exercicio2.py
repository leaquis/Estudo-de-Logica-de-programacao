import os


def manipular_arquivos():
    os.mkdir('nova_pasta')
    print("Pasta 'nova_pasta' criada.")

    os.chdir('nova_pasta')
    print("Se movendo para a  'nova_pasta' que foi criada.")

    with open('arquivo.txt', 'w') as arquivo:
        arquivo.write("Este é um arquivo dentro da nova pasta.")
    print("Arquivo 'arquivo.txt' criado dentro de 'nova_pasta'")

    arquivos = os.listdir('.')
    print("Arquivos no diretório atual: ", arquivos)


manipular_arquivos()
