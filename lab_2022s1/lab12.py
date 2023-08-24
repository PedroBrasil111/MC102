from decimal import Decimal
from recipes_decimal import pi

def zeta(b, x, pi_):
    '''Retorna zeta, somatório de 1 / (n ** s) com n de 1 a 100, onde s = b * x + pi

    b -- constante da fórmula para o cálculo da distância
    x -- quantidade de combustível
    '''
    s = b * x + pi_
    return sum([1 / n ** s for n in range(1, 101)])

def formulaDist(a, b, c, d, x, pi_):
    '''Retorna a distância capaz de ser percorrida em um salto com certa quantidade de combustível x

    a, b, c, d -- constantes (diferentes para cada salto)
    x -- quantidade de combustível
    '''
    numerador = pi_ + a * Decimal.exp(x) - zeta(b, x, pi_)
    denominador = Decimal.exp(-Decimal.sqrt(c * x)) + d * (Decimal("2") * pi_ ** Decimal("3") - x)
    return numerador / denominador

def buscaCombustivel(dist, a, b, c, d, pi_):
    '''Busca binária que chuta valores de combustível para o salto e o retorna ao achá-lo (erro máximo de 10e-32)

    dist -- distância do planeta ao qual será realizado o salto
    a, b, c, d -- constantes para o cálculo da distância
    '''
    esquerda = Decimal("0.") #combustível mínimo
    direita = Decimal("50.") #combustível máximo
    while esquerda < direita:
        chuteCombustivel = (esquerda + direita) / Decimal("2")
        chuteDist = formulaDist(a, b, c, d, chuteCombustivel, pi_)
        if abs(chuteCombustivel - esquerda) <= Decimal("10e-32"):
            return chuteCombustivel
        if chuteDist < dist:
            esquerda = chuteCombustivel
        else:
            direita = chuteCombustivel

def maiorDistancia(dictDistancias, distMax, distMin):
    '''Retorna qual planeta apresenta a maior distância possível para a qual o salto pode ser realizado'''
    maiorDist = 0
    maisDistante = None
    for planeta, dist in dictDistancias.items():
        if distMin <= dist <= distMax and dist > maiorDist:
            maisDistante = planeta
            maiorDist = dist
    return maisDistante

def main():
    pi_ = pi() #guardando pi em uma variável para só calcular uma vez
    numPlanetas = int(input())
    while numPlanetas != 0:
        dictDistancias = {} #associa planeta (chave) à distância
        for _ in range(numPlanetas):
            nomePlaneta = input()
            dist = Decimal(input())
            dictDistancias[nomePlaneta] = dist
        a = Decimal(input())
        b = Decimal(input())
        c = Decimal(input())
        d = Decimal(input())
        distMax = formulaDist(a, b, c, d, Decimal("50."), pi_) #o tanque não suporta mais que 50.0 hawkins
        distMin = formulaDist(a, b, c, d, Decimal("0."), pi_)
        maisDistante = maiorDistancia(dictDistancias, distMax, distMin)
        if maisDistante is None:
            print("GRAU~~")
        else:
            tanque = buscaCombustivel(dictDistancias[maisDistante], a, b, c, d, pi_)
            print(f"{maisDistante}\n{tanque:.28f}")
        numPlanetas = int(input())

if __name__ == "__main__":
    main()
