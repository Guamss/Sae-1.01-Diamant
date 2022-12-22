import random as rd

def round_choice(players, score):
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
        print(f"J{player} a récupéré {score[player]} rubis pendant le round")
        bad_answer = False
        broken = False
        while (not broken):
            reponses = input((f" J{player} : Aller au campement ou à la mine ? (mine/camp)","Répondez correctement (mine/camp)")[bad_answer])
            if reponses == "mine":
                print("Vous allez à la mine")
                broken = True
            elif reponses == "camp":
                leavers.append(player)
                broken = True
                print("Vous retournez au camp")
            else:
                bad_answer = True
    for player in leavers:
        players.remove(player)
    return players, leavers

def card_draw(draw, on_field_card):
	"""
	Permet de tirer une carte au hasard

	Params:
		draw (list) : La pioche du jeu
		on_field_card (list) : Liste des cartes qui ont été tirées pendant le round
	
	Return:
		draw, on_field_card (tuple) : La pioche du jeu et les éléments qui lui ont été retirés
	"""
	draw_pick = rd.randint(0, len(draw)-1)
	on_field_card.append(draw[draw_pick])
	print(draw[draw_pick], "a été tirée ")
	draw.pop(draw_pick)
	return draw, on_field_card
	
def rubis_add(players, score, on_field_card):
    """
    Ajoute les rubis aux joueurs quand une carte rubis est tirée

    Params:
        players (list) : Liste des joueurs qui restent à la mine
        score (dict) : Dictionnaire qui indique les scores des joueurs
        on_field_card (list): Liste des cartes qui ont été tirées pendant le round
    Return:
       score, on_field_card (tuple) : Dictionnaire qui indique les scores des joueurs et les cartes sur le terrain
    """
    #Si il n'y a pas 0 joueurs
    if len(players) != 0:
        rubis = on_field_card[len(on_field_card)-1]
        on_field_card.pop(len(on_field_card)-1)
        #on divise le nombre de rubis par le nombre de joueurs
        rubis_div = rubis//len(players)
        for player in players:
            score[player]+=rubis_div
        rest = rubis%len(players)
        on_field_card.append(rest)
    return score, on_field_card

def relic_add(leavers, score, on_field_card):
    """
    Vérifie le nombre de leavers et ajoute 5 rubis à un au joueur qui a récupéré la relique si les conditions sont remplis
    Param:
        leavers (list) : Liste des joueurs étant revenu au campement
        score (dict) : Dictionnaire qui indique les scores des joueurs
        on_field_card (list): Liste des cartes qui ont été tirées pendant le round

    Return:
        score, on_field_card (tuple) : score et on_field_card
    """
    #relic est l'indice de la relique dans les cartes sur le terrain 
    for search in range(len(on_field_card)):
        if on_field_card[search] == "relic":
            relic = search
    if len(leavers) == 1:
        #Si il n'y a qu'une seule personne qui rentre au camp alors on lui donne la relique qui vaut 5 rubis
        score[leavers[0]] += 5
        print(f"J{leavers[0]} a récupéré la relique et a récupéré 5 rubis")
    else:
        #Sinon cela veut dire que plus de deux joueurs sont parti et alors la relique est détruite
        print("La relique a été détruite, trop de joueurs sont partit")
    on_field_card.pop(relic)       
    return score, on_field_card

def trap_in_draw(on_field_card):
	"""
	Vérifie si il y a deux pièges de même type dans on_field_card
	Param:
		on_field_card (list): Liste des cartes qui ont été tirées pendant le round
	
	Return:
		True, False (boolean)
	"""
	for a in range(len(on_field_card)):
		if type(on_field_card[a]) == str and on_field_card[a] != "relic":
			for i in range(len(on_field_card)):
				if on_field_card[a] == on_field_card[i] and a!=i:
					print("Il y a deux pièges")
					return True
	return False

def reset_player_score(players, score):
	"""
	Reset le score d'un joueur qui a perdu (contre deux pièges)
    Param:
        players (list) : Liste des joueurs qui restent à la mine 
        score (dict) : Dictionnaire qui indique les scores des joueurs

    Return:
        score (dict) : Dictionnaire qui indique les scores des joueurs 
    """
	for player in players:
		score[player] = 0
	return score

def on_leave(leavers, on_field_card, score):
    """
    Quand un ou plusieur joueurs revient au campement les rubis sont répartis equitablement
    Params:
        leavers (list) : Liste des joueurs étant revenu au campement
        on_field_card (list) : Liste des cartes qui ont été tirées pendant le round 
        score (dict) : Dictionnaire qui indique les scores des joueurs
    
    Return: 
        score, rest, on_field_card (tuple) : Le score, les cartes sur le terrain et les joueurs étant revenu au campement
    """
    nbr_rubis = 0
    for card in range(len(on_field_card)):
        if type(on_field_card[card]) == int:
            nbr_rubis += on_field_card[card]
            on_field_card[card] = 0
        rubis_div = nbr_rubis//len(leavers)
    for leaver in leavers:
        score[leaver] += rubis_div
        rest = nbr_rubis%len(leavers)
    return score, rest, on_field_card

def end_game(players, score):
	"""
	Vérifie l'état de la partie (si elle est terminée ou non)

	Params :
		players (list) : Liste des joueurs qui restent à la mine
		score (dict) : Dictionnaire qui indique les scores des joueurs 

	Return :
		winners (list) : Classement des joueurs selon leurs score
	"""
	winners = []
	for player in players:
		winners.append(player)
	for winner in range(len(winners)):
		for compare in range(len(winners)):
			if score[winners[winner]] > score[winners[compare]]:
				winners[winner], winners[compare] = winners[compare], winners[winner]
	return winners
