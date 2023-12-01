import unittest
def te():
    pass
class nome():
    v = "Homo Sapiens"
    def __init__(self,no,sex):
        self._no = no #Protect
        self.__sex = sex # Privado
    def sno(self):
        print("Nome: " + self.no.title())
    def ssex(self):
        print("Seu sexo: " + self.sex)
#inheritance
class animal(nome):
    v = 'gato'
    def mami(self):
        return "Os Dois são mamiferos"
#multi-level inheritance
class natureza(animal):
    pass
#multiple inheritance
class sala():
    def sa(self,sala):
        print("Sala: " + sala)
        return self
class ano():
    def an(self,ano):
        print("Ano: " + ano)
        return self
class aluno(sala,ano):
    pass

x = nome('Carlos',"M")
#print(x.no)
#x.sno()
#x.ssex()

##########################
#y.mami()

class test(unittest.TestCase):
    def setUp(self):
        self.y = animal("dara", "F")
    def test(self):  
        x = self.y.mami()
        self.assertEqual(x,"Os Dois são mamiferos")
        
unittest.main()
#########################

#y.sno()
#y.ssex()
#print(y.v)

aluno = aluno() 
#aluno.an("3º Ano do ensino Medio").sa('12') # metodo chaining

#####################
#funçaõ super
class base:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        print(self.nome) # metodo executa
    #def m(self):
        #print(self.nome)
class test:
    def __init__(self):
        print('teste')
class homem(base,test):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        print("Nome: " + self.nome + " Idade: " + self.idade) #posso modificar o agir do metodo, difente de classe filho normal
        self.test = test() #inicia uma instancia em um atributo
class mulher(base):  
    def __init__(self, nome,idade):
        super().__init__(nome, idade)
        print("Nome: " + self.nome + " Idade: " + self.idade)

#h = homem("Carlos", "20")
#print(h.m())
#f = mulher("Larisa", "21")

#################################################################
#Classes abstratas com methodos abstratos
from abc import ABC, abstractclassmethod
class abs(ABC):
    @abstractclassmethod
    def siga():
        pass
    def pare():
        pass

class sinal(abs):
    color = None
    def siga(self):
        print("vaiiiiiii")
        return self
    def pare(self):
        print("Pareeeee")
        return self
def mudacor(clase,cor): # objetos como argumentos
    clase.color = cor
#sinal = sinal()
#sinal.siga().pare()
#mudacor(sinal,"Black")
#print(sinal.color)

#duck_typing










