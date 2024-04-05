import pygame
import sys

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

# Loop principal
while pygame.mixer.music.get_busy():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

    pygame.time.Clock().tick(10)  # Limita a taxa de atualização do loop

