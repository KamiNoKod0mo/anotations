import math, time, random, os, shutil #mymodule as nicknaame withi functions
from abc import ABC, abstractclassmethod
import functools, time
#x = "Bro"
#print(len(x))
#print(x.find("r"))
#print(x.capitalize())
#print(x.upper())
#print(x.lower())
#print(x.isdigit())
#print(x.isalpha())
#print(x.count("r"))
#print(x.replace("r","aa"))
#print(x*3)

#y = 33
#print(float(y))#type cast
#en = int(input("Entrada: "))
#print(en)
#pi =3.14
#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#fabs, pow, sqrt, max, min#

#name = "Carlos hen"
#fi_na = name[0]# start,stop,step
#slice = slice(1,4)#
#print(name[slice])

#if True:
#    print("Hi")
#elif "x" not in listx:
#    print("IH")
#else:
#    print("none")

#for i in range(10,20,2):
#    print(i)
#for n in "CArlos":
#    print(n)
#time.sleep(1)

#nested matriz
#l,c = 5,5
#s= input("s:")
#for i in range(l):
#    for j in range(c):
#        print(s, end="")
#    if False:
#        break
#    elif j == 4:
#        pass # Para codições vazias
#    else:
#        continue # Não printa pq passa pro proximo laço de repetição, ignora o resto
#    print()

#t = [[3 - i for i in range(3)] for j in range(3)]
#print(t)


food = ["carne","frango", "batata", "aaa"] #List
#food.append("Ice cream")#remove(''), pop(x), insert, sort(reverse), del, len , extend
#print(food[4])
#food2 = ["teste"]
#et = [food,food2]
#print(et[1][0])
#sorted()
#reversed()
#list(range(1,6,x))
#min max sum split
#[value**2 for value in range(1,11)]
#x[1:3] #Fatia

#estudest = ("carlos", 19, "Homem") #tuplas
#print(estudest.index("Homem"))#count, for, if

#capitais = {'DF':'Brasilia','SP':'São Paulo'} #Dicionarios
#print(capitais['SP'])
#print(capitais.get("teste"))#keys, values, items, for key,value; update({"ger":"aa"}), pop, clear
#del() set() update()

#----
#Falta daqui para baixo
#----

#uten = {"faca", "panela"} #set
#uten.add("teste")#remove, clear, union, difference, intersection
#print(uten)

#name = "CARlos"
#if(name[0:2].isupper()): #islower
#    print("up")

#def hi(name, a):
#    print("hi " + name + str(a))
#    r = 2023 - a
#    return r
#na="CArlos "
#print(hi(name="na",a=20))

#Nested functions, função aninhadas
#print(round(abs(float(input("Teste: ")))))
#global and local scope

#----
#Intermediarioa
#---


#def te(size,*args): #guarda em tuplas
#    sum =0
#    args = list(args) #pq nao pode mudar tupla
#    for i in args:
#        sum += i
#    return sum
#print(te(1,2,3))

#**kwargs # guada em dicionario
#def hi(**kwargs):
    #print(kwargs['fist'] + " " + kwargs['l'])
#    for key,value in kwargs.items():
#        print(key+value, end=" ")
#hi(fist="Carlos", m="Henrique", l="De Oliveira")

# str.format()

#animal = "teste"
#print("alguma {1}, {0}, {x}".format(animal, "aaaa", x="tete"))# positional, keyword argument, 2 times
#text = "The {:>10} sobre {:.2}" # <, >,^; :, :b :o :x :X :e :E
#print(text.format(animal,123.444))

#x = random.randint(1,10) #random(), choice, shuffle
#print(x)

#execption
#try:
#    nume = int(input("Nunber divide: "))
#    denomi = int(input("Number divide by: "))
#    r = nume/denomi
#except ZeroDivisionError as e:
#    print(e)
#    print("Erro do 0")
#except ValueError:
#    print("Só numeros")
#except Exception:
#    print("Erro")
#else:
#    print(r)
#finally: # precisar ser executado
#    print("Precisa")

