#lista
lista1 = []
for i in range(1, 6):
   recebe = int(input("Digite um numero:"))
   lista1.append(recebe)


print(lista1)

soma = 0

for i in range(len(lista1)):
    soma += lista1[i]

print('Soma: ', soma)

