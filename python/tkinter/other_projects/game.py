from tkinter import *
import time

#Constantes
COMP = 700
ALTU = 650
Velx = 2
Vely = 5

#Funçoes
def destroi(b):
    canvas.delete(a[b])
    listcood[b]=[0.0,0.0,0.0,0.0]
def bola(Velx,Vely):
    image = canvas.create_oval(25,300,50,325,fill='red')
    while True:
        #Objetos
        cood =  canvas.coords(image)
        coodp = canvas.coords(plata)
        coodpy = coodp[1] -5
        #Movimento da Bola
        if((cood[2] >= (canvas.winfo_width()) or cood [0] < 0)):
            Velx = -Velx
        if(cood[3]>=(canvas.winfo_height()) or cood[1] < 0):
            Vely = -Vely
        #Colisão com a Plataforma
        if cood[1] == coodp[1]-25.0:
            for i in range(int(coodp[0]-25),int(coodp[2]),1):
                if cood[0] == float(i):
                    Vely = -Vely
        #Colisão com os Blocos
        #print(cood[3])
        for b in range(198):
            for x in range(int(listcood[b][1]),int(listcood[b][3])):
                if cood[1] == float(x): 
                    for i in range(int(listcood[b][0]),int(listcood[b][2])):
                    
                        if cood[0] == float(i):
                            Vely = -Vely
                            destroi(b)
                       
        canvas.move(image,Velx,Vely)
        time.sleep(0.01)
        windows.update()
def blocos(x):
    x1=20
    x2=40
    y1=0
    y2=20
    global a 
    a = []
    for i in range(x):
        a.append(i)
    for i in  range(x):
        e = 3
        global listcood
        a[i]=(canvas.create_rectangle(x1,y1,x2,y2,fill='black'))
        canvas.pack()
        windows.update()
        listcood = []
        for i in range(x):
            listcood.append(canvas.coords(a[i]))
        x1= x1+20
        x2= x2+20
        if x2 == 700:
            x1=20
            x2=40
            y1= y1+40
            y2= y2+40
    


        
#Janela
windows = Tk()
windows.resizable(False,False)
windows.title('Ball')

canvas = Canvas(windows, bg='blue', height=ALTU, width=COMP)
canvas.pack()
windows.update()
# Centralização da Janela
window_width = windows.winfo_width()
window_height = windows.winfo_height()
screen_width = windows.winfo_screenwidth()
screen_height = windows.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
windows.geometry(f"{window_width}x{window_height}+{x}+{y}")

#Plataforma
m = 0
plata = canvas.create_rectangle(300,560,400,575,fill="black")

#Movimento Da Plataforma
def move_left(event):
    global m
    if m == -300:
        canvas.move(plata,0,0)
    else:
        canvas.move(plata,-15,0)
        m = m -15
def move_right(event):
    global m
    if m == 300:
        canvas.move(plata,0,0)
    else:
        canvas.move(plata,15,0)
        m = m +15
    
windows.bind("<a>",move_left)
windows.bind("<d>",move_right)

#blocos
blocos(198)


#Bolinha
bola(Velx,Vely)
windows.mainloop()