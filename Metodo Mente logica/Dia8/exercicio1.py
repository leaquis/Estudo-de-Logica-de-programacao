# encoding: utf-8

# criar função que converte fahrenheit para celsius

f = float(input("Digite a temperatura em fahrenheit: "))


def conversao(f):
    celsius = (f - 32) * 5 / 9
    return celsius


celsius = conversao(f)

print(f"{f} graus em Fahrenheit é equivalente a {celsius} graus celsius")
