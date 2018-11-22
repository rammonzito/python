'''
uma casa 400 mil
comprar parcelado em 30 anos
emprestimo de 200 mil em 30 anos
e a taxa de juros é 0.7% ao mes

quanto vc vai pagar no emprestimo
'''
valor_ja_pago=0
valor_emprestado = float(10)
juros_ao_mes = float(0.7/100) #tenho 1% de juros/ mês
numero_meses = 12*30

print(valor_ja_pago+valor_emprestado+(valor_emprestado*(juros_ao_mes * numero_meses)))

input()