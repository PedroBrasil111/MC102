def printMatriz(matriz):
    for linha in matriz:
        print(" ".join([f"{num:03}" for num in linha]))

def selecao(matriz, coordX, coordY, largura, altura):
    return [matriz[i][coordX:(coordX + largura)] for i in range(coordY, (coordY + altura))]

def copia(matriz, subMat, coordX, coordY):
    for i in range(len(subMat)):
        matriz[coordY + i][coordX:(coordX + len(subMat[0]))] = subMat[i]

def espelhamento(matriz, subMat, sentido, coordX, coordY):
    espelhada = []
    if sentido == "h":
        for linha in subMat:
            espelhada.append([linha[i] for i in range((len(subMat[0]) - 1), -1, -1)])
    elif sentido == "v":
        espelhada.extend([subMat[i] for i in range((len(subMat) - 1), -1, -1)])
    copia(matriz, espelhada, coordX, coordY)

def recorte(matriz, subMat, coordX, coordY, coordXsub, coordYsub):
    for i in range(len(subMat)):
        matriz[coordYsub + i][coordXsub:(coordXsub + len(subMat[0]))] = [0] * len(subMat[0]) # zera os pixels deslocados
    copia(matriz, subMat, coordX, coordY)

def rotacao(matriz, subMat, coordX, coordY):
    rotacionada = []
    for j in range(len(subMat[0])):
        rotacionada.append([subMat[i][j] for i in range(len(subMat) - 1, -1, -1)])
    for i in range(len(subMat)):
        matriz[coordY + i][coordX:(coordX + len(subMat[0]))] = [0] * len(subMat[0]) # zera os pixels
    copia(matriz, rotacionada, coordX, coordY)

def main():
    matriz = []
    coordX = coordY = 0
    largura, altura = [int(num) for num in input().split()]
    numOperacoes = int(input())
    for _ in range(altura):
        matriz.append([int(num) for num in input().split()])
    selecionada = selecao(matriz, coordX, coordY, largura, altura)
    for _ in range(numOperacoes):
        leitura = input().split()
        if leitura[0] == "selecao":
            coordX, coordY = int(leitura[1]), int(leitura[2])
            largura, altura = int(leitura[3]), int(leitura[4])
        elif leitura[0] == "copia":
            copia(matriz, selecionada, int(leitura[1]), int(leitura[2]))
        elif leitura[0] == "espelhamento":
            espelhamento(matriz, selecionada, leitura[1], coordX, coordY)
        elif leitura[0] == "rotacao":
            rotacao(matriz, selecionada, coordX, coordY)
        elif leitura[0] == "recorte":
            recorte(matriz, selecionada, int(leitura[1]), int(leitura[2]), coordX, coordY)
        selecionada = selecao(matriz, coordX, coordY, largura, altura)
    printMatriz(matriz)

if __name__ == "__main__":
    main()
