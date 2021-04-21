import numpy as np

class VetorN:
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
        if self.ultimaP == self.capacidade - 1 :
            print('Capacidade maxima atingida')
        else:
            self.ultimaP += 1
            self.valores[self.ultimaP] = valor

    def pesq_linear(self, valor):
        for i in range(self.ultimaP + 1):
            if valor == self.valores[i]:
                return i
        return -1

    def excluir(self, valor):
        posicao = self.pesq_linear(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultimaP):
                self.valores[i] = self.valores[i + 1]
            self.ultimaP -= 1

vetor = VetorN(5)

vetor.insere(2)
vetor.insere(3)
vetor.insere(4)
vetor.insere(5)
vetor.insere(6)

vetor.mostra()
print('-----')
vetor.excluir(2)

vetor.mostra()
