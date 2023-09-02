import pygame
class box:
    def __init__(self, WIN, WIN_WIDTH, WIN_HEIGHT, x, y, width, height, passive_color, active_color=None, is_button=False, is_displaying_text=False):
        self.WIN = WIN
        self.WIN_WIDTH = WIN_WIDTH
        self.WIN_HEIGHT = WIN_HEIGHT
        self.x = WIN_WIDTH*x
        self.y = WIN_HEIGHT*y
        self.width = WIN_WIDTH*width
        self.height = WIN_HEIGHT*height
        self.passive_color = passive_color
        self.active_color = active_color
        self.is_button = is_button
        self.is_displaying_text = is_displaying_text
    def is_display_text(self, font, text, text_color, text_x, text_y):
        self.is_displaying_text = True
        if not(isinstance(text, str)):
            raise Exception(f"TypeError: expected str instance")
        self.text = font.render(text, True, text_color)
        self.text_rect = text.get_rect()
        self.text_rect.center = (text_x, text_y)
    def draw_text(self):
        self.WIN.blit(self.text, self.text_rect)
    def draw_box(self, click=False):
        if click and self.is_button:
            pygame.draw.rect(self.WIN, self.active_color, (self.x, self.y, self.width, self.height))
        elif click and (self.is_button == False):
            raise Exception("Error: class object not button")
        else:
            pygame.draw.rect(self.WIN, self.passive_color, (self.x, self.y, self.width, self.height))
        if self.is_displaying_text:
            draw_text()