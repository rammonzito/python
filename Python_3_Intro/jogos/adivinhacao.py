print("************************************************")
print("Olá! bem-vindo ao jogo de adivinhação em Python!")
print("************************************************")

numero_secreto = 42
numero_entrada = 0
numeros_digitados = []
acertou = False
tentativas_possiveis = 10
rodada = 10

# for rodada in range(1,tentativas_possiveis): #podíamos usar um forzinho, mas vamos usar while :D
while not (acertou) and (rodada > 0):
    print(str.format("Resta(m) {0} tentativa(s) de {1}" , rodada, tentativas_possiveis))
    numero_entrada = input("Digite um número entre 1 e 100:")
    chute = int(numero_entrada)
    print("Número:", chute)

    if(chute < 1 or chute > 100):
        print("você deve digitar um número entre 1 e 100!")
        continue

    acertou = (numero_secreto == chute)
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!!")
        break
    else:
        if (menor):
            print("Seu número é MENOR que o secreto")
        else:
            print("Seu número é MAIOR que o secreto")
    
    if (chute in numeros_digitados):
        print ("Você já tinha tentado", chute)
    elif (chute == 7):
        print("7 é o número da sorte, mas não é o número secreto")
    else:
        print("Você ainda não tinha tentado esse :D")

    numeros_digitados.append(chute)
    rodada -= 1

print("Fim do jogo")