#path = "teste.txt"
#if os.path.exists(path):
#    print("Existe")
#    if os.path.isfile(path):
#        print("é arquivo")
#    elif os.path.isdir(path):
#        print("É pasta")
#with open(path, 'r') as file: # Fecha automaticamente
#    print(file.read())
#with open(path, 'a') as file: # w
 #   file.write("algum texto\n")

#shutil.copyfile(path,'teste2.txt') #souce destination, copy() + permision + dest can be directory; copy2() + matadata
#os.replace('teste2.txt','teste11.txt') # folder

#os.remove('teste11.txt') #rmdir #shutil.rmtree()

#help("modules")

#class name:
#   gen = "Marculino" # class variable
#    def __init__(self,n,age):
#        self.n = n#objeto , instance variable
#        self.age = age

#    def change(self): #metodo
#        print("Seu Nome")
#    def stop(self):
#        return ("Sua idade" + self.age)

#inheritance
#class namef(name):
#    gen2 = "Feminino"
#    def change(self):
#        print("sem nome ppp")

#multi-level inheritance
#class human(namef):
#    pass

#multiple inheritance
#class f():
#    def genf(self):
#        print("Female")
#        return self
#class m():
#    def genm(self):
#        print("male")
#        return self
#class animal(f,m):
#    pass

#no1 = name("CArlos","20")
#no1.change()
#print(no1.n + "\n" + no1.stop())
#no1.gen = "Male"
#print(no1.age + no1.gen)

#no2 = namef("TEste","22")
#no2.change()
#print(no2.n + "\n" + no2.stop())

#animal = animal()
#animal.genf()
#animal.genm()

#method chaining
#animal.genf().genm()
#

##Super() Function
#class prin:
#    def __init__(self, nome,age):
#        self.nome = nome
#        self.age = age

#class alun(prin):
#        def __init__(self, nome, age):
#             super().__init__(nome,age)
#             print("algo")
#class sala(prin):
#        def __init__(self, nome, age):
#              super().__init__(nome, age)
#              print("Diferente")


#aluno = alun("CArlos", 21)
#sala = sala("primeira", 2)
#
#Abstract classes

#class abstracto(ABC):
#    @abstractclassmethod
#    def go(self):
#        pass
#    @abstractclassmethod
#    def stopr(self):
#        pass

#class children(abstracto):
#    color = None
#    def go(self):
#        print("You Can Go")
#        return self
#    def stop(self):
#        print("Stop Punk")
#        return self

#def chage_color(child,color):
#    child.color = color

#t = children()
#t.go().stop()
#objects as arguments
#kid = children()
#chage_color(kid, "red")
#print(kid.color)

#duck_typing 
#class Duck:
#    def walk(self):
#        print("This duck is walking")
#    def talk(self):
#        print("This duck is qwuacking")
#class Chicken:
##    def walk(self):
##        print("This chicken is walking")
#    def talk(self):
#        print("This chicken is qwuacking")
#class Pessoa():
#    def catch(self, duck):
#        duck.walk()
#        duck.talk()

#duck = Duck()
#chicken = Chicken()
#pessoa = Pessoa()

#pessoa.catch(chicken)

#----
# Advanced
#----

#walrus operator :=         #*******
#print (happy := True)

#assign a function to a variable
#def hello():
#    print("Hello")
#hi = hello
#hi()
#say = print
#say("Que porra")

#Higher Order Function
#1. aceita uma função como argumento
#def up(text):
#    return text.upper()
#def hello(func):
#    text = func("Hello")
#    print(text)
#hello(up)

#2.returns a function
#def divisor(x):
#    def dividend(y):
#        return y / x
#    return dividend

#divide = divisor(3)
#print(divide(9))

# Lambda Function parameters:expresion 1 line
#intei = lambda x,y:x + 2 *y
#age_check = lambda age:True if age >=10 else False
#print(age_check(10))
#print(intei(5,10))

#.sort() method   = used with lists key, reverse=true, list
#sort(x) function = used with iterable, reverse, tuplas

#studens = [("Carlos", "B", 26),
#           ("Luisa" , "A",25)]
#studens2 = (("Carlos", "B", 26),
#           ("Luisa" , "A",25))
#a = lambda aa:aa[1]
#studens.sort(key=a) # reverse
#studens2s = sorted(studens2, key=a)
#for i in studens2s:
#    print(i)

