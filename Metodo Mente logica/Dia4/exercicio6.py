#Calculadora

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
print("sinais das operações: ")
print("+ -> soma ")
print("- -> subtração ")
print("* -> multiplicação ")
print("/ -> divisão ")
operacao = str(input("Digite o sinal da operação que você deseja fazer: "))

if operacao == "+":
    print("A operação escolhida foi SOMA")
    resultado = numero1 + numero2
    print("A soma dos dois numeros é: ", resultado)
elif operacao == "-":
    print("A operação escolhida foi SUBTRAÇÃO")
    resultado = numero1 - numero2
    print("A subtração dos dois numeros é: ", resultado)
elif operacao == "*":
    print("A operação escolhida foi MULTIPLICAÇÃO")
    resultado = numero1 * numero2
    print("A multiplicação dos dois numeros é: ", resultado)
elif operacao == "/":
    print("A operação escolhida foi DIVISÃO")
    if numero2 != 0:
        resultado = numero1 / numero2
        print("A divisão dos dois numeros é: ", resultado)
    else:
        print("Não é possivel dividir por 0")
else:
    print("Operação invalida!")
