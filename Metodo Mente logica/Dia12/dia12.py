# try, except, else, finally

# try = tentando fazer algo
# except = trata o erro
# else = para uma condição positiva
# finally = roda de qualquer jeito

try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: arquivo não encontrado")
else:
    print("Arquivo lido!")
    print(conteudo)
finally:
    print("Operação finalizada")
    if 'arquivo' in locals():
        arquivo.close()
        print("Arquivo fechado!")

try:
    numero = int(input("Digite um numero: "))
    resultado = 100 / numero
except ValueError:
    print("Entrada inválida, tente novamente!")
except ZeroDivisionError:
    print("Divisão por 0!")
else:
    print(f"O resultado é: {resultado}")
finally:
    print("Operação concluída")

try:
    numero = int(input("Digite um numero: "))
    resultado = 100 / numero
except (ValueError, ZeroDivisionError) as error:
    print("Erro: ", error)
else:
    print(f"O resultado é: {resultado}")
finally:
    print("Operação concluída")
