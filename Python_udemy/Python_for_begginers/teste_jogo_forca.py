palavra = "RAMON"
palavra_secreta = list(palavra)
letras_descobertas = []
acertou = False
letras_informadas = ""

print("\n*** Jogo da Forca ***\n")

for i in range(0, len(palavra_secreta)):
    letras_descobertas.append("-")

print(str.format("A palavra secreta possui {0} letras", len(palavra)))

while not acertou:
    print(letras_descobertas)
    print("letras já informadas: " + letras_informadas)
    letra = input("Digite uma letra: ").upper()
    for i in range(0, len(palavra_secreta)):
        if letra == palavra_secreta[i]:
            letras_descobertas[i] = letra
    letras_informadas += letra + ", "
    
    acertou = True

    for x in range(0, len(letras_descobertas)):
        if (letras_descobertas[x] == "-"):
            acertou = False

print(palavra)
print("Parabéns! Você acertou!")
input()

