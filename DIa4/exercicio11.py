#Uma empresa de táxi cobra uma tarifa básica de R$4.00, mais R$0.25 por quilômetro rodado. Crie um programa que calcula o valor total da corrida com base na distância percorrida.

distancia = float(input("Digite a distancia percorrida em KM: "))

valor_final = 4 + (0.25 * distancia)

print(f"O valor final da corrida foi: R${valor_final:.2f}")
