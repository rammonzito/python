class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0 #propriedade privada
    
    def imprimir(self):
        print(str.format("Nome: {0}, Telefone: {1}, Empresa: {2}", self.nome, self.telefone, self.empresa))
    
    def curtir(self):
        self.__curtidas += 1
    
    def obter_curtidas(self):
        return self.__curtidas
    
    #@staticmethod #pra não ter que receber uma instancia da classe (sem self)
    @classmethod #    
    def gerar_perfis(classe, nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        perfis = []
        for linha in arquivo:
            valores = linha.split(',')
            perfis.append(classe(*valores))
        arquivo.close()
        return perfis        
    
class Perfil_Vip(Perfil):
    'Classe de Perfil VIP'

    def __init__(self, nome, telefone, empresa, apelido = ''):
        super(Perfil_Vip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido

    def obter_creditos(self):
        return super(Perfil_Vip, self).obter_curtidas * 10.0

# exercícios para treinamento
class Data(object):
    'Classe para formatar data'
    
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def imprime(self):
        print(str.format("Data: {0}/{1}/{2}", self.day, self.month, self.year))

class Pessoa(object):
    'Classe que contém método para calcular IMC e afins'

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = float(peso)
        self.altura = float(altura)
        self.resultado = self.calculaIMC()

    def  calculaIMC(self):
        return (self.peso / (self.altura ** 2))

    def imprime(self):
        print(str.format("IMC de {0} é: {1}", self.nome, self.resultado))    