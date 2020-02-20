import random


letras_descobertas = []
letras_ja_utilizadas = ""
palavras = []

arquivo = open("palavras.txt", "r")

for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

arquivo.close()

numero = random.randrange(0, len(palavras))
palavra_secreta = palavras[numero].upper()


print(palavra_secreta)

print("\n*** Jogo da Forca ***\n")

letras_descobertas = ["-" for letra in palavra_secreta]

print (letras_descobertas)
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