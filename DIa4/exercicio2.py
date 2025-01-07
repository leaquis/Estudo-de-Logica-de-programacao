#baseado numa entrada do usuario, verificar se o numero é ou não maior que zero

numero = float(input("Digite um numero: "))

if numero > 0:
    print("Numero maior que zero")
elif numero == 0:
    print("0 numero é zero")
else: 
    print("Numero menor que zero")
    