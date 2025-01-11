#identificar numeros pares e impares até 20
pares = 0
impares = 0

for i in range(1, 21):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de numeros pares = ", pares)
print("Quantidade de numeros impares = ", impares)
