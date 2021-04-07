class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = self.media

    def media(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def mostra(self):
        print('Nome: ', self.nome)
        print('Nota 1: ', self.nota1)
        print('Nota 2: ', self.nota2)
        print('Média: ', self.media)

    def resultado(self):
        if self.media >= 6.0:
            print('aprovado')
        else:
            print('reprovado')


a1 = Aluno('joao', 8.5, 6.5)
media = a1.media()

print(a1.mostra())
print(a1.resultado())

aluno2 = Aluno('pedro', 4.5, 6.0)
media2 = aluno2.media()

print(aluno2.mostra())
print(aluno2.resultado())