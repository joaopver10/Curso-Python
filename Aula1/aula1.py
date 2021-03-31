tempoGasto = float(input('Digite o tempo gasto: '))
veloMedia = float(input('Digite a velocidade media '))
distancia = tempoGasto * veloMedia
litrosUsados = distancia / 12

print(f'O tempo gasto da viagem foi {tempoGasto} com a velocidade media de {veloMedia}')
print(f'A distancia percorrida {distancia} utilizou {litrosUsados} litros')
