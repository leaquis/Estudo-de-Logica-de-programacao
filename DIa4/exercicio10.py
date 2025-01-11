#pedra papel e tesoura
import random

opcoes = ["pedra", "papel", "tesoura"]

jogador = input("Escolha entra Pedra, Papel ou Tesoura: ").lower()
computador = random.choice(opcoes)

if jogador == "pedra" or jogador == "tesoura" or jogador == "papel":
    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or (jogador == "tesoura" and computador == "papel") or (jogador == "papel" and computador == "pedra"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
else:
    print("Opção indisponivel")

