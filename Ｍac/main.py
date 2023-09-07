import pygame
import time
import json

import Utils
pygame.init()

with open("/Users/philliao/Documents/Eye-Saver/Ｍac/setup.json") as file:
    setup_info = json.load(file)

WIN = pygame.display.set_mode((setup_info["WIDTH"], setup_info["HEIGHT"]))
pygame.display.set_caption(setup_info["SCREEN_CAPTION"])

def set_font(font_type:str="Segoe-UI", font_size:int=24):
    font = pygame.font.SysFont(font_type, font_size)
    return font




def draw_background(WIN, BG_COLOR, WIDTH, HEIGHT, font=None, text=None, text_color=None, text_x='', text_y=''):
    pygame.draw.rect(WIN, BG_COLOR, (0, 0, WIDTH, HEIGHT))
    if not(isinstance(text, str)):
        raise Exception(f"TypeError: expected str instance")
    text = font.render(text, True, text_color)
    text_rect = text.get_rect()
    if (text_x=='' and text_y==''):
        text_rect.center = (WIDTH/2, HEIGHT/2)
    else:
        text_rect.center = (text_x,text_y)
    WIN.blit(text, text_rect)

passive_color = Utils.COLORS[setup_info["PASSIVE_COLOR"]]
active_color = Utils.COLORS[setup_info["ACTIVE_COLOR"]]

control_box = Utils.box(WIN, setup_info["WIDTH"], setup_info["HEIGHT"], setup_info["CONTROL_BOX_X"], setup_info["CONTROL_BOX_Y"], setup_info["CONTROL_BOX_WIDTH"], setup_info["CONTROL_BOX_HEIGHT"], passive_color, True)
input_box = Utils.box(WIN, setup_info["WIDTH"], setup_info["HEIGHT"], setup_info["INPUT_BOX_X"], setup_info["INPUT_BOX_Y"], setup_info["INPUT_BOX_WIDTH"], setup_info["INPUT_BOX_HEIGHT"], passive_color)



while True:
    pygame.time.Clock().tick(setup_info["FPS"])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            





    bg_font = set_font(setup_info["BG_TEXT_TYPE"], setup_info["BG_TEXT_SIZE"])
    
    main_text = setup_info["BG_STARTUP_TEXT"]
    draw_background(WIN, Utils.colors.COLORS[setup_info["BG_COLOR"]], setup_info["WIDTH"], setup_info["HEIGHT"], bg_font, main_text, Utils.COLORS[setup_info["TEXT_COLOR"]])
    
    control_box.draw_box(False)
    input_box.draw_box(False)
    pygame.display.update()