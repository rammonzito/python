acessos_dia = []
quantidade_acessos_necessaria = 1000000.0
contador_dias = 0

N = int(input("Quantidade de dias para tentar: "))


for d in range(N):
    if (sum(acessos_dia) >= quantidade_acessos_necessaria):
        print(str.format("Conseguiram bater a meta em: {0} dias", contador_dias))
        break
    A = int(input("Acessos Dia: "))
    acessos_dia.append(A)
    contador_dias += 1

