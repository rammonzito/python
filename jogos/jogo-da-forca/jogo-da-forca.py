print("Bem-Vindo ao Jogo da Forca")

palavra_secreta = "goiaba".upper()

numero_de_tentativas = 3
erros = 0
acertou = False
letras_utilizadas = []

def captura_letra():
    letra = input("informe uma letra: ")
    return letra.upper()

palavra_apresentada = ["-" for letra in palavra_secreta]
while erros < numero_de_tentativas:
    print("Situação:")
    print(palavra_apresentada)
    print("Letras utilizadas:")
    print(letras_utilizadas)

    letra = captura_letra()
    print("chute: " + letra)
    letras_utilizadas.append(letra)

    if letra in palavra_secreta:
        acertou = True   
        for i in range(0, len(palavra_apresentada)):
            if letra == palavra_secreta[i]:
                palavra_apresentada[i] = letra
    else:
        acertou = False
        erros += 1

    print(acertou)
    