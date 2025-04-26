def calcular_fatorial():
    while True:
        try:
            numero = int(input("Digite um numero inteiro não negativo para calculo de fatorial: "))
            if numero < 0:
                print("Numero negativo!")
                continue
            break
        except ValueError:
            print("Entrada inválida")
    
    fatorial = 1

    for i in range(1, numero + 1):
        fatorial *= i
    
    print(f"fatorial de {numero} é {fatorial}")


calcular_fatorial()
