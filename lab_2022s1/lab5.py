def PRNG(n_aleatorio: list): # Armazenamento do número em lista permite alterá-lo globalmente na função
    n_aleatorio[0] = (7 * n_aleatorio[0] + 111) % 1024
    print(f"MENSAGEM DEBUG - número gerado: {n_aleatorio[0]}")
    return n_aleatorio[0]

def soco(ataque, defesa, n_aleatorio):
    m = PRNG(n_aleatorio) % 3
    dano_soco = (ataque - defesa) * m
    if dano_soco < 0:
        dano_soco = 0
    return dano_soco

def arremesso_de_facas(ataque, n_aleatorio):
    n = PRNG(n_aleatorio) % 6
    dano_facas = 0
    for i in range (1, n + 1):
        dano_facas += ataque // (3 ** i)
    return dano_facas

def invocacao_de_fada(n_aleatorio):
    status_adicionais = [0, 0, 0, 0]
    # onde [0] = cura, [1] = aumento de ataque, [2] = aumento de defesa, [3] = monstro
    p = PRNG(n_aleatorio) % 100
    q = PRNG(n_aleatorio) % 1024
    status_adicionais[0] = p
    if q < 100:
        if q % 2 != 0:
            status_adicionais[1] = q
        elif q % 2 == 0 and q != 0:
            status_adicionais[2] = q
    elif q >= 1019:
        status_adicionais[3] = "monstro"
    return status_adicionais

def troca_turno(t): # retorna uma lista com quem ataca e quem defende no turno
    if t % 2 == 0:
        atacante_defensor = [0, 1] # [Sarah, Clone]
    else:
        atacante_defensor = [1, 0] # [Clone, Sarah]
    return atacante_defensor

def checa_vida(vida_Sarah, vida_Clone):
    if vida_Sarah <= 0:
        print("Sarah foi derrotada...")
        return False
    elif vida_Clone <= 0:
        print("O clone foi derrotado! Sarah venceu!\nFIM - PARABENS")
        return False
    else:
        return True

# Leitura de entradas iniciais:
statusSarah = (input())
statusClone = (input())
numero_gerador = []
numero_gerador.append(int(input()))

# Separação em listas para cada atributo:
lista_statusSarah = statusSarah.split()
lista_statusClone = statusClone.split()
lista_vida = [int(lista_statusSarah[0]), int(lista_statusClone[0])]
lista_ataque = [int(lista_statusSarah[1]), int(lista_statusClone[1])]
lista_defesa = [int(lista_statusSarah[2]), int(lista_statusClone[2])]

turno = 0 # Para determinar turnos, 0 -- Sarah, 1 -- Clone
ambas_vivas = True
while ambas_vivas:
    comando = input()
    ataca_defende = troca_turno(turno) # a_d[0] é o atacante, a_d[1] é o defensor
    if ataca_defende[0] == 0:
        atacante = "Sarah"
        defensor = "O clone"
    else:
        atacante = "O clone"
        defensor = "Sarah"

    if comando == "soco":
        dano = soco(lista_ataque[ataca_defende[0]], lista_defesa[ataca_defende[1]], numero_gerador)
        lista_vida[ataca_defende[1]] -= dano
        print(f"{defensor} sofreu {dano} pontos de dano!")

    elif comando == "facas":
        dano = arremesso_de_facas(lista_ataque[ataca_defende[0]], numero_gerador)
        lista_vida[ataca_defende[1]] -= dano
        print(f"{defensor} sofreu {dano} pontos de dano!")

    elif comando == "fada":
        aumento_fada = invocacao_de_fada(numero_gerador)
        lista_vida[ataca_defende[0]] += aumento_fada[0]
        lista_ataque[ataca_defende[0]] += aumento_fada[1]
        lista_defesa[ataca_defende[0]] += aumento_fada[2]
        print(f"{atacante} ganhou {aumento_fada[0]} pontos de vida!")
        if aumento_fada[1] != 0:
            print(f"{atacante} ganhou {aumento_fada[1]} pontos de ataque!")
        elif aumento_fada[2] != 0:
            print(f"{atacante} ganhou {aumento_fada[2]} pontos de defesa!")
        if aumento_fada[3] == "monstro":
            if ataca_defende[0] == 0:
                print("O quê? A fada trouxe um monstro gigante com ela!\
\nO Clone e o castelo foram destruídos,\ne Sarah agora tem um novo pet.\
\nFINAL SECRETO - PARABENS???")
            elif ataca_defende[0] == 1:
                print("O quê? A fada trouxe um monstro gigante com ela!\nSarah foi derrotada...")
            break

    ambas_vivas = checa_vida(lista_vida[0], lista_vida[1])
    turno += 1
