def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    

numero = int(input("Digite um numero para calcular o fatorial: "))
if numero < 0:
    print("Fatorial não existe para números negativos.")
else:
    resultado = fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}")
