import numpy as np

class FilaPrioridade:

    def __init__(self, capacidade):
        self.capacidade = capacidade
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

        if self.numero_elementos == 0:
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1
        else:
            x = self.numero_elementos - 1
            while x >= 0:
                if valor > self.valores[x]:
                    self.valores[x + 1] = self.valores[x]
                else:
                    break
                x -= 1
            self.valores[x + 1] = valor
            self.numero_elementos += 1
    def desenfileirar(self):
        if self.__filaVazia():
            print('A fila esta vazia')
            return
        valor = self.valores[self.numero_elementos - 1]
        self.numero_elementos -= 1
        return valor

    def primeiro(self):
        if self.__filaVazia():
            return-1
        return self.valores[self.numero_elementos - 1]


fila = FilaPrioridade(5)

fila.enfileirar(30)
fila.enfileirar(50)
fila.enfileirar(10)
print(fila.primeiro())