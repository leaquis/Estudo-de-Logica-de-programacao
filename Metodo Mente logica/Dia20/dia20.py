# Boas praticas

"""
    Calcula a média de notas

    Parametros:
        notas(lista): Lista contendo as notas
    Retorna:
        média(float): Média das notas
"""
def calcular_media(notas):
    return sum(notas) / len(notas)


print(calcular_media({10, 9, 8}))


# DRY (Dont Repeat Yourself)
def exibir_mensagem(mensagem, status=None):
    if status != None:
        print(mensagem + " - " + status)
        return
    else:
        print(mensagem)


exibir_mensagem("Mensagem 1",  "Alerta")
exibir_mensagem("Mensagem 2", "Sucesso")
exibir_mensagem("Mensagem 3", "Alerta")

# recursos da linguagem - para não reinventar a roda
numeros = [1, 2, 2, 3, 4, 5]
print(set(numeros))


# modularização
def soma(n1, n2):
    return n1 + n2


def calcular_soma_tarifas(t1, t2):
    return soma(t1, t2)


def calcular_soma_faturamento(f1, f2):
    return soma(f1, f2)


# Padrões de projetos, Kiss, DRY, Clean Code
