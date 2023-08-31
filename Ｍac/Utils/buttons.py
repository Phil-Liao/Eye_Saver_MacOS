import pygame
class button:
    def __init__(self, WIN, x, y, width, height, color) -> None:
        self.WIN = WIN
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    def draw_button(self):
        pygame.draw.rect(self.WIN, self.color, (self.x, self.y, self.width, self.height))