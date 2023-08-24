class Sala:
    '''Contém as características da sala.

    Os atributos (características) da sala são:
    seu número, as salas conectadas, o item no baú e as personagens presentes.

    Parâmetros:
    numero_sala -- o número da sala
    lista_conexoes -- lista contendo os números das salas com as quais essa sala possui conexão
    item -- item no baú da sala. Por padrão, não há nenhum item ("Nada")
    personagem -- personagem presente na sala. Por padrão, não há personagem (string vazia),
    mas pode conter o clone ("Clone"), a Sarah ("Sarah"), ou ambas ("CloneSarah")
    '''
    def __init__(self, numero_sala, lista_conexoes, item = "Nada", personagem = ""):
        self._numero_sala = numero_sala
        self._lista_conexoes = lista_conexoes
        self.item = item
        self.personagem = personagem

    @property
    def item(self):
        '''Retorna o item que está na sala'''
        return self._item

    @property
    def personagem(self):
        '''Retorna o personagem que está na sala'''
        return self._personagem

    @item.setter
    def item(self, item):
        '''Setter para o item na sala'''
        self._item = item

    @personagem.setter
    def personagem(self, personagem):
        '''Setter para o personagem na sala'''
        self._personagem = personagem

    def acao(self, lista_itens, tamanho_inventario):
        '''Checa quais as possíveis ações de Sarah ao entrar na sala.

        Para o teste do bot, se houver algum item na sala, a função instantaneamente
        o remove da sala e o adiciona ao inventário de Sarah caso ainda haja espaço.
        Se Sarah entrar na mesma sala do clone (quando personagem == "CloneSarah"),
        é checado se ela carrega a espada. Caso carregue, Sarah vence. Caso contrário, ela perde.

        Parâmetros:
        lista_itens -- lista com os itens que estão no inventário de Sarah
        tamanho_inventario -- número máximo de itens que Sarah pode carregar
        '''
        self.personagem += "Sarah"
        if self.personagem != "CloneSarah":
            if self._item != "Nada":
                print(f"Você está na sala de número {self._numero_sala} ela contém um baú com \
{self._item} e dela você pode ir para as salas {self._lista_conexoes}")
                print(f"Pegar {self._item}")
                if len(lista_itens) < tamanho_inventario:
                    lista_itens.append(self._item)
                    print(f"{self._item} adicionado ao inventário")
                    self._item = "Nada"
                else:
                    print("Inventário cheio!")
            else:
                print(f"Você está na sala de número {self._numero_sala} e dela você pode \
ir para as salas {self._lista_conexoes}")
        else:
            if "espada" in lista_itens:
                print("Você derrotou o clone maligno com a espada mágica! Com a Sarah \
no reino o mundo pode voltar ao equilíbrio.\nPARABÉNS!")
            else:
                print("Infelizmente você encontrou o clone sem a espada das fadas e \
foi derrotado. Tente novamente...")
        self.personagem = ""

def formata_lista(lista):
    '''Formata os items de uma lista, passando-os de str para int

    Parâmetros:
    lista -- lista a ser formatada'''
    for i in range(len(lista)):
        lista[i] = int(format(lista[i]))

# Declaração de variáveis
mapa = []
inventario = []

n = int(input()) # n = número de salas
for _ in range(n):
    caracteristicas_sala = input().split()
    formata_lista(caracteristicas_sala)
    n_sala = caracteristicas_sala.pop(0) # n_sala = número da sala
    mapa.append(Sala(n_sala, caracteristicas_sala))

numero_itens = int(input())
for _ in range(numero_itens):
    sala_item = input().split()
    sala_item[0] = int(format(sala_item[0]))
    mapa[sala_item[0]].item = sala_item[1]

sala_clone = int(input())
mapa[sala_clone].personagem = "Clone"
sala_inicial = int(input())
capacidade_inventario = int(input())

lista_movimentos = input().split()
lista_movimentos.insert(0, sala_inicial)
formata_lista(lista_movimentos)

print("Bem-vindo as Aventuras de Sarah 2.0\nSarah acorda no saguão do antigo castelo de \
sua família,ela tem a oportunidade única de derrotar o seu clone maligno que \
se apoderou do reino.\nPara isso ela deve encontrar o baú da sua família que contém a \
espada mágica que apenas a verdadeira herdeira pode utilizar.\n\
Na sala onde está Sarah vê várias portas. Qual é a sua próxima ação?")
print(f"DEBUG - O clone está na sala: {sala_clone}")

for sala_atual in lista_movimentos:
    if sala_atual != sala_inicial:
        print(f"Mover para sala {sala_atual}")
        sala_inicial = ''
    mapa[sala_atual].acao(inventario, capacidade_inventario)
    if "poção" in inventario:
        print("Você pegou a poção da morte e virou pó instantaneamente. Tente novamente...")
        break
