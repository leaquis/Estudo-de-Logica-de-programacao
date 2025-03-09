#Crie um programa para uma instituição bancária que analisa o pedido de empréstimo.
#● O cliente deve informar o valor do empréstimo, a renda mensal e o número de parcelas.
#● O empréstimo será aprovado se o valor da parcela não exceder 30% da renda mensal.

valor_emprestimo = float(input("Digite o valor do emprestimo que você deseja: R$"))
renda_mensal = float(input("Digite o valor da sua renda mensal: R$"))
n_parcelas = int(input("Digite o numero de parcelas desejado:"))

valor_parcela = valor_emprestimo / n_parcelas
limite_parcela = renda_mensal * 0.30

if valor_parcela <= limite_parcela:
    print("Emprestimo aprovado!")
    print(f"o valor da parcela sera: R${valor_parcela: .2f}")
else:
    print("Emprestimo negado!")
    print(f"o valor da parcela R${valor_parcela: .2f} excede os 30% da renda mensal")
