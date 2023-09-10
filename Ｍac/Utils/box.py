import pygame
class box:
    def __init__(self, WIN, WIN_WIDTH, WIN_HEIGHT, x, y, width, height, transparent=False, passive_color=(), border=False, border_width=0, border_radius=0, border_color=None):
        self.WIN = WIN
        self.WIN_WIDTH = WIN_WIDTH
        self.WIN_HEIGHT = WIN_HEIGHT
        self.x = WIN_WIDTH*x
        self.y = WIN_HEIGHT*y
        self.width = WIN_WIDTH*width
        self.height = WIN_HEIGHT*height
        self.transparent = transparent
        if not(self.transparent):
            self.passive_color = passive_color
        self.button = False
        self.display_text = False
        self.border = border
        if self.border:
            self.border_width = border_width
            self.border_radius = border_radius
            if border_color == -1:
                self.border_color = passive_color
            else:
                self.border_color = border_color
    def is_display_text(self, font, text, text_passive_color, text_x, text_y, text_active_color = None):
        self.display_text = True
        if not(isinstance(text, str)):
            raise Exception(f"TypeError: expected str instance")
        self.text_passive = font.render(text, True, text_passive_color)
        self.text_rect_passive = self.text_passive.get_rect()
        self.text_rect_passive.center = ((self.x+(self.width*text_x)), (self.y+(self.height*text_y)))
        if text_active_color != None:
            if self.button:
                self.text_active = font.render(text, True, text_active_color)
                self.text_rect_active = self.text_active.get_rect()
                self.text_rect_active.center = ((self.x+(self.width*text_x)), (self.y+(self.height*text_y)))
            else:
                raise Exception("box.error box object not set as button")
    
    def is_button(self, active_color, sticky=False):
        self.button = True
        self.active_color = active_color
        self.sticky = sticky
    
    
    def is_input(self):
        pass
    def input(self):
        pass
    
    def clicked(self, coordinates, status):
        x, y = coordinates[0], coordinates[1]
        x_boundry = self.x <= x <= self.x + self.width
        y_boundry = self.y <= y <= self.y + self.height
        if x_boundry and y_boundry:
            if self.sticky:
                return not(status)
            else:
                return True
        else:
            if self.sticky:
                return status
            else:
                return False
    
    def draw_text(self, click):
        if not(click):
            self.WIN.blit(self.text_passive, self.text_rect_passive)
        else:
            self.WIN.blit(self.text_active, self.text_rect_active)
    def draw_box(self, click=False):
        if not(self.transparent) and click and self.border and self.button:
            pygame.draw.rect(self.WIN, self.active_color, ((self.x + self.border_width), (self.y + self.border_width), (self.width - 2*self.border_width), (self.height - 2*self.border_width)))
            pygame.draw.rect(self.WIN, self.active_color, (self.x, self.y, self.width, self.height), self.border_width, self.border_radius)
        elif self.transparent and click and self.border and self.button:
            pygame.draw.rect(self.WIN, self.active_color, (self.x, self.y, self.width, self.height), self.border_width, self.border_radius)
        elif not(self.transparent) and not(click) and self.border:
            pygame.draw.rect(self.WIN, self.passive_color, ((self.x + self.border_width), (self.y + self.border_width), (self.width - 2*self.border_width), (self.height - 2*self.border_width)))
            pygame.draw.rect(self.WIN, self.passive_color, (self.x, self.y, self.width, self.height), self.border_width, self.border_radius)
        elif self.transparent and not(click):
            pygame.draw.rect(self.WIN, self.border_color, (self.x, self.y, self.width, self.height), self.border_width, self.border_radius)

        if self.display_text:
            self.draw_text(click)