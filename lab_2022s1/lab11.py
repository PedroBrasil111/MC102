from dataclasses import dataclass

@dataclass
class Noticia():
    nId: int
    titulo: str
    qtdLeitores: int
    qtdLeitoresFinal: int
    qtdCliques: int
    tempo: int
    paragrafos: str

    def relatorio(self):
        return f"nId: {self.nId}\nqtdLeitores: {self.qtdLeitores}\nqtdLeitoresFinal: {self.qtdLeitoresFinal}\n\
qtdCliques: {self.qtdCliques}\ntempo: {self.tempo}"

def lerNoticia(noticia):
    nId = int(noticia.readline().split()[1]) #pegando index 1 para tirar o que vem antes dos dois pontos
    titulo = noticia.readline().split(maxsplit=1)[1][:-1] #slice para remover \n no final
    qtdLeitores = int(noticia.readline().split()[1])
    qtdLeitoresFinal = int(noticia.readline().split()[1])
    qtdCliques = int(noticia.readline().split()[1])
    tempo = int(noticia.readline().split()[1])
    paragrafos = noticia.read().split("\n")
    return Noticia(nId, titulo, qtdLeitores, qtdLeitoresFinal, qtdCliques, tempo, paragrafos)

def mediaLeitores(listaNoticias):
    return f"{sum([noticia.qtdLeitores for noticia in listaNoticias]) // len(listaNoticias)}"

def maisLeitores(listaNoticias):
    maior = listaNoticias[0]
    for i in range(len(listaNoticias)):
        if listaNoticias[i].qtdLeitores > maior.qtdLeitores:
            maior = listaNoticias[i]
    return f'"{maior.titulo}" {maior.qtdLeitores}'

def maisLeitoresFinais(listaNoticias):
    maior = listaNoticias[0]
    for i in range(len(listaNoticias)):
        if listaNoticias[i].qtdLeitoresFinal > maior.qtdLeitoresFinal:
            maior = listaNoticias[i]
    return f'"{maior.titulo}" {maior.qtdLeitoresFinal}'

def mediaCliques(listaNoticias):
    return f"{sum([noticia.qtdCliques for noticia in listaNoticias]) // len(listaNoticias)}"

def maiorTempo(listaNoticias):
    maior = listaNoticias[0]
    for i in range(len(listaNoticias)):
        if listaNoticias[i].tempo > maior.tempo:
            maior = listaNoticias[i]
    return f"{maior.tempo}"

def mediaParagrafos(listaNoticias):
    return f"{sum([(len(noticia.paragrafos) - 1) for noticia in listaNoticias]) // len(listaNoticias)}" #len - 1 para não contar última linha em branco

def printRelatorioFinal(listaNoticias):
    return f"{mediaLeitores(listaNoticias)}\n{maisLeitores(listaNoticias)}\n{maisLeitoresFinais(listaNoticias)}\n\
{mediaCliques(listaNoticias)}\n{maiorTempo(listaNoticias)}\n{mediaParagrafos(listaNoticias)}"

def main():
    listaNoticias = []
    numNoticias = int(input())
    for _ in range(numNoticias):
        leitura = input()
        with open(leitura) as noticia:
            listaNoticias.append(lerNoticia(noticia))
    for noticia in listaNoticias:
        with open(f"relatorio_{noticia.nId}.txt", "w+") as relatorio:
            relatorio.write(noticia.relatorio())
    with open("relatorio_final.txt", "w+") as relatorioFinal:
        relatorioFinal.write(printRelatorioFinal(listaNoticias))

if __name__ == "__main__":
    main()
