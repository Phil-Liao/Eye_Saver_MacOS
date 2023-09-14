import pygame
import time
import json

import Utils
pygame.init()
pygame.font.init()

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


control_box = Utils.box(WIN, setup_info["WIDTH"], setup_info["HEIGHT"], setup_info["CONTROL_BOX_X"], setup_info["CONTROL_BOX_Y"], setup_info["CONTROL_BOX_WIDTH"], setup_info["CONTROL_BOX_HEIGHT"], True, None, 
                        True, setup_info["CONTROL_BOX_BORDER_WIDTH"], setup_info["CONTROL_BOX_BORDER_RADIUS"], Utils.COLORS[setup_info["CONTROL_BOX_BORDER_COLOR"]], True)
control_box.is_button(Utils.COLORS[setup_info["ACTIVE_COLOR"]])
control_box_font = set_font()
control_box_text = setup_info["CONTROL_BOX_STARTUP_TEXT"]




input_box = Utils.box(WIN, setup_info["WIDTH"], setup_info["HEIGHT"], setup_info["INPUT_BOX_X"], setup_info["INPUT_BOX_Y"], setup_info["INPUT_BOX_WIDTH"], setup_info["INPUT_BOX_HEIGHT"], False, Utils.COLORS[setup_info["PASSIVE_COLOR"]], True,
                      setup_info["INPUT_BOX_BORDER_WIDTH"], setup_info["INPUT_BOX_BORDER_RADIUS"], -1, True)
input_box.is_button(Utils.COLORS[setup_info["ACTIVE_COLOR"]], True)
input_box_font = set_font()
input_box_text = setup_info["INPUT_BOX_STARTUP_TEXT"]



main_text = setup_info["BG_STARTUP_TEXT"]




def start_countdown(main_text, countdown_time):
    start = time.time()
    return start





started = False
input_box_click = False
user_input_text = ""
while True:
    control_box_click = False

    pygame.time.Clock().tick(setup_info["FPS"])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            control_box_click = control_box.clicked(mouse_pos, control_box_click)
            input_box_click = input_box.clicked(mouse_pos, input_box_click)
        if (event.type == pygame.KEYDOWN) and input_box_click:
            if event.key == pygame.K_RETURN:
                
                
                started = True
                input_box_click = not(input_box_click)
                countdown_time = float(user_input_text)
                start_time = start_countdown(main_text, countdown_time)
                user_input_text = ""
            
            
            
            
            elif event.key == pygame.K_BACKSPACE:
                user_input_text = user_input_text[:-1]
            elif event.unicode.isdigit():
                user_input_text += event.unicode
            elif event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
                user_input_text += event.unicode
            
    if control_box_click and input_box_click:
        
        
        started = True
        input_box_click = False
        countdown_time = float(user_input_text)
        start_time = start_countdown(main_text, countdown_time)
        user_input_text = ""
    
    
    
    elif input_box_click and input_box_text == setup_info["INPUT_BOX_STARTUP_TEXT"]:
        input_box_text = ""
    elif input_box_click:
        input_box_text = user_input_text


    if started:
        if (time.time() - start_time) >= countdown_time*60:
            main_text = setup_info["BG_TIME_UP_TEXT"]
        if (time.time() - start_time) < countdown_time*60:
            main_text = str(round((countdown_time*60 - time.time() + start_time)/60, 2))
    bg_font = set_font(setup_info["BG_TEXT_TYPE"], setup_info["BG_TEXT_SIZE"])


    draw_background(WIN, Utils.colors.COLORS[setup_info["BG_COLOR"]], setup_info["WIDTH"], setup_info["HEIGHT"], bg_font, main_text, Utils.COLORS[setup_info["TEXT_PASSIVE_COLOR"]])
    
    control_box.draw_box(control_box_click)
    input_box.draw_box(input_box_click)

    control_box.draw_text(control_box_text, control_box_font, Utils.COLORS[setup_info["TEXT_PASSIVE_COLOR"]], Utils.COLORS[setup_info["TEXT_ACTIVE_COLOR"]],
                          setup_info["CONTROL_BOX_TEXT_X"], setup_info["CONTROL_BOX_TEXT_Y"], control_box_click)
    input_box.draw_text(input_box_text, input_box_font, Utils.COLORS[setup_info["TEXT_PASSIVE_COLOR"]], Utils.COLORS[setup_info["TEXT_ACTIVE_COLOR"]],
                        setup_info["INPUT_BOX_TEXT_X"], setup_info["INPUT_BOX_TEXT_Y"], input_box_click)
    
    pygame.display.update()