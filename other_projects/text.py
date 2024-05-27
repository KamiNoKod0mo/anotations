import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def muda_cor():
    color = colorchooser.askcolor(title='Escolha')
    text_area.config(fg=color[1])

def muda_fonte(*args):
    text_area.config(font=(font_name.get(),size_box.get()))

def novo_arq():
    window.title("Untitled")
    text_area.delete(1.0,END)

def abre_arq():
    file = askopenfilename(defaultextension='.txt', file=[("All files", "*.*"), ("Text Documents","*.txt")])
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, 'r')

        text_area.insert(1.0,file.read())
    except Exception:
        print("Não deu para abri")
    finally:
        file.close()

def salva():
    file = filedialog.asksaveasfilename(initialfile='untitled.txt',
                                        defaultextension='.txt',
                                        filetypes=[("All Files", "*.*"),
                                        ("Text Documents", "*.txt")])
    
    if file == "":
        return 

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")
            file.write(text_area.get(1.0,END))
        except Exception:
            print("Não Salvou")
        finally:
            file.close()
        
def corta():
    text_area.event_generate("<<Cut>>")

def copia():
    text_area.event_generate("<<Copy>>")

def cola():
    text_area.event_generate("<<Paste>>")

def sobre():
    showinfo("About", "Versão 1.0")

def sair():
    window.destroy()

window = Tk()
window.title("Editor de Texto")
file = None

window_width = 500
window_heighy = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x =int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_heighy / 2))


window.geometry("{}x{}+{}+{}".format(window_width,window_heighy,x,y))

font_name = StringVar(window)
font_name.set('Arial')
font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky=N + E + S + W)

scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

color_butoon = Button(frame, text='Color', command=muda_cor)
color_butoon.grid(row=0,column=0)

font_b = OptionMenu(frame, font_name, *font.families(), command=muda_fonte)
font_b.grid(row=0,column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=muda_fonte)
size_box.grid(row=0,column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label='New',command=novo_arq)
file_menu.add_command(label='Open',command=abre_arq)
file_menu.add_command(label='Save',command=salva)
file_menu.add_separator()
file_menu.add_command(label='Quit',command=sair)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut', command=corta)
edit_menu.add_command(label='Copy', command=copia)
edit_menu.add_command(label='Paste', command=cola)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About', command=sobre)


window.mainloop()


