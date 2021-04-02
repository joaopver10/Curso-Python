sair = 0

while sair != 4:
    print("")
    print("- Para Soma digite 1 ")
    print("- Para dividir digite 2 ")
    print("- Para multiplicar digite 3")
    print("- Para sair digite 4 ")
    numDigitado = int(input("Digite a opção escolhida: "))

    if numDigitado == 1:
        calculando = int(input("digite o primeiro numero: "))
        calculando2 = int(input("digite o segundo numero: "))
        print(f"A soma de {calculando} + {calculando2} é de {calculando + calculando2}")
    elif numDigitado == 2:
        print("Entrou")
    elif numDigitado == 3:
        print("Recuperou")
    else:
        print("Saindo...")
        break
