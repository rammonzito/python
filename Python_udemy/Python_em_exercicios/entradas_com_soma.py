numeros = []
quantidade_numeros = int(input("Digite quantos números você deseja somar: "))

def somar (self):
    total = 0
    for numero in numeros:
        total += numero
    return total

for i in range(quantidade_numeros):
    numeros.append(int(input("Digite um número: ")))

valor_final = sum(numeros) #somar(numeros)
print(str.format("Sua soma total é: {0}", valor_final))

print("Teminei de somar")

