import random 

numero_menor = 1 
numero_maior = 10

tentativa_maxima = 10 

numero_secreto = random.randint(numero_menor, numero_maior)

acertou = False 

for tentativa in range(tentativa_maxima):
    palpite = int ( input("Digite o numero: ") )

    if palpite == numero_secreto: # se palpite for igual a numero_secreto então faça algo:
        acertou = True
        break
    else:
        print("Numero errado \n")

if acertou:
    print("Você acertou")
else:
    print("Você não conseguiu")    