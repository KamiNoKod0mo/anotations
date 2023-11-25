from tkinter import *
#import tkinter as tk
#import ttkbootstrap as ttk
from tkinter import ttk
from tkinter import scrolledtext
#widgets gui elements
#windows - serves as a container to hold the widgets

#window =  Tk() #instantiate of a window
#window = ttk.Window(themename='journal')
#window.geometry("420x420")
#window.title("Fist GUI")
#window.iconbitmap('...'m)
###
#windows size
#window.minsize(200,200)
#window.maxsize(1000,500)
#window.resizable(True,True)
#####
#scren size
#print(window.winfo_screenwidth())
#print(window.winfo_screenheight())
#####
#window.attributes('-alpha',0.1)
#window.attributes('-topmost', True)
#-disable, -fullscreen
#window.overrideredirect(True)
#grip =ttk.Sizegrip(window)
#grip.place(relx = 1.0,rely = 1.0,anchor='se',relwidth=1) #relative position, nw,ne,se,sn
#####
#icon = PhotoImage(file='casa.png')
#window.iconphoto(True, icon)
#window.config(background='yellow') # hex color too
#window.mainloop() # place windows on computeer scren, listen for events

#label an area widget that holds text and/or an image within a window 
#photo2 = PhotoImage(file='casa.png')
#Label = Label(window,text='Hello word',
#                        font=('Arial',40,'bold'),
#                        fg='red',bg='white',
#                        relief=RAISED,# sunken
#                        bd=10,
#                        padx=20,
#                        pady=20,
#                        image=photo2,
#                        compound='bottom')
#Label.pack() # Top to the Bottom in default
#Label.place(x=0,y=0,width= 20,height =10)#fixed possition
######
#butons = clack it, then it does stuff
#count = 0
#def click():
#    global count
#    count +=1
#    print(count)
#photo3 = PhotoImage(file='casa.png')
#button = Button(window,
#                text='Click sera',
#                command=click,
#                font=('Comic Sans',30),
#                fg='green',bg='pink',u
#                activeforeground='green',activebackground='pink',
#                state=ACTIVE,
#                image=photo3,
#                compound='bottom'
#                )
#button.pack()
###########################
#entry widget
#def submit():
#    user = entry.get()
#    print('Hello ' + user)
    #entry['state'] = DISABLE
#    entry.config(state=DISABLED)
#def delete():
#    entry.delete(0,END)
#def apaga():
#    entry.delete(len(entry.get())-1,END)

#entry = Entry(window,
#              font=('Arial',50),
#                    fg='pink',bg='yellow',
#                    show='*')
#entry.insert(0,'Nome')
#entry.pack(side=LEFT)

#submit = Button(window,text='Submit',command=submit)
#submit.pack(side=RIGHT)
#delete = Button(window,text='deletar',command=delete)
#delete.pack(side=RIGHT)
#backspa= Button(window,text='Apagar',command=apaga)
#backspa.pack(side=RIGHT)
##########
#check buttons
#def display():
#    if(x.get() == 1):
#        print("Voçe aceito")
#    else:
#        print("Não aceito")
#x = IntVar() # 0 or 1 ou BooleanVaar ou StringVar
#photo4 = PhotoImage(file='casa.png')
#check = Checkbutton(window,
#                    text='Eu aceito'
#                    ,variable=x,
#                    onvalue=1,offvalue=0,
#                    command=display,
#                    font=('arial',20),
#                    fg='blue',bg='green',
#                    activebackground='green',activeforeground='blue',
#                    padx=25,pady=10,
#                    image=photo4,compound='left')
#check.pack()
#########
#Radio button
#def order():
#    if(y.get()==0):
#        print('You odered arroz')
#    elif(y.get()==1):
#        print('You odered Feijão')
#    elif(y.get()==2):
#        print('You odered carne')
#photo5 = PhotoImage(file='casa.png') # da para usar em uma lista
#food = ["arroz",'feijao', 'carne']
#y = IntVar()
#for index in range(len(food)):
#    radiob = Radiobutton(window,text=food[index],
#                        variable=y,value=index,
#                        padx=25,
#                        font=("Impact",40),
#                        image=photo5,compound='left',
#                        indicatoron=0, #tira os circulos
#                        width=375,command=order)
#    radiob.pack(anchor=W)
############
#Scale
#htp = PhotoImage(file='casa.png')
#hlabel = Label(image=htp)
#hlabel.pack()  
#def sub():
#    print('Temp: ' + str(scacle.get()) + " C")
#scacle = Scale(window,from_=100,to=0,
#               length=600,orient=VERTICAL,
#               font = ('consolas',20),
#               tickinterval=10,
#               showvalue= 0,#hide current value
#               resolution= 5,
#               troughcolor='red',
#               fg='red',bg='black',command= lambda value:print(value))
#scacle.set(40)
#scacle.pack()

