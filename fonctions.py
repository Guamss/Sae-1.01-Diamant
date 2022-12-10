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
	temp = [] #Une copie de la liste players
	decal = 1
	for i in range(len(players)):
		temp.append(players[i])
	for player in temp:
		print(f"J{player} a récupéré {score[player]} rubis pendant le round")
		reponses = input(f" J{player} : Aller au campement ou à la mine ? (mine/camp)")
		if reponses == "mine":
			print("Vous allez à la mine")
		elif reponses == "camp":
			players.pop(player-decal)
			decal+=1
			print("Vous retournez au campement")
		else:
			mauvaise_reponse = True
			while mauvaise_reponse:
				reponses = input("Répondez correctement (mine/camp)")
				if reponses == "mine":
					mauvaise_reponse = False
					print("Vous allez à la mine")
				elif reponses == "camp":
					mauvaise_reponse = False
					players.pop(player-decal)
					decal+=1
					print("Vous retournez au camp")
	return players

def card_draw(draw, on_field_card):
	"""
	Permet de tirer une carte au hasard

	Params:
		draw (list) : La pioche du jeu
		on__field_card (list) : Liste des cartes qui ont été tirées pendant le round
	
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
	
	"""
	rubis = on_field_card[len(on_field_card)-1]
	on_field_card.pop(len(on_field_card)-1)
	rubis_div = rubis//len(players)
	for player in players:
		score[player]+=rubis_div
	rest = rubis%len(players)
	on_field_card.append(rest)
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

def reset__player_score(players, score):
	"""
	Reset le score d'un joueur qui a perdu (contre deux pièges)
	"""
	for player in players:
		score[player] = 0
	return score

def on_leave(players, on_field_card, score):
	#globalement juste à récupérer les rubis et les relics et faire un écran de victoire et c'est fini après c'est interface graphique
	pass

def verify_end_game(nbr_round, winner, nbr_rubis):
	"""
	Vérifie l'état de la partie (si elle est terminée ou non)

	Params :
		nbr_round (int) : le nombre de round qui a été effectué
		winner (int) : le joueur qui a gagné la partie (J0, J1 etc...)
		nbr_rubis (int) : le nombre de rubis du joueur gagnant

	Return :
		True, False (boolean)
	"""
	if nbr_round == 5:
		print(f"J{winner} a gagné avec {nbr_rubis}")
		return True
	else:
		return False