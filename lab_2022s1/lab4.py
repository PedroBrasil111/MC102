listaSolucoes = [] # Lista que armazenará as soluções de cada operação
operador = ""

while operador != "0":
    leitura = (input())
    dados = leitura.split() # Separa operador e números em uma lista
    operador = dados[0]
    n_1 = int(format(dados[1]))
    n_2 = int(format(dados[2]))

    if operador == "+":
        solucao = n_1 + n_2
    elif operador == "-":
        solucao = n_1 - n_2
    elif operador == "*":
        solucao = n_1 * n_2
    elif operador == "/":
        quociente = n_1 // n_2
        resto = n_1 % n_2
        solucao = f"{quociente} {resto}"
    elif operador == ";":
        dividendo = n_1 - n_2
        if dividendo < 0:
            dividendo = - dividendo
            # Transformação de negativo em positivo para possibilitar o uso de range...
            # mais à frente. O resultado não se altera por conta disso
        if dividendo != 0:
            solucao = "1" # Definir 1 como 1° divisor previamente ajuda na formatação
            for x in range(2, dividendo + 1):
                if dividendo % x == 0:
                    solucao += f" {x}"
        else: # caso especial se n_1 == n_2
            solucao = 0

    if operador != "0":
        # If com mesma condição do while impede impressão repetida do último resultado
        listaSolucoes.append(solucao)
for x in listaSolucoes:
    print(x)
