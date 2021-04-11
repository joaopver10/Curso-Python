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

    def pesq_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultimaP

        while True:
            posicao_atual = int((limite_inferior + limite_superior) / 2)
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            elif limite_inferior > limite_superior:
                return -1
            else:
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                else:
                    limite_superior = posicao_atual - 1

    def excluir(self, valor):
        posicao = self.pesq_binaria(valor)
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
print('----------------------')
print('----------------------')
print('----------------------')

print(vetor.pesq_binaria(4))