#buto = Button(window,text='subimit',command=sub)
#buto.pack()
########
###List Box
#def suba():
#    #print(listbox.get(listbox.curselection()))
#    food = []
#    for index in listbox.curselection():
#        food.insert(index,listbox.get(index))
#    for index in food:
#        print(index)
#def add():
#    listbox.insert(listbox.size(),enbox.get())
#    listbox.config(height=listbox.size())
#def dele():
#    #listbox.delete(listbox.curselection())
#    for index in reversed(listbox.curselection()):
#        listbox.delete(index)
#    listbox.config(height=listbox.size())
#listbox = Listbox(window,
#                  bg="red",
#                  font=("Constantia",35),
#                  width=12,
#                  selectmode=MULTIPLE)
#listbox.pack()
#listbox.insert(1, 'Pizza')
#listbox.insert(2, 'Arroz')
#listbox.insert(3, 'Feijão')
#listbox.insert(4, 'Batata')

#listbox.config(height=listbox.size())
#enbox = Entry(window)
#enbox.pack()

#butos = Button(window,text='sub',command=suba)
#butos.pack()
#addbuto = Button(window,text='add',command=add)
#addbuto.pack()
#delbuto = Button(window,text='del',command=dele)
#delbuto.pack()
#################
#Messagebox 
#from tkinter import messagebox

#def click():
    #messagebox.showinfo(title='This a teste',message="Good")
    #messagebox.showwarning(title='This a teste2',message="bad")
    #messagebox.showerror(title='This a teste3',message="erro")
    #if messagebox.askokcancel(title='This a teste4',message="ask") == True:
    #    print("OK")
    #else:
    #    print("Não ok")
    #messagebox.askretrycancel(title='This a teste5',message="rask")
    #messagebox.askyesno(title='This a yes',message="sim ou nao") 
    #messagebox.askquestion(title='This a testeaaaaa',message="Question") # yes or no
    #messagebox.askyesnocancel(title='yes yess',message="Do you do",icon='warning') # True False None

#but = Button(window,command=click, text='Click me')
#but.pack()
#############
#color chooser
from tkinter import colorchooser # submodule
#def cli():
    #color = colorchooser.askcolor()
    #colohex = color[1]
#    window.config(bg=colorchooser.askcolor()[1])

#window.geometry("420x420")
#butto = Button(text='Click',command=cli)
#butto.pack()
#############
#text area/text widget
#def su():
#    input = texto.get("1.0",END)
#    print(input)
#texto = Text(window,bg='light yellow',
#             font=('Ink Free',25),
#             height=8,width=20,
#             padx=20,pady=20,
#             fg="purple")
#texto.pack()

#butto = Button(text='Submit',command=su)
#butto.pack()
####################
#filedialog
from tkinter import filedialog
#def up():
#    path = filedialog.askopenfilename(initialdir='C:\\Users\\Carlo\\Desktop',title='Titulo',
#                                      filetypes=(("text files","*.txt"),("All files","*")))
#    file = open(path,'r')
#    print(file.read())
#    file.close()
#buttup = Button(text='Open',command=up)
#buttup.pack()
#Save file ##########
#def savef():
#    file = filedialog.asksaveasfile(initialdir='C:\\Users\\Carlo\\Desktop',
#                                    defaultextension='.txt',
#                                    filetypes=[
#                                        ("Text file",'.txt'),
#                                        ("HTML file", ".html"),
#                                        ("All files", ".*")
#                                    ])
#    if file is None:
#        return
#    filet = str(text.get(1.0,END))
    #input
