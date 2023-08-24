dia_mes = int(input())
dia_semana = input()
preco = float(input())

if dia_mes % 7 == 0:
    preco = preco / 2
elif dia_semana == "sexta-feira":
    preco = preco * 3 / 4
else:
    preco = preco - dia_mes
if preco < 0:
    preco = 0
print("%.2f" % preco)
# Tive que pesquisar como deixar duas casas decimais,
# tentei com round() mas ele só deixa um zero depois da vírgula

if dia_semana == "segunda-feira":
    print("É um dia terrível, você não devia ter saído da cama.")
elif dia_semana == "sábado" or dia_semana == "domingo":
    print("Agradecemos a preferência, tenha um ótimo fim de semana!")
else:
    print(f"Agradecemos a preferência, tenha uma ótima {dia_semana}!")
