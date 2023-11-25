from random_walk import RandomWalk
import matplotlib.pyplot as plt

while True:

    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points)) 

    
    
    # Criar uma figura e um eixo, e define tamanho
    fig, ax = plt.subplots(dpi=128,figsize=(10, 6))
    #plt.figure(figsize=(10, 6))

    plt.scatter(rw.x_values,rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    plt.scatter(0, 0, color='green',edgecolors='none', s=100) 
    plt.scatter(rw.x_values[-1], rw.y_values[-1],color='red', edgecolors='none', s=100)

    # Desativar a visibilidade dos eixos x e y
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)  

    

    plt.show()
    keep_running = input("Make another walk? (y/n): ") 
    if keep_running =='n': 
        break