#    file.write(filet)
#    file.close()

#buttsa = Button(text='save',command=savef)
#buttsa.pack()
#text = Text(window)
#text.pack()

#############
#Menu bar
#t = PhotoImage(file="casa.png")
#def op():
#    print("Open")
#def sa():
#    print("Save")
#menu
#menubar = Menu(window)#tk.Menu
#window.config(menu=menubar)

#subMenu
#filemenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
#menubar.add_cascade(label="File",menu=filemenu)

#filemenu.add_command(label="Open",command=op)
#filemenu.add_command(label="Save",command=sa)
#filemenu.add_separator()
#filemenu.add_command(label="Exit",command=quit)

#def cut():
#    print("Cut")
#def cop():
#    print("Copy")
#def pas():
#    print("Paste")3

#editmenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
#menubar.add_cascade(label="Edit",menu=editmenu)
#editmenu.add_command(label="Cut",command=cut,image=t,compound='right')
#editmenu.add_command(label="Copy",command=cop)
#editmenu.add_command(label="Paste",command=pas)

################
#Frame

#frame = Frame(window,bg="Pink",bd=5,relief=SUNKEN)
#frame.place(x=0,y=0)

#Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP)
#Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
#Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
#Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)

####################
#New windows
#def crew():
#    neww = Tk() # new windows 'on the top' of the other windwows,linked to a 'bottom' widows
                        #tk independent window
#    window.destroy()
#Button(window,text="Create a new Window",command=crew).pack()
##############
#tabs
#from tkinter import ttk

#note = ttk.Notebook(window)# widget that menages a collection of windows/displays
#tab1 = ttk.Frame(note)
#tab2 = ttk.Frame(note)

#title_label = ttk.Label(master= window, text= 'Miles ',font='Calibri 24 bold')
#title_label.pack()

#note.add(tab1,text="Tab 1")
#note.add(tab2,text="Tab 2")

#note.pack(expand=True,fill="both")

#Label(tab1,text=("Hello"),width=50,height=25).pack()
#Label(tab2,text=("Good bye"),width=50,height=25).pack()


###############
#grids

#titleLabel = Label(window,text="Suas Informações",font=('Arial',25)).grid(row=0,column=0,columnspan=2)

#fnl = Label(window,text='Fist Name: ',width=20,bg='red').grid(row=1,column=0)
#fne = Entry(window).grid(row=1,column=1)

#lnl = Label(window,text='Last Name: ',bg='green').grid(row=2,column=0)
#lne = Entry(window).grid(row=2,column=1)

#enl = Label(window,text='Email: ',width=30,bg='Blue').grid(row=3,column=0)
#ene = Entry(window).grid(row=3,column=1)

#subb = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)
######################
#Progresor
#from tkinter.ttk import *
#import time
#def start():
#    GB = 100
#    download = 0
#    speed = 1
#    while(download<GB):
#        time.sleep(0.05)
#        bar['value']+=(speed/GB)*100
#        download+=speed
#        percent.set(str(int((download/GB)*100))+"%")  
#        text.set(str(download)+"/"+str(GB) + " Tasks Completed")  
#        window.update_idletasks()
#percent = StringVar() 
#text = StringVar()

#bar = ttk.Progressbar(window,orient=HORIZONTAL,length=300)
#bar.pack(pady=10)

#percentlabel = Label(window,textvariable=percent).pack()
#textlabel = Label(window,textvariable=text).pack()

