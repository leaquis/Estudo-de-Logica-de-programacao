#listas(array) e tuplas
#interligados com os loops - estruturas de repetição

carros = ["bmw", "fiat", "ford"]

#os indices começam a contar do 0
print(carros[0])
print(carros[2])

carros.append("vw")

print(carros[3])

carros[0] = "bmw eletrico"

print(carros[0])

print(carros)

carros.remove("fiat")

print(carros)

#metodos => append, remove

print(len(carros))

if "bmw eletrico" in carros:
    print("Achei!")

#tuplas
# cria (1, 2, 3)
#não pode mudificar

cores = ("vermelho", "verde", "amarelo", "azul", "preto", "branco")

print(cores)
print(cores[1])

for cor in cores:
    print("Cor: ", cor)

print(len(cores))

if "vermelho" in cores:
    print("Tem a cor vermelha!")

# cores.append("teste")
# cores[1] = "roxo"

#array/lista => modifica
#tuplas => não modifica

