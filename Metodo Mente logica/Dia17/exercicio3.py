def contagem_regresiva(n):
    if n == 0:
        print(n)
    else:
        print(n)
        contagem_regresiva(n - 1)


n = int(input("Digite um numero para fazer a contagem regressiva: "))

if n < 0:
    print("O numero não pode ser negativo")
else:
    contagem_regresiva(n)