from tkinter import *
import customtkinter
import random

# Anthony Gabriel Neves Mendes


def proxima_jogada(linha, coluna):
    global jogador
    if botoes[linha][coluna]['text'] == "" and verificar_vencedor() is False:
        if jogador == jogadores[0]:
            botoes[linha][coluna]['text'] = jogador
            if verificar_vencedor() is False:
                jogador = jogadores[1]
                # rotulo.config
                rotulo.configure(text=(jogadores[1] + ' vez'))
            elif verificar_vencedor() is True:
                rotulo.configure(text=(jogadores[0] + ' venceu'))
            elif verificar_vencedor() == "Empate":
                rotulo.configure(text=('Empate!'))
        else:
            botoes[linha][coluna]['text'] = jogador
            if verificar_vencedor() is False:
                jogador = jogadores[0]
                rotulo.configure(text=(jogadores[0] + ' vez'))
            elif verificar_vencedor() is True:
                rotulo.configure(text=(jogadores[1] + ' venceu'))
            elif verificar_vencedor() == "Empate":
                rotulo.configure(text=('Empate!'))
# Yoel Gomez
# Carlos Henrique


def verificar_vencedor():
    for linha in range(3):
        if botoes[linha][0]['text'] == botoes[linha][1]['text'] == botoes[linha][2]['text'] != "":
            botoes[linha][0].configure(bg='green')
            botoes[linha][1].configure(bg='green')
            botoes[linha][2].configure(bg='green')
            return True
    for coluna in range(3):
        if botoes[0][coluna]['text'] == botoes[1][coluna]['text'] == botoes[2][coluna]['text'] != "":
            botoes[0][coluna].configure(bg='green')
            botoes[1][coluna].configure(bg='green')
            botoes[2][coluna].configure(bg='green')
            return True

    if botoes[0][0]['text'] == botoes[1][1]['text'] == botoes[2][2]['text'] != "":
        botoes[0][0].configure(bg='green')
        botoes[1][1].configure(bg='green')
        botoes[2][2].configure(bg='green')
        return True
    elif botoes[2][0]['text'] == botoes[1][1]['text'] == botoes[0][2]['text'] != "":
        botoes[0][2].configure(bg='green')
        botoes[1][1].configure(bg='green')
        botoes[2][0].configure(bg='green')
        return True

    elif espacos_vazios() is False:
        for linha in range(3):
            for coluna in range(3):
                botoes[linha][coluna].config(bg='yellow')
        return "Empate"
    else:
        return False
# Carlos Henrique
# Tarcisio Trindade


def espacos_vazios():
    espaco = 9
    for linha in range(3):
        for coluna in range(3):
            if botoes[linha][coluna]['text'] != "":
                espaco -= 1
    if espaco == 0:
        return False
    else:
        return True
# Tarcisio Trindade

# Vitor Alcantara


def novo_jogo():
    global jogador
    jogador = random.choice(jogadores)
    # rotulo.config(text=jogador + " vez")
    rotulo.configure(text=jogador + " vez")

    for linha in range(3):
        for coluna in range(3):
            botoes[linha][coluna].config(
                text='', bg="#275db3", bd=1, highlightbackground='#000000')
# Vitor Alcantara


# Carlos Henrique
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
janela = customtkinter.CTk()

janela.title("Jogo da Velha")
janela.resizable(False, False)
jogadores = ['X', 'O']
jogador = random.choice(jogadores)

botoes = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# rotulo = Label(master=janela,text=jogador + " vez", font=('consolas', 40))
rotulo = customtkinter.CTkLabel(
    master=janela, text=jogador + " vez", font=('consolas', 40))
rotulo.pack(side='top')

# botao_reiniciar = Button(master=janela,text='Reiniciar', font=('consolas', 20), command=novo_jogo)
botao_reiniciar = customtkinter.CTkButton(
    master=janela, text='Reiniciar', font=('consolas', 20), command=novo_jogo)
botao_reiniciar.pack(side='top', pady=10)

# frame = Frame(janela)
frame = customtkinter.CTkFrame(janela)
frame.pack()

for linha in range(3):
    for coluna in range(3):
        botoes[linha][coluna] = Button(frame, text="", font=('consolas', 40), width=5, height=2, bg="#275db3", bd=1, highlightbackground='#000000', activebackground='#1e4a8f',
                                       command=lambda linha=linha, coluna=coluna: proxima_jogada(linha, coluna),)
        botoes[linha][coluna].grid(row=linha, column=coluna)

janela.mainloop()
# Carlos Henrique
