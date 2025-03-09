#estrutura de repetição
#repetir N vezes
#onde N é um numero que nós mesmos definimos ou uma condição

frutas= ["maçã", "banana", "laranja"]

#for n in list:
# bloco repetindo

for fruta in frutas:
    print("Fruta: ", fruta)

for i in range(5):
    print("Num: ", i)

#while
contador = 0

while contador < 5:
    print("Numero While: ", contador)
    contador += 1

#loop com uma condição mal definida pode rodar infinitamente

for i in range(10):
    if i == 5:
        break
    print("Num for ", i)

# break => para o loop
#continue > pula uma execução

for i in range(10):
    if i == 5:
        continue
    print("Num for ", i)



