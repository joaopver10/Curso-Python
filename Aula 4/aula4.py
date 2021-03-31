nota = media = soma = 0

for _ in range(1, 6):
    nota = float(input("Digite uma nota: "))
    soma += nota

print(f"A soma é {soma}")

media = soma / 5
print(f"A média é: {media}")

tabuada = 3

for num in range(1, 11):
   print(f'a tabuada ficou {tabuada} x {num} = {tabuada * num}')
