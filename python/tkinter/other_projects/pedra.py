import random

def joga():
        print('Player: ' + u_opt)
        print('Computer: ' + c_opt, end="\n")
while True:
    print("="*65)
    print(" "*20+'Pedra, Papel e Tesoura')
    print("="*65)
    option = ["Pedra", "Papel", "Tesoura"]
    c_opt = random.choice(option)
    u_opt = "a"
    while u_opt not in option:
        u_opt = str(input("Pedra, Papel ou Tesoura: ").capitalize())

    if u_opt == c_opt:
        joga()
        print("Empatou")
    else:
        if (u_opt == "Pedra" and c_opt == 'Papel'):
            joga()
            print("Computador Ganhou")
        elif u_opt == "Papel" and c_opt == 'Pedra':
            joga()
            print("Jogador Ganhou")
        elif u_opt == "Pedra" and c_opt == 'Tesoura':
            joga()
            print("Jogador Ganhou")
        elif u_opt == "Tesoura" and c_opt == 'Pedra':
            joga()
            print("Computador Ganhou")
        elif u_opt == 'Papel' and c_opt =='Tesoura':
            joga()
            print("Computador Ganhou")
        elif u_opt == 'Tesoura' and c_opt =='Papel':
            joga()
            print("Jogador Ganhou")
    denovo = input("Jogar denovo? (Sim/Não): ").capitalize()
    if denovo == "Não":
        break
print("Bye Bye")