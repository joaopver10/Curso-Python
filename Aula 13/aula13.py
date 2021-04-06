with open('caminho para ler o arquivo') as tex:
    for linha in tex:
        print(linha)

with open('texto2.txt', 'w') as texto:
    texto.write('Olá todos')

with open('C:/Users/joaop/Documents/GitHub/Curso-Python/Aula 11/texto2.txt') as texto2:
    for linha in texto2:
        print(linha)
