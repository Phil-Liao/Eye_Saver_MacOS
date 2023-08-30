import pygame
import time

pygame.init()

with open("/Users/philliao/Documents/Eye-Saver/Ｍac/setup.txt", "r") as file:
    setup_info = file.readlines()
    setup_info[0] = int(setup_info[0])
    setup_info[1] = int(setup_info[1])


WIDTH, HEIGHT = setup_info[0], setup_info[1]
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(setup_info[2])






FPS = 60
while True:
    pygame.time.Clock().tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        