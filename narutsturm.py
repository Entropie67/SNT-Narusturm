###########################################
#           SNT - M. Elophe - 2020        #
###########################################

# Ici on va importer les modules que nous allons utiliser.
# C'est comme le from robot import * de France IOI
import pygame
from pygame.locals import *

# Ouverture de la fenêtre Pygame
TAILLE_FENETRE = (640, 480)
fenetre = pygame.display.set_mode(TAILLE_FENETRE)
# On peut ajouter un titre à la fenêtre.
pygame.display.set_caption("Narusturm !")

# Couleur de fond au format RGB : (Rouge, Vert, Bleu)
# En l'occurence, ici, j'ai jeté mon dévolu sur un petit violet pâle pas trop agrgessif.
couleur = (92, 107, 192)
fenetre.fill(couleur)



# Il faut penser à rafraichir l'écran ! (Surtout en été)
pygame.display.flip()

# Boucle de jeu, "infinie", parce que le jeu doit continuer tant que je ne l'arrête pas
continuer = 1
while continuer:
	continuer = int(input())