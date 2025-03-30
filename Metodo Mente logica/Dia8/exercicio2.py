# encoding: utf-8

while True:
    print("\nCalculadora")
    print("Qual operação você quer fazer?")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    operacao = input()

    def n1():
        primeiro_numero = float(input("Digite o primeiro numero: "))
        return primeiro_numero
    
    def n2():
        segundo_numero = float(input("Digite o segundo numero: "))
        return segundo_numero

    def soma():
        numero1 = n1()
        numero2 = n2()
        resultado = numero1 + numero2
        return resultado
 
    def subtracao():
        numero1 = n1()
        numero2 = n2()
        resultado = numero1 - numero2
        return resultado
 
    def multiplicacao():
        numero1 = n1()
        numero2 = n2()
        resultado = numero1 * numero2
        return resultado
 
    def divisao():
        numero1 = n1()
        numero2 = n2()
        if numero2 != 0:
            resultado = numero1 / numero2
            return resultado
        else:
            resultado = "inválido, divisão por 0"
            return resultado

    if operacao == "1":
        print(f"O resultado da soma é {soma()}")
    elif operacao == "2":
        print(f"O resultado da subtração é {subtracao()}")
    elif operacao == "3":
        print(f"O resultado da multiplicação é {multiplicacao()}")
    elif operacao == "4":
        print(f"O resultado da divisão é {divisao()}")
    elif operacao == "5":
        print("Saindo do programa.")
        break
    else:
        print("opção inválida. Tente novamente.")