#butaa = Button(window,text='Download',command=start).pack()
#####################
#Canvas draw graphs, plots, images in a window
#canvas = Canvas(window,height=500,width=500)
#canvas.create_line(0,0,500,500,fill="Blue",width=5)
#canvas.create_rectangle(50,50,250,250,fill="pink",dash=(4,2,1,1))
#points = [250,0,500,500,0,500]
#canvas.create_polygon(points,fill="green",outline='black',width=5)
#canvas.create_arc(0,0,500,500,style=PIESLICE,start=90,extent=90)
#canvas.create_oval(190,190,310,310)

#canvas.create_window((150,100), window=ttk.Button(window,text= 'teste'))

#canvas.pack()
##################
#keyboards events
#def do(event):
#    print("Aperto: " + event.keysym)
#    labell.config(text=event.keysym)
#window.bind("<Key>",do)

#labell = Label(window,font=('Helvetica', 100))
#labell.pack()
####################
#mouse events
#def doso(event):
#    print("Algo " + str(event.x)+ ", " + str(event.y))

#window.bind("<Button-1>",doso)
#window.bind("<Button-2>",doso)
#window.bind("<Button-3>",doso)
#window.bind("<ButtonRelease>",doso)
#window.bind("<Enter>",doso)
#window.bind("<Leave>",doso)
#window.bind("<Motion>",doso)
###############
#drag and drop
#def drag(event):
#    widget = event.widget
#    widget.startX = event.x
#    widget.starty = event.y
#def drag_mo(event):
#    widget = event.widget
#    x = widget.winfo_x() - widget.startX + event.x
#    y = widget.winfo_y() - widget.starty + event.y
#    widget.place(x=x,y=y)
#la = Label(window,bg='red',width=10,height=5)
#la.place(x=0,y=0)

#la2 = Label(window,bg='blue',width=10,height=5)
#la2.place(x=100,y=100)

#la.bind("<Button-1>",drag)
#la.bind("<B1-Motion>",drag_mo)

#la2.bind("<Button-1>",drag)
#la2.bind("<B1-Motion>",drag_mo)
###############
#move images
#def move_up(event):
#    ll.place(x=ll.winfo_x(), y=ll.winfo_y()-10)
#def move_down(event):
#    ll.place(x=ll.winfo_x(), y=ll.winfo_y()+10)
#def move_left(event):
#    ll.place(x=ll.winfo_x()-10, y=ll.winfo_y())
#def move_right(event):
#    ll.place(x=ll.winfo_x()+10, y=ll.winfo_y())


#window.geometry('500x500')

#window.bind("<w>",move_up)
#window.bind("<s>",move_down)
#window.bind("<a>",move_left)
#window.bind("<d>",move_right)
#window.bind("<Up>",move_up)
#window.bind("<Down>",move_down)
#window.bind("<Left>",move_left)
#window.bind("<Right>",move_right)

#ima = PhotoImage()
#ll = Label(window, bg='red', width=10,height=5)
#ll.place(x=0,y=0)
##########
#def move_up(event):
#    can.move(myimage,0,-10)
#def move_down(event):
#    can.move(myimage,0,10)
#def move_left(event):
#    can.move(myimage,-10,0)
#def move_right(event):
#    can.move(myimage,10,0)

#window.bind("<w>",move_up)
#window.bind("<s>",move_down)
#window.bind("<a>",move_left)
#window.bind("<d>",move_right)

#can = Canvas(window,width=500,height=500)
#can.pack()
#photo = PhotoImage(file="casa.png")
#myimage = can.create_image(0,0,image=photo,anchor=NW)
################
#animation
#import time

#WIDHT = 500
#HEIGHT = 500
#xVel = 3
#yVel = 2

#canv = Canvas(window,width=WIDHT,height=HEIGHT,bg='red')
#canv.pack()

#p_ima = PhotoImage(file='casa.png')
#m_ima = canv.create_image(0,0,image=p_ima,anchor=NW)

#image_width = p_ima.width()
#image_height = p_ima.height()

