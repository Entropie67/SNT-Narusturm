###########################################
#              SNT M. Elophe              #
###########################################

# Ici on va importer les modules que nous allons utiliser.
import pygame
from pygame.locals import *


# Ouverture de la fenêtre Pygame
TAILLE_FENETRE = (640, 480)
fenetre = pygame.display.set_mode(TAILLE_FENETRE)



# Boucle de jeu
continuer = 1
while continuer:
	continuer = int(input())