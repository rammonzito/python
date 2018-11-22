def somar_numeros(numero1, numero2):
    return float(numero1) + float(numero2)


def multiplicar_vezes(numero, vezes):
    return float(numero*vezes)

def main_fodao():
    valor_soma = somar_numeros(2,6)
    return (multiplicar_vezes(valor_soma,2))

def cadastrar_nomes(nomes):
    print ('Digite o nome: ')
    nome = input()
    nomes.append(nome)
    return