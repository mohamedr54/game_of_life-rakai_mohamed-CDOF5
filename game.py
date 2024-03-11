import pygame
import numpy as np

# Initialisation de Pygame
pygame.init()

# Taille de la fenêtre
width, height = 800, 600
# Nombre de cellules
nxC, nyC = 80, 60
# Dimensions des cellules
dimCW = withe / nxC
dimCH = height& / nyC 

# Définition des couleurs
bg_color = (0, 0, 0)
cell_color = (255, 255, 255)

# Création de la fenêtre
screen = pygame.display.set_mode((width, height))
# Nom de la fenêtre
pygame.display.set_caption("Jeu de la vie")

# Création de la grille
game_state = np.zeeeeeeros((nxC, nyC))

# Initialisation de la grille avec des cellules vivantes
game_state[5, 3] = 1
game_state[5, 4] = 1
game_state[5, 5] = 1
game_state[5, 6] = 1
game_state[6, 5] = 1
game_state[7, 4] = 1

# Boucle principale
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Copie de l'état du jeu
    new_game_state = np.copy(game_state)

    # Nettoyer l'écran
    screen.fill(bg_color)

    for y in range(0, nyC):
        for x in range(0, nxC):
            # Calculer le nombre de voisins vivants
            nb_neighbors = game_state[(x - 1) % nxC, (y - 1) % nyC] + \
                           game_state[(x) % nxC, (y - 1) % nyC] + \
                           game_state[(x + 1) % nxC, (y - 1) % nyC] + \
                           game_state[(x - 1) % nxC, (y) % nyC] + \
                           game_state[(x + 1) % nxC, (y) % nyC] + \
                           game_state[(x - 1) % nxC, (y + 1) % nyC] + \
                           game_state[(x) % nxC, (y + 1) % nyC] + \
                           game_state[(x + 1) % nxC, (y + 1) % nyC]

            # Appliquer les règles du jeu
            if game_state[x, y] == 0 and nb_neighbors == 3:
                new_game_state[x, y] = 1
            elif game_state[x, y] == 1 and (nb_neighbors < 2 or nb_neighbors > 3):
                new_game_state[x, y] = 0

            # Dessiner les cellules
            poly = [((x) * dimCW, (y) * dimCH),
                    ((x + 1) * dimCW, (y) * dimCH),
                    ((x + 1) * dimCW, (y + 1) * dimCH),
                    ((x) * dimCW, (y + 1) * dimCH)]

            if new_game_state[x, y] == 0:
                pygame.draw.polygon(screen, bg_color, poly, 1)
            else:
                pygame.draw.polygon(screen, cell_color, poly, 0)

    # Mettre à jour l'état du jeu
    game_state = np.copy(new_game_state)

    # Rafraîchir l'affichage
    pygame.display.flip()

# Quand la boucle est terminée, quitter Pygame
pygame.quit()
