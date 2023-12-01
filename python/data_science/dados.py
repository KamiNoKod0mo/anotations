import matplotlib.pyplot as plt

plt.title("SquareNumbers", fontsize=24) 
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both',labelsize=14) #Define o tamanho dos rótulos das marcações

input_values = [1, 2, 3, 4, 5] # valores
squares = [1, 4, 9, 16, 25]

plt.scatter(2, 5) # associa x,y
plt.scatter(input_values,squares,s=100,color=(0, 0, 0.8)) # associa valores de lista individualmente s-tamanhot, c= troca a cor

plt.plot(input_values,squares, linewidth=5) # associa todos os valores # linha

x_values = list(range(1, 6)) #valores gerados
y_values = [x**1 for x in x_values]

plt.scatter(x_values, y_values, s=100,edgecolor='none',c=y_values, cmap=plt.cm.Blues)# remove borda e gradiente
plt.axis([0, 6, 0, 26])#Define o intervalo para cada eixo

#plt.show() # mostra
plt.savefig('/squares_plot.png',bbox_inches='tight') #salva 

