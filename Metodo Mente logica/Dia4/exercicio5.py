#Situação: Uma loja oferece descontos com base no valor da compra.
#● Se o valor for maior ou igual a R$1000, o desconto é de 10%.
#● Se for entre R$500 e R$999, o desconto é de 5%.
#● Caso contrário, não há desconto.

valor_compra = 400

if valor_compra >= 1000:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print("Você tem direito a 10% de desconto")
    print("Valor a pagar: R$", valor_final)
elif valor_compra >= 500:
    desconto = valor_compra * 0.05
    valor_final = valor_compra - desconto
    print("Você tem direito a 05% de desconto")
    print("Valor a pagar: R$", valor_final)
else:
    print("Você não tem direito a desconto")
    print("Valor a pagar: R$", valor_compra)
