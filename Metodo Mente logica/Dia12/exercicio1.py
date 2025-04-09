def divisaoSegura():
    try:
        numero1 = float(input("Digite o primeiro numero da divisão: "))
        numero2 = float(input("Digite o segundo numero da divisão: "))
        resultado = numero1 / numero2
    except (ValueError, ZeroDivisionError) as error:
        print("Erro: ", error)
    else:
        print(f"O resultado é: {resultado}")
    finally:
        print("Operação concluída")


divisaoSegura()