#map - applies a function to each item in a iterable (list,tuple,etc)
#store = [("Calça",20.00),
#         ("Camisa",25.00)]

#to_euros = lambda data:(data[0],data[1]*0.82)
#store_euro = list(map(to_euros, store))
#for i in store_euro:
#    print(i)

#filter

#freind = [("CArlos",18), ("Luisa",14)]
#age = lambda data:data[1] >=18
#can_drink = list(filter(age,freind))
#for i in can_drink:
#    print(i)

#reduce
#factorial = [5,4,3,2,1] # junta os 2 primeiros e assim por diante
#result = functools.reduce(lambda x, y:x*y,factorial)
#print(result)

# list comprehension tipo labda só qeu com listas (if/else)
#squares = [i for i in range(1,11) if i <= 5]
#print(squares)

#dictionary comprehension dictionary = {key:expresion for (key,value) in iterable}
#city_in_f = {'Brasilia': 100, "França": 75}
#city_in_c = {key: round((value-32)*(5/9)) for (key,value) in city_in_f.items() if value >75} #(if/else) dentro "X" if value ... else "y"
#print(city_in_c

#zip(*iterables) # agregada elementos de de listas ...etc
#usename = ["Carlos", "Bro"]
#password = ["password","abc123"]
#users = zip(usename, password)
#print(type(users))
#for i in users:
#    print(i)

#import modulo
#print(__name__)
#print(modulo.__name__)

#if __name__ == "__main__":
#    print("runing thhis module directly")
#else:
#    print("running other module indirectly")

#print(time.ctime(0)) #second
#print(time.time())
#print(time.ctime(time.time()))
#.localtime() .strftime("%B %d %Y %H:%M:%S", x) # local time
# .strptime(x,"%d %B %Y") #string representencion of time or date
#tupla = (2020, 4, 20, 4, 20, 0,0,0,0)
#time.asctime(tupla)
#time.mktime(tupla)

import threading, time
#thread = a flow of execution
#cpu bound = program/task internal events CPU
#io bound = program/task external events user input
#def eat_breakfast():
#    time.sleep(3)
#    print("Estudar")
#def coffe():
#    time.sleep(4)
#    print("Café")
#def study():
#    time.sleep(5)
#    print("Cabou o estudo")

#x = threading.Thread(target=eat_breakfast, args=())
#x.start()
#y = threading.Thread(target=coffe, args=())
#y.start()
#z = threading.Thread(target=study, args=())
#z.start()

#x.join()#para o main esperar
#y.join()
#z.join()
#eat_breakfast()
#coffe()
#study()

#print(threading.active_count())
#print(threading.enumerate())
#print(time.perf_counter())

# daemon thread - thats runs in the background, not important for program to run
# non-daemon, cannot normaly killed, stay alive ultin task is complete
#def timer():
#    print()
#    print()
#    cout = 0
#    while True:
#        time.sleep(1)
#        cout += 1
#        print("Logger in for: ", cout, " seconds")

#x = threading.Thread(target=timer, daemon=(True))
#x.start()
##x.setDaemon(True)
#print(x.isDaemon)
#answer = input("Quer sair? ")

##multitheading - better for cpu bound tasks (heavy cpu usage) 
#Multiprocessinf - running tasks in parallel, better for cpu bound tasks (heavy cpu usage) diferent cpu cores

#from multiprocessing import Process, cpu_count
#import time
#def counter(num):
#    count =0
#    while count < num:
#        count += 1
#def main():
#    print(cpu_count())
#    a = Process(target=counter, args=(500000000,))
#    b = Process(target=counter, args=(500000000,))
    #a.start()
    #b.start()
    #a.join()
    #b.join()
#    print("Tempo", time.perf_counter())

#if __name__ == '__main__':
#    main()





#multiply = lambda x, y: x * y
#print(multiply(5,5))





#import tkinter as tk

#def my_function():
#    print("A função foi executada!")

#root = tk.Tk()
#root.withdraw()
#while True:
#    my_function()
#root.mainloop()






