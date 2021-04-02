#dicionario
alunos = {}

for i in range(1,4):
    nome = input('Digite seu nome: ')
    nota = float(input('Digite sua nota: '))
    alunos[nome] = nota

print(alunos)

soma = 0

for nota in alunos.values():
    soma += nota

print('A média é', soma / 3)