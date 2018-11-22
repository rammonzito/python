# -*- coding: UTF-8 -*-

import re

def listar(nomes):
    print('Nomes cadastrados:')
    for nome in nomes:
        print (nome)    
    
def cadastrar(nomes):
    print('Digita seu Nome: ')
    nome = input()
    nomes.append(nome)
    print('Cadastrado com Sucesso!')

def menu():
    nomes = []
    escolha = ''
    while (escolha != '0'):
        print ('Digite 1 para cadastrar, 2 para listar, 3 para excluir, 4 para alterar, 5 para pesquisar, 6 para pesquisar com expressões regulares e 0 para terminar')
        escolha = input()

        if (escolha == '1'):
            cadastrar(nomes)
        
        if (escolha == '2'):
            listar(nomes)

        if (escolha == '3'):
            remover_da_lista(nomes)
        
        if (escolha == '4'):
            alterar(nomes)
        
        if (escolha == '5'):
            pesquisar(nomes)

        if (escolha == '6'):
            procurar_regex(nomes)

def remover_da_lista(nomes):
    print('Qual nome você gostaria de remover?')
    nome = input()
    nomes.remove(nome)
    print('Nome removido com sucesso!')

def alterar(nomes):
    print('Qual nome você gostaria de alterar?')
    nome = input()
    if (nome in nomes):
        print('Qual o novo Nome?')
        novo_nome = input()
        meu_index = nomes.index(nome)
        nomes[meu_index] = novo_nome
        print('Nome alterado com sucesso!')
    else:
        print('Nome inexiste')

def pesquisar(nomes):
    print('Qual nome você gostaria de pesquisar?')
    nome = input()
    if(nome in nomes):
        print('Nome %s cadastrado!' % nome)
    else:
        print('Nome %s não cadastrado.' % nome)

def procurar_regex(nomes):
    print('Digite a expressão regular:')
    regex = input()
    nomes_concatenados = ''.join(nomes)
    resultado =  re.findall(regex, nomes_concatenados)
    if resultado is not None:
        print(resultado.group())
    else:
        print('Não Localizado')

    #concatene os nomes
    #busque pela expressão regular no string
    #imprime o resultado

menu()
