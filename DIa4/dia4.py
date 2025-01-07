#Condicionais -> estrutura if, else

idade = 17

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

#meia entrada -> menor de 18 anos ou esta estudando(escola ou faculdade)

estudante = True

if idade < 18 or estudante:
    print("Tem meia entrada")
else:
    print("Não tem meia entrada")

#nota S,A,B,C,D
# elif => uma condição intermediaria entre else e if

nota = 10

if nota >=9:
    print("Nota S")
elif nota >=8:
    print("Nota A")
elif nota >=7:
    print("Nota B")
elif nota >=6:
    print("Nota C")
else:
    print("Nota D")
