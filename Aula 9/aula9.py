def lerValor():
    valor = float(input("Digite a temperatura: "))
    return valor

def temperaturaCel(celsius):
    f = (9 * celsius + 160) / 5
    return f

def mostra(texto):
    print(texto)


lendo = lerValor()
calcula = temperaturaCel(lendo)
mostrando = mostra(calcula)


def leValor():
    tempo = float(input("Digite o tempo gasto: "))
    velocidade = float(input("Digite a velocidade: "))
    return tempo, velocidade

def calculaDistancia(tempo, velocidade):
    return tempo * velocidade


def calculaLitros(distancia):
    return distancia / 12


def resultados(velocidade, tempo, distancia, litros):
    print('Velocidade: ', velocidade)
    print('Tempo: ', tempo)
    print('Distancia: ', distancia)
    print('Litros: ', litros)

v1, v2 = leValor()
calculoD = calculaDistancia(v1, v2)
calculoL = calculaLitros(calculoD)
mostra = resultados(v2, v1, calculoD, calculoL)