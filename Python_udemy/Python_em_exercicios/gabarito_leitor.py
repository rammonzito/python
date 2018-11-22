N = 7 #int(input("Número de questões: "))
sequencia_correta="ABBCDAA"
pontos = 0
gabarito = sequencia_correta
entrada_aluno = input("Insira as respostas do aluno: ").upper()#.split())
# i = 0
total = 0

print(list(zip(gabarito,entrada_aluno))) 


for o, c in zip(gabarito, entrada_aluno):
    if (o == c):
        total += 1

print (str.format("Acertos: {0} de {1}", total, N))        

# for n in range (len(gabarito)):
#     if(list(entrada_aluno)[i] == n):
#         pontos += 1
#     i += 1
# print (str.format("O aluno acertou {0} questões", pontos))