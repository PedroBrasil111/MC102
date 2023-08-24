def pares(fita1, fita2):
    return [fita1[i] + fita2[i] for i in range(len(fita1))]

def conta_mutacao(par_ancestral, par_evoluido):
    num_mutacoes = 0
    for condicao in [par_evoluido[i] > par_ancestral[i] for i in range(len(par_ancestral))]:
        if condicao:
            num_mutacoes += 1
    return num_mutacoes

def sort_caracteristicas(dict_mutacoes):
    lista_carac = [carac for carac in dict_mutacoes.keys()]
    num_mutacoes = [num for num in dict_mutacoes.values()]
    sorted_carac = [lista_carac[num_mutacoes.index(num)] for num in sorted(dict_mutacoes.values())]
    return sorted_carac

def checaAncestralidade(dict_espec, carac):
    for espec, car_espec in dict_espec.items():
        if carac in car_espec:
            if car_espec == [carac]:
                print(espec)
            else:
                car_espec.remove(carac)

def main():
    dict_pares = {}          # Relaciona características aos seus pares de genes
    dict_especies = {}       # Relaciona espécies às suas características
    dict_mutacoes = {}       # Relaciona características ao número de mutações em relação à característica ancestral
    num_aliens = int(input())
    for _ in range(num_aliens):
        leitura = [txt for txt in input().split(sep=" | ")] # [0] - espécies, [1] - características
        dict_especies[leitura[0]] = [carac for carac in leitura[1].strip().split()]
    num_carac = int(input()) # carac - caracterítica
    for i in range(num_carac):
        carac = input()
        fita1 = input()
        fita2 = input()
        dict_pares[carac] = pares(fita1,fita2)
        if i == 0:
            carac_ancestral = carac
            dict_mutacoes[carac] = 0
        else:
            dict_mutacoes[carac] = conta_mutacao(dict_pares[carac_ancestral], dict_pares[carac])
    for carac in sort_caracteristicas(dict_mutacoes):
        print(f"CARACTERÍSTICA: {carac}")
        checaAncestralidade(dict_especies, carac)

if __name__ == "__main__":
    main()
