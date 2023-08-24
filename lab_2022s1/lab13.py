def renomeiaArquivo(listaCaminhos, caminhoArquivo, pastaRaiz):
    nomeArquivo, pastaArquivo = caminhoArquivo.split()
    if pastaArquivo == pastaRaiz:
        return pastaRaiz + "_" + nomeArquivo
    for caminho in listaCaminhos:
        if caminho.split()[0] == pastaArquivo: #compara se o caminho é a pasta do arquivo
            return renomeiaArquivo(listaCaminhos, caminho, pastaRaiz) + "_" + nomeArquivo

def main():
    listaCaminhos = [] #guarda as entradas
    pastaRaiz, numArquivos = input().split()
    for _ in range(int(numArquivos)):
        caminhoArquivo = input()
        listaCaminhos.append(caminhoArquivo)
        print(renomeiaArquivo(listaCaminhos, caminhoArquivo, pastaRaiz))

if __name__ == "__main__":
    main()
