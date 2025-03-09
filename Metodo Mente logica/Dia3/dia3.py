# Operadores aritmeticos

a = 5
b = 2

print("Adição: ", a + b)
print("Subtração: ",a - b)
print("Multiplicação: ",a * b)
print("Divisão: ",a / b)

# ** exponinciação
# // divisão inteira

print("Exponenciação: ",a ** b)
print ("Divisão inteira: ",a // b)

# operadores de comparação
x = 10
y = 5

print("Maior que: ", x > y)
print("Maior ou igual: ", x >= y)
print("Menor que: ", x < y)
print("Menor ou igual: ", x <= y)
print("Diferente que: ", x != y)
print("Igual a: ", x == y)

# operadores logicos
# AND, OR ou NOT

#unir comparações

idade = 20
possui_carteira = True

pode_dirigir = (idade >= 18) and possui_carteira

print("Pode dirigir? ", pode_dirigir)

#AND só é verdadeiro quando ambas operações são verdadeiras
#OR é verdadeira caso pelo menos uma das operações seja verdadeira

e_estudante = False
idade = 60
e_professor = False

meia_entrada = (idade >= 60) or e_estudante or e_professor

print("Tem direito a meia entrada? ", meia_entrada)

#NOT inverte um booleano

chovendo = True
nao_chovendo = not chovendo

print("Esta chovendo? ", chovendo)
print("Não esta chovendo? ", nao_chovendo)

