def cortaMatriz(mat, j):
    '''Retorna a sub-matriz obtida removendo a primeira linha e a j-ésima coluna de uma matriz'''
    subMat = []
    for i in range(1, len(mat)):
        linha = mat[i][:j]           # elementos do início da linha até a posição j exclusive
        linha.extend(mat[i][j + 1:]) # elementos de j exclusive até o final da linha
        subMat.append(linha)
    return subMat

def detLaplace(mat):
    '''Retorna o determinante de uma matriz utilizando o método de Laplace (pela primeira linha) recursivamente'''
    if len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]  # determinante de matriz 2x2
    detMat = 0    # o determinante de cada sub-matriz é somado a essa variável
    for j in range(len(mat[0])):
        subMat = cortaMatriz(mat, j)
        subDet = ((-1) ** j) * mat[0][j] * detLaplace(subMat) # (-1)**(i+j), mas i é sempre igual a 0
        detMat += subDet
    return detMat

def main():
    m = int(input())    # número de matrizes
    n = int(input())    # dimensão das matrizes
    detFinal = 1        # o produto dos determinantes será guardado nessa variável
    for _ in range(m):
        mat = []
        for _ in range(n):
            mat.append([int(num) for num in input().split()]) # leitura da matriz
        detFinal *= detLaplace(mat)
    print(f"Após as {m} transformações, o objeto {n}-dimensional teve o volume multiplicado no valor {detFinal}.")

if __name__ == "__main__":
    main()
