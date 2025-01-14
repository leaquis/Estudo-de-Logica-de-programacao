# Crie um jogo em que o programa escolhe um número aleatório entre 1 e 100, e o usuário tenta adivinhar. O programa deve dar dicas se o número é maior ou menor do que o palpite.
# O jogo continua até o usuário acertar.
import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    escolha = int(input("Digite um numero de 1 a 100:"))
    tentativas += 1

    if escolha == numero_secreto:
        print(f"Parabens! Você acertou em {tentativas} tentativas.")
        break
    elif escolha < numero_secreto:
        print("O número é maior.")
    else:
        print("O número é menor.")
