#Crie um programa que calcula o IMC e verifica se a pessoa está dentro do peso ideal (IMC entre 18.5 e 24.9).

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

IMC = peso / (altura ** 2)

peso_ideal = (IMC >= 18.5) and (IMC <= 24.9)

print("Seu IMC é: ", IMC)

if peso_ideal:
    print("Você esta no peso ideal!")
else:
    print("Você não esta no peso ideal!")
