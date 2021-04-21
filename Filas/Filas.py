import numpy as np

class FilaCircular:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __filaVazia(self):
        return self.numero_elementos == 0

    def __filaCheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__filaCheia():
            print('A fila esta cheia')
            return

        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.__filaVazia():
            print('A fila já esta vazia')
            return
        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade:
            self.inicio = 0
        self.numero_elementos -= 1
        return temp

    def primeiro(self):
        if self.__filaVazia():
            return-1
        return self.valores[self.inicio]


fila = FilaCircular(5)

print(fila.primeiro())

fila.enfileirar(2)
fila.enfileirar(3)
fila.enfileirar(5)


fila.enfileirar(1)
fila.enfileirar(7)



fila.desenfileirar()
fila.desenfileirar()
print(fila.primeiro())
