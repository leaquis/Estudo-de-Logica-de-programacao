#classificação de idade
idade = int(input("Digite a sua idade: "))

if idade <= 12 and idade >= 0:
    print("Você é uma criança")
elif idade <= 17:
    print("Você é um adolescente")
elif idade <= 59:
    print("Você é um adulto")
elif idade >= 60:
    print("Você é um idoso")
else:
    print("Idade inválida")
