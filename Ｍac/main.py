import pygame
import time
import json

import Utils
pygame.init()

with open("/Users/philliao/Documents/Eye-Saver/Ｍac/setup.json") as file:
    setup_info = json.load(file)

WIN = pygame.display.set_mode((setup_info["WIDTH"], setup_info["HEIGHT"]))
pygame.display.set_caption(setup_info["SCREEN_CAPTION"])




def draw_background(WIN, BG_COLOR, WIDTH, HEIGHT):
    pygame.draw.rect(WIN, BG_COLOR, (0, 0, WIDTH, HEIGHT))


passive_color = Utils.COLORS[setup_info["PASSIVE_COLOR"]]
active_color = Utils.COLORS[setup_info["ACTIVE_COLOR"]]

control_box = Utils.box(WIN, setup_info["WIDTH"], setup_info["HEIGHT"], setup_info["CONTROL_BOX_X"], setup_info["CONTROL_BOX_Y"], setup_info["CONTROL_BOX_WIDTH"], setup_info["CONTROL_BOX_HEIGHT"], passive_color, active_color, True)
input_box = Utils.box(WIN, setup_info["WIDTH"], setup_info["HEIGHT"], setup_info["INPUT_BOX_X"], setup_info["INPUT_BOX_Y"], setup_info["INPUT_BOX_WIDTH"], setup_info["INPUT_BOX_HEIGHT"], passive_color)



while True:
    pygame.time.Clock().tick(setup_info["FPS"])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    draw_background(WIN, Utils.colors.COLORS[setup_info["BG_COLOR"]], setup_info["WIDTH"], setup_info["HEIGHT"])
    control_box.draw_box(False)
    input_box.draw_box(False)
    pygame.display.update()
