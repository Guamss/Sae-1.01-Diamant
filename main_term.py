from fonctions_term import *

nbr_round = 1 #Nombre de round 
score = {} #Score global des joueurs
score_round = {} #Score des joueurs par round

nbr_p = int(input("Combien de joueurs ?"))
if nbr_p > 8 or nbr_p < 3:
        print("il n'y a pas le bon nombre de joueurs (entre 3 et 8) de joueurs")
else:
        print(f"Le jeu va s'éxecuter à {nbr_p} joueurs")
        #Définition des scores aux joueurs sous la forme {Joueur : Score}
        for player in range(1, nbr_p+1):
                score_round[player] = 0
                score[player] = 0
        #Début du jeu en 5 round
        while nbr_round != 6:
                #On attribue un joueur par élément de la liste players et on ajoute le score accumulé pendant le round au score global
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
                print(f"Un nouveau round commence : {nbr_round}")
                #Tant que le round n'est pas fini
                while not finish:
                        #On tire une carte de la pioche pour la mettre sur le terrain
                        draw, on_field_card = card_draw(draw, on_field_card)
                        last_index = on_field_card[len(on_field_card)-1]
                        #Si une carte rubis est tirée on attribue les rubis équitablement et on laisse le reste dans sur le terrain
                        if type(last_index) == int:
                                score_round, on_field_card = rubis_add(players, score_round, on_field_card)
                        print(f"Il y a {on_field_card} sur le terrain")
                        #Si il y a 2 pièges de même type sur le terrain alors tous les joueurs qui ne sont pas au camp perdent tous leurs rubis et on recommence un round
                        if trap_in_draw(on_field_card):
                                for player in players:
                                        print(f"J{player} a perdu {score_round[player]} !")
                                score_round = reset_player_score(players, score_round)
                                nbr_round+=1
                                finish = True             
                        else:
                                players, leavers = round_choice(players, score_round)
                                #Sinon on vérifie si un joueur est revenu au camp
                                if len(leavers) > 0:
                                        #Si oui on réparti les rubis restant équitablement aux nombre de joueurs qui sont revenus au campement
                                        score_round, rest, on_field_card = on_leave(leavers, on_field_card, score_round) 
                                        if "relic" in on_field_card:
                                                #Si il y a une relique sur le terrain on appelle relic_add
                                            score_round, on_field_card = relic_add(leavers, score_round, on_field_card)
                                #Si tous les joueurs sont revenu au camp on recommence une manche
                                elif len(players) == 0:
                                        nbr_round += 1
                                        finish = True
        #Une fois la partie fini on ajoute les scores du dernier round au score global
        for player in range(1, nbr_p+1):
            players.append(player)
            score[player]+=score_round[player]
            print(f"J{player} : a {score[player]} rubis dans son coffre, il a rapporté {score_round[player]} rubis pendant ce round-ci")
        #On détermine le gagnant de la partie avec un classement
        winners = end_game(players, score)
        if len(winners) > 0:
            print("La partie est terminée")
            for classement in range(len(winners)):
                print(f"J{winners[classement]} est {classement+1} avec un score de {score[winners[classement]]}")
