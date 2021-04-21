class No:  # Classe para criar cada um dos nós

    def __init__(self, valor):
        self.valor = valor
        self.prox = None

    def mostra_no(self):
        print(self.valor)


class ListaEncadeada:  # Armazena as estruturas de todos os nós

    def __init__(self, nodecount=0):
        # independente da quantidade continua executando a mesma quantidade de passos
        # a complexidade é O(1)
        self.primeiro = None
        self.nodecount = nodecount

    def insere_inicio(self, valor):  # O(1)
        novo = No(valor)
        novo.prox = self.primeiro
        self.primeiro = novo
        self.nodecount = self.nodecount + 1

    def bubbsort(self):  # a complexidade no pior caso é O(n²) pois temos duas estruturas de repetição
        for i in range(self.nodecount - 1):
            atual = self.primeiro
            proximo = atual.prox
            anterior = None
            while proximo:
                if atual.valor > proximo.valor:
                    if anterior == None:
                        anterior = atual.prox
                        proximo = proximo.prox
                        anterior.prox = atual
                        atual.prox = proximo
                        self.primeiro = anterior
                    else:
                        temp = proximo
                        proximo = proximo.prox
                        anterior.prox = atual.prox
                        anterior = temp
                        temp.prox = atual
                        atual.prox = proximo
                else:
                    anterior = atual
                    atual = proximo
                    proximo = proximo.prox
            i = i + i

    def mostrar(self):  # O(n)
        if self.primeiro == None:
            print('A lista está vazia')
            return None

        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.prox

    def pesquisa(self, valor):  # O(n)
        if self.primeiro == None:
            print('A lista está vazia')
            return None

        atual = self.primeiro
        while atual.valor != valor:
            if atual.prox == None:
                return None
            else:
                atual = atual.prox
        return atual

    def excluir_inicio(self):  # O(1)
        if self.primeiro == None:
            print('A lista está vazia')
            return None

        temp = self.primeiro
        self.primeiro = self.primeiro.prox
        return temp

    def excluir_posicao(self, valor):  # O(n) A complexidade aumenta dependendo da entrada de dados
        if self.primeiro == None:
            print('A lista está vazia')
            return None

        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if atual.prox == None:
                return None
            else:
                anterior = atual
                atual = atual.prox

        if atual == self.primeiro:
            self.primeiro = self.primeiro.prox
        else:
            anterior.proximo = atual.prox

        return atual


lista = ListaEncadeada()
lista.insere_inicio(20)
lista.insere_inicio(10)
lista.insere_inicio(30)
lista.insere_inicio(40)
lista.insere_inicio(5)

print(lista.mostrar())

print('----------')

print('Depois de Ordernar a lista')

print('----------')

lista.bubbsort()
print(lista.mostrar())