#while True:
#    cood = canv.coords(m_ima)
#    print(cood)
#    if(cood[0]>=WIDHT-image_width or cood[0]<0):
#        xVel = -xVel
#    if(cood[1]>=HEIGHT-image_height or cood[1]<0):
#        yVel = -yVel
#    canv.move(m_ima,xVel,yVel)
#    window.update()
#    time.sleep(0.01)
####################
#multiple animations
#import time
#WIDHT = 500
#HEIGHT = 500
#class ball:
#    def __init__(self,canvas,x,y,diametro,xvel,yvel,color):
#        self.canvas = canvas
#        self.image = canvas.create_oval(x,y,diametro,diametro,fill=color)
#        self.xvel = xvel
#        self.yvel = yvel
#    def move(self):
#        coods = self.canvas.coords(self.image)
#        print(coods)
#        if(coods[2]>=(self.canvas.winfo_width()) or coods[0]<0):
#           self.xvel= -self.xvel
#        if(coods[3]>=(self.canvas.winfo_height()) or coods[1]<0):
#           self.yvel= -self.yvel    
#        self.canvas.move(self.image,self.xvel,self.yvel)
#canva = Canvas(window,width=WIDHT,height=HEIGHT)
#canva.pack()

#volley = ball(canva,0,0,100,2,3,'red')
#tennis = ball(canva,0,0,50,5,4,'orange')
#bas = ball(canva,0,0,125,8,7,'Blue')
#while True:
#    volley.move()
#    tennis.move()
#    bas.move()
#    window.update()
#    time.sleep(0.01)
#####################
#clock progama
#from time import *
#def update():
#    timeS = strftime('%I:%M:%S %p')
#    tlabel.config(text=timeS)

#    dayS = strftime('%A')
#    dlabel.config(text=dayS)

#    dateS = strftime('%B %d, %Y')
#    dalabel.config(text=dateS)

#    window.after(1000,update)

#tlabel = Label(window,font=('Arial',50),fg='red',bg='black')
#tlabel.pack()

#dlabel = Label(window,font=('Ink Free',50),fg='green',bg='black')
#dlabel.pack()

#dalabel = Label(window,font=('Ink Free',30),fg='blue',bg='black')
#dalabel.pack()

#update()
####################
#send email
#import smtplib
#sender = 'carlos.farias1267@gmail.com'
#rece = "carlos.henrique19444@gmail.com"
#password = "oliveira3003carlos"
#subject = "Teste"
#body = "Em Python"

#messa = f"""From: Carlos {sender}
#to: Rico{rece}
#Subject: {subject}\n
#{body}
#"""

#server = smtplib.SMTP("smtp.gmail.com",587)
#server.starttls()

#server.login(sender,password)
#print("Logged in...")
#server.sendmail(sender, rece, messa)
#print('Mandou')
##################333
#pip
#pip install --upgrade pip
#pip list
#pip list --outdated
#pip install "namepackage"
#
#
#
#pyinstaller -F -w python2.py -i icon.icon



###
#item = ('a','b','c')
#combo = ttk.Combobox(window)
#combo.configure(values=item)
#combo.pack()

#spin = ttk.Spinbox(window,from_=0, to=10,increment=1)
#spin.pack()
###
#name = ['carlos', 'teste']
#last = ['henrique', 'testando']
# treeview
#table = ttk.Treeview(window,columns=('first','last'),show='headings')
#table.heading('first',text='First name')
#table.heading('last',text='Surname')
#table.pack(fill= 'both', expand= True)

#for i in range(0,2):
#    table.insert(parent= '', index=0,values= (name[i],last[i]))
####
#scroll text(simple)
#scrolled_text = scrolledtext.ScrolledText(window,width=100,height=5)
#scrolled_text.pack()

###grid 2.0
#nl = Label(window,text='Fist Name: ',width=20,bg='red')
#nl2 = Label(window,text='foda: ',width=20,bg='blue')

#window.columnconfigure(0,weight=1)
#window.columnconfigure(1,weight=1)

#window.rowconfigure(0,weight=1)
#window.rowconfigure(1,weight=1)

