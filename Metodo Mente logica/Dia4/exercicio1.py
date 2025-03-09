#comissão de vendas
# >= 100 = 2%
# >= 500 = 1%
# < 500 = 0.5%

venda = 1200

if venda >= 1000:
    comissao = venda * .02
    print("A comissão da venda sera: R$", comissao)
elif venda >= 500:
    comissao = venda * .01
    print("A comissão da venda sera: R$", comissao)
else:
    comissao = venda * .005
    print("A comissão da venda sera: R$", comissao)
    