palavra = "ramon".upper()
palavra_secreta = list(palavra)
letras_descobertas = []
letras_ja_utilizadas = ""

print("\n*** Jogo da Forca ***\n")

letras_descobertas = ["_" for letra in palavra_secreta]

acertou = False

while acertou == False:
    print("A palavra tem %s letras" % len(palavra_secreta))
    print("Letra já utilizadas: %s " % letras_ja_utilizadas)

    letra = str(input("Digite uma letra:")).upper()
    letras_ja_utilizadas += letra + ", "

    for i in range(0, len(palavra_secreta)) :
        if letra == palavra_secreta[i] :
            letras_descobertas[i] = letra
        print(letras_descobertas[i])

    acertou = True

    for x in range(0, len(letras_descobertas)) :
        if letras_descobertas[x] == "-" :
            acertou = False
    
print("Parabéns! Você acertou!")
input()