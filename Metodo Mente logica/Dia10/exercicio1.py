import conversoes

while True:
    print("\n --- Conversor de temperaturas ---")
    print("Qual conversão você quer fazer?")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 - Celsius para Kelvin")
    print("4 - Kelvin para Celsius")
    print("5 - Sair")
    opcao = input()

    if opcao == "1":
        celsius = conversoes.temperatura()
        print(f"O a conversão da temperatura {celsius} graus celsius para fahrenheit é {conversoes.celsius_para_fahrenheit(celsius)}")
    elif opcao == "2":
        fahrenheit = conversoes.temperatura()
        print(f"O a conversão da temperatura {fahrenheit} graus fahrenheit para celsius é {conversoes.fahrenheit_para_celsius(fahrenheit)}")
    elif opcao == "3":
        celsius = conversoes.temperatura()
        print(f"O a conversão da temperatura {celsius} graus celsius para kelvin é {conversoes.celsius_para_kelvin(celsius)}")
    elif opcao == "4":
        kelvin = conversoes.temperatura()
        print(f"O a conversão da temperatura {kelvin} graus kelvin para celsius é {conversoes.kelvin_para_celsius(kelvin)}")
    elif opcao == "5":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
