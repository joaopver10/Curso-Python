lista = []

try:
    valor = float(input('Digite um valor: '))
    valor2 = float(input('Digite outro valor: '))
    lista.append(valor)
    lista.append(valor2)
    divide = lista[0] / lista[1]
except ValueError:
    print('Valor digitado invalido')
except ZeroDivisionError:
    print('Erro na divisão')
except IndexError:
    print('Erro na divisão devido a posição da lista')
except KeyboardInterrupt:
    print('Foi parada pelo usuario')
else:
    print(f'A divisão foi de {divide}')