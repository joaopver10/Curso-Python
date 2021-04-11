import numpy as np


class VetorOrd:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaP = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def mostra(self):
        if self.ultimaP == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultimaP + 1):
                print(i, '-', self.valores[i])

    def insere(self, valor):
        if self.ultimaP == self.capacidade - 1:
            print('Capacidade maxima atingida')
            return

        posicao = 0
        for i in range(self.ultimaP + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultimaP:
                posicao = i + 1

        x = self.ultimaP

        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = valor
        self.ultimaP += 1

    def pesq_linear(self, valor):
        for i in range(self.ultimaP + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
            if i == self.ultimaP:
                return -1

    def excluir(self, valor):
        posicao = self.pesq_linear(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultimaP):
                self.valores[i] = self.valores[i + 1]
            self.ultimaP -= 1


vetor = VetorOrd(10)
vetor.insere(6)
vetor.insere(4)
vetor.insere(1)
vetor.insere(3)
vetor.insere(2)
vetor.insere(8)
vetor.insere(9)
vetor.mostra()
print(vetor.pesq_linear(33))
print('----------------------')
print('----------------------')
print('----------------------')
vetor.excluir(3)
vetor.excluir(33)
vetor.mostra()
