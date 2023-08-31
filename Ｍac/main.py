import pygame
import time
import Utils
pygame.init()

with open("/Users/philliao/Documents/Eye-Saver/Ｍac/setup.txt", "r") as file:
    setup_info = file.readlines()
    setup_info[0] = int(setup_info[0])
    setup_info[1] = int(setup_info[1])


WIDTH, HEIGHT = setup_info[0], setup_info[1]
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(setup_info[2])




def draw_background(WIN):
    pygame.draw.rect(WIN, Utils.colors.COLORS[setup_info[3]], (0, 0, WIDTH, HEIGHT))


#control_button = Utils.button(WIN, (WIDTH*0.025), (HEIGHT*0.66), (WIDTH*0.45), "", )




FPS = 60
while True:
    pygame.time.Clock().tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    draw_background(WIN)
    pygame.display.update()
