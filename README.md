# SAE 1.01 - Diamant
***
## Comment lancer le jeu ?

### En terminal

Pour jouer sur un terminal, il suffit de lancer ***main_term.py*** dans le dossier *terminal* ou d'utiliser la commande : 
- ```python3 main_term.py```

Une fois le jeu lancé, les informations essentielles sont données aux joueurs. <br>

#### Spécificité pour comprendre le jeu :
1. Quand une carte rubis est tirée, elle est divisée équitablement entre tous les joueurs
et le reste est dans la liste des cartes sur le terrain. <br>
 Exemple à 3 joueurs :
- 15 a été tirée
- Il y a [0] sur le terrain

2. Le jeu a été modifié et le theme est sur le jeu Minecraft.
C'est à dire que la liste des cartes modifiées sont :
- piège : [ spider , creeper , lava , enderman ]

### Avec interface graphique

Pour jouer avec une interface graphique, il suffit de télécharger tkinter puis de lancer ***main_graph.py*** dans le dossier *graphique* ou d'utiliser la commande :
- *Pour installer tkinter :* ```pip3 install tk```
- *Pour lancer le jeu :* ```python3 main_graph.py```

**Remarque : Le jeu n'est jouable qu'entre 3 et 8 personnes (inclus).**

## Le travail accompli

### Le terminal

Lors de cette Saé nous avons réalisé le jeu Diamant jouable sur terminal incluant
les reliques, un jeu en 5 manches ainsi qu'un classement en fin de partie.

### L'interface graphique

Nous avons fait une interface graphique basique permettant d'effectuer des choix,
mais aussi avec quelques illustrations simples, le jeu ne fonctionne pas dans son intégralité
(choix mine/camp qui bug).

## Les problèmes rencontrés / bugs

### Les reliques

L'intégration de la mécanique des reliques dans le jeu a créé beaucoup de bugs
dans le jeu qui ont été depuis réglé, mais cette fonction a été l'une des tâches
les plus difficiles à debuger.

### Ajout des rubis et répartition

Une erreur de condition quand on a 0 joueur sur le terrain et qu'on doit
répartir les diamants donc on divise par 0 et on a une erreur. Ce problème
a été corrigé assez rapidement.

### Choix Camp/Mine

Quand les joueurs quittent la mine pour revenir au camp, on enlève les joueurs
concernés de la liste joueurs et on les ajoute à la liste leavers, ceci a eu
pour effet des erreurs de list index out of range ce qui a aussi été corrigé.

### Le choix camp/mine par l'interface graphique

Le programme ne s'arrête pas et le joueur n'a pas le temps de dire son choix via la touche F1 ou F2
car la boucle continue (pas de fonction input pour stopper le programme) et malgrés tout ce qu'on a fait le problème n'a
pas été réglé par manque de temps.

## Idée originale

Nous avions pour idée de réaliser le jeu Diamant tout s'inspirant du jeu Minecraft