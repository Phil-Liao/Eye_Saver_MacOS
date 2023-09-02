import pygame
class box:
    def __init__(self, WIN, WIN_WIDTH, WIN_HEIGHT, x, y, width, height, passive_color, active_color=None, button=False):
        self.WIN = WIN
        self.WIN_WIDTH = WIN_WIDTH
        self.WIN_HEIGHT = WIN_HEIGHT
        self.x = WIN_WIDTH*x
        self.y = WIN_HEIGHT*y
        self.width = WIN_WIDTH*width
        self.height = WIN_HEIGHT*height
        self.passive_color = passive_color
        self.active_color = active_color
        self.button = button
    def draw_box(self, click=False):
        if click and self.button:
            pygame.draw.rect(self.WIN, self.active_color, (self.x, self.y, self.width, self.height))
        elif click and (self.button == False):
            raise Exception("Error, class object not button")
        else:
            pygame.draw.rect(self.WIN, self.passive_color, (self.x, self.y, self.width, self.height))
    