#nl.grid(row= 0,column=1, sticky='nsew')
#nl2.grid(row=1,column=0,columnspan=2,sticky='nsew')

#label.grid_forget()
#######
#nl.lift()
#nl2.lower()
#nl.tkraise(aboveThis=nl2)
######33
#import tkinter as tk

#class App(tk.Tk):
#    def __init__(self,title,size):
#        super().__init__()
#        self.title(title)
#        self.geometry(size)

#        self.mainloop()

#App("teste",('500x500')) 
#window.mainloop()


#import tkinter as tk
#from tkinter import ttk, font

# window
#window = tk.Tk()
#window.title('Styling')
#window.geometry('400x300')

# print(font.families())

# style 
#style = ttk.Style()
# print(style.theme_names())
# style.theme_use('classic')

#style.configure('new.TButton', foreground = 'green', font = ('Jokerman', 20))
#style.map('new.TButton', 
#	foreground = [('pressed', 'red'),('disabled', 'red')],
#	background = [('pressed', 'green'), ('active', 'blue')])
#style.configure('TFrame', background = 'pink')

# widgets 
#label = ttk.Label(
#	window, 
#	text = 'A label\nAnd then type on another line', 
#	background = 'red', 
#	foreground = 'white',
#	font = ('Jokerman', 20),
#	justify = 'right')

#label.pack()

#button = ttk.Button(window, text = 'A button', style = 'new.TButton')
#button.pack()

# exercise: 
# add a frame with a width and height and give it a pink background color

#frame = ttk.Frame(window, height = 200, width = 100)
#frame.pack()

# run 


#window.mainloop()
#####################3
#extra widgets
""" import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter


window = ttk.Window(themename='darkly')
window.title('extra widgets')

scroll_frame = ScrolledFrame(window)
scroll_frame.pack(expand= True, fill = 'both')

for i in range(100):
    frame = ttk.Frame(scroll_frame)
    ttk.Label(frame, text= f'Label: {i}').pack(fill='x',side='left')
    ttk.Button(frame, text = f'Button: {i}').pack(fill = 'x', side='left')
    frame.pack(fill = 'x', expand=True)

toasat = ToastNotification(
    title='This is a message title',
    message = 'This is the actual message',
    duration = 2000,
    bootstyle='dark',
    position= (0,0,'ne')
)

ttk.Button(window, text='Show toast', command= toasat.show_toast).pack()
# tooltip
button = ttk.Button(window, text = 'tooltip button', bootstyle='warning')
button.pack(pady=10)
ToolTip(button, text= 'faz algo', bootstyle='danger-inverse')

#calendar
calendar = DateEntry(window)
calendar.pack(pady= 10)

ttk.Button(window,text='get calendar date',command=lambda: print(calendar.entry.get())).pack()

#progress - floodgauge
progress_int = tk.IntVar(value = 50)
progress = ttk.Floodgauge(window, text='progress', variable=progress_int,bootstyle='danger',mask='mask {}%')
progress.pack(pady= 10, fill='x')

ttk.Scale(window, from_ = 0, to =100, variable=progress_int).pack()
#meter
meter = ttk.Meter(
    window,
    amountused= 10,
    interactive= True,
    metertype= 'semi',
    subtext= 'some other text',
    bootstyle= 'danger'
    )
meter.pack()

window.mainloop()
 """
