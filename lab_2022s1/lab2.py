print("*Que página de meme do Instagram você é?*")
idade = int(input("Qual a sua idade?\n"))
print(idade)

if idade < 0 or idade > 125:
    resultado = "Erro: entrada inválida"

elif idade < 25:
    segundos = int(input("Quantos segundos são necessários para saber se um vídeo é bom?\n"))
    print(segundos)
    if segundos < 0:
        resultado = "Erro: entrada inválida"
    elif segundos <= 5:
        resultado = "Você deveria estar no TikTok"
    else:
        resultado = "@meltmemes"

elif 25 <= idade <= 40:
    banda = input(("Qual banda você gosta mais?\n"))
    if banda == "A" or banda == "B":
        if banda == "A":
            print ("A) Matanza")
        else:
            print("B) Iron Maiden")
        resultado = "@badrockistamemes"
    elif banda == "C" or banda == "D":
        if banda == "C":
            print("C) Imagine Dragons")
        else:
            print("D) BlackPink")
        capivaras = input("São as capivaras os melhores animais da Terra?\n")
        print(capivaras)
        if capivaras == "Sim":
            resultado = "@genteboamemes"
        elif capivaras == "Não":
            resultado = "@wrongchoicememes"
        else:
            resultado = "Erro: entrada inválida"
    else:   # Caso banda != A,B,C,D
        print(banda) 
        resultado = "Erro: entrada inválida"

else:   # Se 40 < idade <= 125
    imagem = input("Que imagem de bom dia você manda no grupo da família?\n")
    if imagem == "A":
        print("A) Bebê em roupa de flor")
        resultado = "@bomdiabebe"
    elif imagem == "B":
        print("B) Gato")
        resultado = "@kittykatmsgs"
    elif imagem == "C":
        print("C) Coração e rosas")
        resultado = "@bomdiaflordodia"
    else:
        print(imagem)
        resultado = "Erro: entrada inválida"

if resultado == "Erro: entrada inválida":
    print(resultado)
elif resultado == "Você deveria estar no TikTok":
    print(f"RESULTADO\n{resultado}")
else:   # Se o resultado é alguma página, deve ter "Sua página de memes é"
    print(f"RESULTADO\nSua página de memes é: {resultado}")
