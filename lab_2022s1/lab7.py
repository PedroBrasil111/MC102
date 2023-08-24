def conta_consecutivos(lista):
    '''Imprime qual item mais se repete consecutivamente numa lista dada e quantas vezes ele se repete.'''
    contador = [1] * len(lista)
    for i in range(1, len(lista)):
        if lista[i] == lista[i - 1]:
            contador[i] += contador[i - 1]
    print(lista[contador.index(max(contador))], max(contador))

def conta_unicos(lista):
    '''Imprime quantos itens únicos existem em uma lista dada.'''
    contador = []
    for item in lista:
        if item not in contador:
            contador.append(item)
    print(len(contador))

def remove_item(lista, item):
    '''Devolve uma lista removendo todos os itens iguais a um dado item a partir de uma lista dada.'''
    sem_item = lista.copy()
    for i in range(len(lista)):
        if lista[i] == item:
            sem_item.remove(lista[i])
    return sem_item

def exclui_repeticao(lista):
    '''Devolve uma lista removendo todas as repetições de itens a partir de uma lista dada.'''
    sem_repeticao = []
    for item in lista:
        if item not in sem_repeticao:
            sem_repeticao.append(item)
    return sem_repeticao

def formata_nome(lista_nomes):
    '''Devolve uma lista com os nomes das fotos no padrão XX_y-z-w a partir de uma lista dada.'''
    lista_formatada = []
    for nome_foto in lista_nomes:
        lista_auxiliar = nome_foto.split(sep="_")
        categoria_foto = lista_auxiliar[0]
        descricao_foto = lista_auxiliar[1].lower().split()
        descricao_foto_str = "-".join(descricao_foto)
        nome_final = categoria_foto + "_" + descricao_foto_str
        lista_formatada.append(nome_final)
    return lista_formatada

def organiza_fotos(lista):
    '''Imprime três listas, cada uma contendo as fotos específicas por categoria.

    A primeira lista contém as fotos iniciadas em "CC", a segunda, em "CR" e a terceira, em "HA".'''
    lista_cc = []
    lista_cr = []
    lista_ha = []
    for foto in lista:
        if foto[:2] == "CC":
            lista_cc.append(foto)
        elif foto[:2] == "CR":
            lista_cr.append(foto)
        elif foto[:2] == "HA":
            lista_ha.append(foto)
    print(f"{lista_ha}\n{lista_cr}\n{lista_cc}")

def main():
    entrada = input().split("/ ")
    lista_fotos = entrada[0].split(", ")
    conta_consecutivos(lista_fotos)
    conta_unicos(lista_fotos)
    organiza_fotos(formata_nome(exclui_repeticao(remove_item(lista_fotos, entrada[1]))))

if __name__ == "__main__":
    main()
