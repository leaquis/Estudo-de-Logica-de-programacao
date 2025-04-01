aluno = {
    "nome": "Giovani",
    "turma": "1A"
}

materia = input("Digite o nome da matéria: ")
nota = int(input("Digite a nota: "))


def adicionar_nota(materia, nota):
    aluno[materia] = nota


adicionar_nota(materia, nota)

print(aluno)
