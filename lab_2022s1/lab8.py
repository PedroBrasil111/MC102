from datetime import date, timedelta

def modo_estoque(dict_produtos, set_categorias):
    '''Permite a inserção e remoção de produtos ao dicionário de produtos.

    O dicionário de produtos apresenta sub-dicionários contendo as características de cada produto
    O conjunto de categorias guarda todas as categorias para imprimi-las no modo relatório'''
    num_operacoes = int(input())
    for _ in range(num_operacoes):
        leitura = input().split()
        # 0 = insere/remove, 1 = produto, 2 = quantidade, 3 = categoria, 4 = preço, 5 = validade
        if leitura[0] == "0": # inserção
            dict_produtos[leitura[1]] = {"quantidade": int(leitura[2]),\
            "categoria": leitura[3], "preço": float(leitura[4]), "validade": leitura[5]}
            set_categorias.add(leitura[3])
        else: # remoção
            try:
                if int(leitura[2]) <= dict_produtos[leitura[1]].get("quantidade", 0):
                    dict_produtos[leitura[1]]["quantidade"] -= int(leitura[2])
                    print("SUCCESS")
                else:
                    print("ERROR")
            except KeyError:
                print("ERROR")

def modo_caixa(dict_produtos, lucro):
    '''Remove a quantidade vendida de produtos do dicionário de produtos e retorna o saldo das vendas'''
    num_operacoes = int(input())
    for _ in range(num_operacoes):
        leitura = input().split()
        dict_produtos[leitura[0]]["quantidade"] -= int(leitura[1])
        lucro += dict_produtos[leitura[0]]["preço"] * int(leitura[1])
    return lucro

def data(data_str):
    '''Converte uma data em formato de string para o formato apoiado pela biblioteca datetime'''
    ano = int(data_str[4:])
    mes = int(data_str[2:4])
    dia = int(data_str[:2])
    data_formatada = date(ano, mes, dia)
    return data_formatada

def checa_estoque(data_atual, dict_produtos):
    '''Define o que deve acontecer com cada produto quando for chamado o relatório

    A função remove itens esgotados do dicionário de produtos, além de criar uma
    lista de produtos que devem ser repostos e outra de produtos que devem entrar
    em promoção.'''
    # Declaração de variáveis
    lista_promocao = []
    lista_reposicao = []
    aux = dict_produtos.copy()
    estoque_vazio = True

    for produto in dict_produtos.keys():
        data_vencimento = data(dict_produtos[produto]["validade"])
        if dict_produtos[produto]["quantidade"] == 0:
            del aux[produto]
            lista_reposicao.append(produto)
        elif data_vencimento - data_atual <= timedelta(7):
            lista_promocao.append(produto)
    if aux:
        estoque_vazio = False
    return aux, lista_reposicao, lista_promocao, estoque_vazio

def relatorio(dict_produtos, ganhos, set_categorias):
    '''Imprime os produtos em estoque, aqueles que devem ser repostos e os que devem entrar em promoção

    A impressão dos produtos é feita em ordem alfabética, e os mesmos são impressos sob suas
    respectivas categorias, essas também organizadas em ordem alfabética.
    '''
    data_atual = data(input())
    dict_produtos, lista_reposicao, lista_promocao, estoque_vazio = checa_estoque(data_atual, dict_produtos)
    print("* ESTOQUE")
    if not estoque_vazio:
        for categoria in sorted(set_categorias):
            categoria_vazia = True
            for produto in dict_produtos:
                if dict_produtos[produto]["categoria"] == categoria:
                    categoria_vazia = False
                    break
            # O for aqui serve para evitar bug no caso de não ter nenhum item da categoria
            if not categoria_vazia:
                print(f"- {categoria}")
            for produto in sorted(dict_produtos):
                if dict_produtos[produto]["categoria"] == categoria:
                    print(produto, dict_produtos[produto]["quantidade"])
    print(f"* SALDO {ganhos:.2f}")
    if lista_reposicao:
        print("* REPOSICAO")
        for produto in lista_reposicao:
            print(produto)
    if lista_promocao:
        print("* PROMOCAO")
        for produto in lista_promocao:
            print(produto)

def main():
    '''Chama o modo desejado dependendo do input (0 -- relatório, 1 -- estoque, 2 -- caixa)'''
    # Declaração de variáveis
    produtos = {}
    categorias = set()
    saldo = 0
    modo = input()

    while modo != "0":
        if modo == "1":
            modo_estoque(produtos, categorias)
        elif modo == "2":
            saldo = modo_caixa(produtos, saldo)
        modo = input()
        if modo == "0":
            relatorio(produtos, saldo, categorias)

if __name__ == "__main__":
    main()
