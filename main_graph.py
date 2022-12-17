from tkinter import *
from fonctions_term import *


WIDTH = 1200
HEIGHT = 800

#Fênetre root
root = Tk()
root.title('Saé 1.01 - Diamant')
root.iconphoto(False, PhotoImage(file='img/icon.png'))
background = PhotoImage(file = "img/background.png")

def button_is_pressed(pressed):
    return not pressed

def round_choice_graph(players, score, canvas):
    """
    Laisse le choix aux joueurs d'aller à la mine ou au camp, si le joueurs va au camp alors celui-ci ne pourra plus jouer du round

    Params:
        players (list) : Liste des joueurs qui restent à la mine
        score (dict) : Dictionnaire qui indique les scores des joueurs
    
    Return:
        players (list) : Liste des joueurs qui restent à la mine
    """
    
    leavers = []
    for player in players:
        camp_pressed = False
        mine_pressed = False
        canvas.create_text(WIDTH//2, HEIGHT//3+30*player, text =f"J{player} a récupéré {score[player]} rubis pendant le round", font=('Helvetica','15','bold'), fill="black")
        camp = Button(root, text="camp",fg="white", bg="black", command=lambda: [button_is_pressed(camp_pressed)])
        mine = Button(root, text="mine",fg="white", bg="black",command=lambda: [button_is_pressed(mine_pressed)])
        canvas.create_text(WIDTH//2-90, HEIGHT//2+12, text =f"J{player}", font=('Helvetica','15','bold'), fill="black")
        canvas.create_window(WIDTH//2, HEIGHT//2, anchor="nw", window=camp)
        canvas.create_window(WIDTH//2-60, HEIGHT//2, anchor="nw", window=mine)
        while not (mine_pressed or camp_pressed):
            canvas.update()
            if mine_pressed:
                canvas.create_text(WIDTH//2, HEIGHT//3+100, text ="Vous allez à la mine", font=('Helvetica','15','bold'), fill="black")
            elif camp_pressed:
                leavers.append(player)
                canvas.create_text(WIDTH//2, HEIGHT//3+100, text =f"Vous retournez au camp", font=('Helvetica','15','bold'), fill="black")
        for player in leavers:
            players.remove(player)
    return players, leavers




root.geometry(f"{WIDTH}x{HEIGHT}")

def start_game(nbr_p):
    draw_menu = Canvas(root, width = WIDTH, height = HEIGHT)
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
    draw, on_field_card = card_draw(draw, on_field_card)
    last_index = on_field_card[len(on_field_card)-1]
    draw_menu.create_text(WIDTH//2, HEIGHT//10, text =f"{last_index} a été tiré", font=('Helvetica','15','bold'), fill="black")
    if type(last_index) == int:
        score_round, on_field_card = rubis_add(players, score_round, on_field_card)
        #draw_menu.create_image(WIDTH//10, 500, image=rubis_img, anchor="nw")
    draw_menu.create_text(WIDTH//2, HEIGHT//5, text =f"Il y a {on_field_card} sur le terrain", font=('Helvetica','15','bold'), fill="black")
    if trap_in_draw(on_field_card):
        draw_menu.destroy()
        draw_menu = Canvas(root, width = WIDTH, height = HEIGHT)
        draw_menu.pack(fill = "both", expand = True)
        for player in players:
            draw_menu.create_text(WIDTH//2, HEIGHT-200+50*player, text =f"J{player} a perdu {score_round[player]} !", font=('Helvetica','15','bold'), fill="black")
        score_round = reset_player_score(players, score_round)
        nbr_round+=1
        finish = True
    else:
        players, leavers = round_choice_graph(players, score_round, draw_menu)

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