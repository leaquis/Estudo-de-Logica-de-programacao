frase = input("Digite uma frase: ")
palavras = frase.split()
frase_invertida = " ".join(reversed(palavras))
print(F"Frase invertida: {frase_invertida}")
