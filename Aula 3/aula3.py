m1 = float(input("Digite a nota 1:"))
m2 = float(input("Digite a nota 2:"))
m3 = float(input("Digite a nota 3:"))
exame = False


media = (m1 + m2 + m3) / 3


if media >= 0.0 and media <= 4.0:
    print("reprovado")
elif media >= 4.1 and media <= 6.0:
    print("Recuperação")
    notaEx = float(input("Digite a nota do exame:"))
    if notaEx >= 6.0:
        print("Aprovado")
    else:
        print("Reprovado")
elif media > 6:
    print("Aprovado")