#########
#Animacion
""" import customtkinter as ctk
from random import choice

class SlidePanel(ctk.CTkFrame):
    def __init__(self,parent,start_pos,end_pos):
        super().__init__(master=parent)

        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width =  abs(start_pos - end_pos)
        #print(self.width)
        self.place(relx=self.start_pos,rely=0.05,relwidth=self.width , relheight = 0.9)

        self.pos = start_pos
        self.in_start_pos = True

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx = self.pos, rely=0.05, relwidth=self.width, relheight = 0.9)
            self.after(10,self.animate_forward)
        else:
            self.in_start_pos = False
    
    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx = self.pos, rely=0.05, relwidth=self.width, relheight = 0.9)
            self.after(10,self.animate_backwards)
        else:
            self.in_start_pos = True

def move_btn():
    global button_x
    button_x += 0.001
    button.place(relx = button_x, rely=0.5,anchor = 'center')
    if button_x < 0.9:
        window.after(10,move_btn)

def infinite_print():
    global button_x
    button_x += 0.5
    if button_x < 10:
        print('infinite')
        print(button_x)
        window.after(100,infinite_print)

window = ctk.CTk()
window.title('Animated Widgets')
window.geometry('600x400')
#ctk.set_appearance_mode('light')

animated_panel = SlidePanel(window,1.0,0.7)
ctk.CTkLabel(animated_panel,text='Label 1').pack(expand = True, fill= 'both', padx=2,pady=10)
ctk.CTkLabel(animated_panel,text='Label 1').pack(expand = True, fill= 'both', padx=2,pady=10)
ctk.CTkButton(animated_panel,text='Button').pack(expand = True, fill= 'both', padx=2,pady=10)


button_x = 0.5
button = ctk.CTkButton(window, text= 'toggle sidebar', command=animated_panel.animate)
button.place(relx = button_x, rely =0.5,anchor = 'center')
window.mainloop() """

#####images pillow
""" import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

def stretch_image(event):
    global resized_tk
    width = event.width
    height = event.height

    resized_image = image_orin.resize((width,height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    canvas.create_image(0,0,image=resized_tk,anchor = 'nw')

def fill_image(event):
    global resized_tk

    canvas_ratio = event.width / event.height
    if canvas_ratio > image_ratio:
        width = int(height*image_ratio)
        height = int(event.height)
    else:
        width = int(event.width)
        height =int(width/image_ratio)
    resized_image = image_orin.resize((width,height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(
        int(event.width /2),int(event.height/2),anchor = 'center',image=resized_tk
    )

window = tk.Tk()
window.geometry('600x400')
window.title('Imagens')
#grid
window.columnconfigure((0,1,2,3), weight= 1, uniform= 'a')
window.rowconfigure(0,weight= 1)
#
image_orin = Image.open('/home/carlos_/Desktop/Projects/Python/annotation/958580.jpg')
image_ratio = image_orin.size[0] / image_orin.size[1]
image_tk = ImageTk.PhotoImage(image_orin)

image_p = Image.open('/home/carlos_/Desktop/Projects/Python/annotation/programming-hold-code.png').resize((30,30))
image_p_tk = ImageTk.PhotoImage(image_p)

img_ctk = ctk.CTkImage(
    light_image= Image.open('/home/carlos_/Desktop/Projects/Python/annotation/programming-hold-code.png'),
    dark_image= Image.open('/home/carlos_/Desktop/Projects/Python/annotation/programming-hold-code.png')
)

#label = ttk.Label(window,text='teste',image=image_tk)
#label.pack()

button_frame = ttk.Frame(window)

button = ttk.Button(button_frame,text = 'A button', image=image_p_tk, compound='left')
button.pack(pady=10)

button_ctk = ctk.CTkButton(button_frame,text = 'A button', image=image_p_tk, compound='left')
button_ctk.pack(pady=10)

button_frame.grid(column=0,row=0,sticky='nsew')

canvas = tk.Canvas(window,background='black',bd=0,highlightthickness= 0, relief='ridge')
canvas.grid(column = 1,columnspan=3, row =0,sticky= 'nsew')
canvas.create_image(0,0,image=image_tk,anchor='nw') 

canvas.bind('<Configure>',stretch_image)


window.mainloop()

 """
##Animation
#...
#change the tittle bar color
""" import customtkinter as ctk
from ctypes import windll, byref, sizeof,c_int

app = ctk.CTk(fg_color='red')
app.geometry('300x200')

HWND = windll.user32.GetParent(app.winfo_id())
title_bar_color = 0x000000FF
windll.dwmapi.DwmSetWindowAttribute(HWND,35,
    byref(c_int(title_bar_color)),
    sizeof(c_int))


app.mainloop() """


