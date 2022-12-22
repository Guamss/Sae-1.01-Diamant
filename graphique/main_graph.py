from tkinter import *
from fonctions_term import *

WIDTH = 1200
HEIGHT = 800

#Fênetre root
root = Tk()
root.title('Saé 1.01 - Diamant')
root.iconphoto(False, PhotoImage(file='img/icon.png'))
background = PhotoImage(file = "img/background.png")
root.resizable(0, 0)
root.geometry(f"{WIDTH}x{HEIGHT}")

def round_choice_mine_graph(window, canvas, players, leavers, player, score):
        print("mine")
        canvas.create_text(WIDTH//2, HEIGHT//3+100, text =f"J{player} : Vous allez à la mine", font=('Helvetica','15','bold'), fill="black")
        return players, leavers

def round_choice_camp_graph(window, canvas, players, leavers, player, score):
    print("camp")
    leavers.append(player)
    canvas.create_text(WIDTH//2, HEIGHT//3+100, text =f"J{player} : Vous retournez au camp", font=('Helvetica','15','bold'), fill="black")
    return players, leavers


def send_round_choice_graph(players, score, canvas, window, player = 0, leavers = []):
    pause_var = False
    window.bind("<F1>", lambda e: [round_choice_mine_graph(window, canvas, players, leavers, player, score)])
    window.bind("<F2>", lambda e: [round_choice_camp_graph(window, canvas, players, leavers, player, score)])

def start_game(nbr_p):
    newWindow = Toplevel(root)
    newWindow.resizable(0, 0)
    draw_menu = Canvas(newWindow, width = WIDTH, height = HEIGHT)
    draw_menu.pack(fill = "both", expand = True)
    
    nbr_round = 1 #Nombre de round 
    score = {} #Score global des joueurs
    score_round = {} #Score des joueurs par round

    for player in range(1, nbr_p+1):
        score_round[player] = 0
        score[player] = 0
        players = []
    for player in range(1, nbr_p+1):
        players.append(player)
        score[player]+=score_round[player]
        if nbr_round > 1:
            print(f"J{player} : a {score[player]} rubis dans son coffre, il a rapporté {score_round[player]} rubis pendant ce round-ci")
    score_round[player] = 0
    #On défini la pioche
    draw = [1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17,
            "spider", "spider", "spider",
            "creeper", "creeper", "creeper",
            "lava", "lava", "lava",
            "enderman", "enderman", "enderman",
            "relic"]
    #Les cartes actuellement sur le terrain (le round n'a pas commencé alors elle est vide)
    on_field_card = []
    finish = False
    #rubis_img = PhotoImage(file = "img/rubis.png")
    print(f"Un nouveau round commence : {nbr_round}")
    #while not finish:
    illustation_img = Canvas(newWindow, width = WIDTH, height = HEIGHT)
    illustation_img.pack()
    draw, on_field_card = card_draw(draw, on_field_card)
    last_index = on_field_card[len(on_field_card)-1]
    draw_menu.create_text(WIDTH//2, HEIGHT//10, text =f"{last_index} a été tiré", font=('Helvetica','15','bold'), fill="black")
    if type(last_index) == int:
        rubis_img = PhotoImage(file = "img/rubis.png")  
        illustation_img.place(x=0, y=0, height = 140, width = 161)
        illustation_img.create_image(0, 0, image=rubis_img, anchor=NW)
        score_round, on_field_card = rubis_add(players, score_round, on_field_card)
    elif last_index == "enderman":
        illustation_img.place(x=0, y=0, height = 103, width = 39)
        enderman = PhotoImage(file = "img/enderman.png")
        illustation_img.create_image(0, 0, image=enderman, anchor=NW)
    elif last_index == "creeper":
        illustation_img.place(x=0, y=0, height = 163, width = 104)
        creeper = PhotoImage(file = "img/creeper.png")
        illustation_img.create_image(0, 0, image=creeper, anchor=NW)
    elif last_index == "spider":
        illustation_img.place(x=0, y=0, height = 100, width = 103)
        spider = PhotoImage(file = "img/spider.png")
        illustation_img.create_image(0, 0, image=spider, anchor=NW)
    elif last_index == "lava":
        illustation_img.place(x=0, y=0, height = 100, width = 100)
        lava = PhotoImage(file = "img/lava.png")
        illustation_img.create_image(0, 0, image=lava, anchor=NW)
    elif last_index == "relic":
        illustation_img.place(x=0, y=0, height = 100, width = 99)
        relic = PhotoImage(file = "img/relic.png")
        illustation_img.create_image(0, 0, image=relic, anchor=NW)
    draw_menu.create_text(WIDTH//2, HEIGHT//5, text =f"Il y a {on_field_card} sur le terrain", font=('Helvetica','15','bold'), fill="black")
    if trap_in_draw(on_field_card):
        draw_menu.destroy()
        draw_menu = Canvas(newWindow, width = WIDTH, height = HEIGHT)
        draw_menu.pack(fill = "both", expand = True)
        for player in players:
            draw_menu.create_text(WIDTH//2, HEIGHT-200+50*player, text =f"J{player} a perdu {score_round[player]} !", font=('Helvetica','15','bold'), fill="black")
        score_round = reset_player_score(players, score_round)
        nbr_round+=1
        finish = True
    else:
            players, leavers = send_round_choice_graph(players, score_round, draw_menu, newWindow)
            draw_menu.create_text(WIDTH//2, HEIGHT//3+30*player, text =f"J{player} a récupéré {score[player]} rubis pendant le round", font=('Helvetica','15','bold'), fill="black")

def start_menu():
    choice = Canvas(root, width = WIDTH, height = HEIGHT)
    choice.create_text(WIDTH//2, 100, text ="Combien de joueurs", font=('Helvetica','30','bold'), fill="black")
    choice.pack(fill = "both", expand = True)
    
    trois = Button(root, text="3 joueurs",
        command=lambda: [start_game(3), choice.destroy()])
    quatre = Button(root, text="4 joueurs",
        command=lambda : [start_game(4), choice.destroy()])
    cinq = Button(root, text="5 joueurs",
        command=lambda : [start_game(5), choice.destroy()])
    six = Button(root, text="6 joueurs",
        command= lambda : [start_game(6), choice.destroy()])
    sept = Button(root, text="7 joueurs",
        command=lambda : [start_game(7), choice.destroy()])
    huit = Button(root, text="8 joueurs",
        command=lambda : [start_game(8), choice.destroy()])

    choice.create_window(WIDTH//2, 160, anchor="nw", window=trois)
    choice.create_window(WIDTH//2, 220, anchor="nw", window=quatre)
    choice.create_window(WIDTH//2, 280, anchor="nw", window=cinq)
    choice.create_window(WIDTH//2, 340, anchor="nw", window=six)
    choice.create_window(WIDTH//2, 400, anchor="nw", window=sept)
    choice.create_window(WIDTH//2, 460, anchor="nw", window=huit)


#Première fenêtre
canvas = Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack(fill = "both", expand = True)
canvas.create_image(0, 0, image = background, anchor = "nw")
button1 = Button(root, text = "Start game", 
        font=('Helvetica','15','bold'), 
        width=10,
        fg="white",
        bg="black",
        command=lambda: [canvas.destroy(),start_menu()])
button2 = Button(root, text = "Exit",
        font=('Helvetica','15','bold'),
        width=10, 
        fg="white", 
        bg="black", 
        command=root.destroy)

canvas.create_text(WIDTH//2, 100, text ="SAE 1.01 - DIAMANT", font=('Helvetica','30','bold'), fill="white")
canvas.create_window(WIDTH//2-70, 170, anchor = "nw", window = button1)
canvas.create_window(WIDTH//2-70, 230,anchor = "nw", window = button2)

root.mainloop()