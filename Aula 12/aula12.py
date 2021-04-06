dicionarioAluno = {}

for i in range(1,3):
    nome = input('Digite o nome do aluno: ')
    nota = float(input('Digite a nota do aluno: '))
    dicionarioAluno[nome] = nota

with open('texto.txt', 'w') as texto:
    for nome, nota in dicionarioAluno.items():
        texto.write(f'{nome}, {nota}\n')

with open('C:/Users/joaop/Documents/GitHub/Curso-Python/Aula 12/texto.txt') as texto2:
    for linha in texto2:
        print(linha)
