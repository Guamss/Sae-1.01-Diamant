from fonctions import *

nbr_round = 1
score = {}
score_round = {}

nbr_p = int(input("Combien de joueurs ?"))
if nbr_p > 8 or nbr_p < 3:
        print("il n'y a pas le bon nombre de joueurs (entre 3 et 8) de joueurs")
else:
        print(f"Le jeu va s'éxecuter à {nbr_p} joueurs")
        for player in range(1, nbr_p+1):
                score_round[player] = 0
                score[player] = 0
        while nbr_round != 5:
                players = []
                for player in range(1, nbr_p+1):
                        players.append(player)
                        score[player]+=score_round[player]
                        if nbr_round > 1:
                                print(f"J:{player} a {score[player]} rubis dans son coffre, il a rapporté {score_round[player]} rubis pendant ce round-ci")
                        score_round[player] = 0
                draw = [1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17,
                        "spider", "spider", "spider",
                        "snake", "snake", "snake",
                        "lava", "lava", "lava",
                        "belier", "belier", "belier",
                        "relic", "relic", "relic", "relic", "relic"]
                on_field_card = []
                finish = False
                print(f"Un nouveau round commence : {nbr_round}")
                while not finish:
                        draw, on_field_card = card_draw(draw, on_field_card)
                        last_index = on_field_card[len(on_field_card)-1]
                        if type(last_index) == int:
                                score_round, on_field_card = rubis_add(players, score_round, on_field_card)
                        print(f"Il y a {on_field_card} sur le terrain")
                        if trap_in_draw(on_field_card):
                                for player in players:
                                        print(f"J{player} a perdu {score_round[player]} !")
                                score_round = reset__player_score(players, score_round)
                                nbr_round+=1
                                finish = True
                        else:
                                if len(round_choice(players, score_round)) == 0:
                                        nbr_round +=1
                                        finish = True