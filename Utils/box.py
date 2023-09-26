import pygame
class box:
    def __init__(self, WIN, WIN_WIDTH, WIN_HEIGHT, x, y, width, height, transparent=False, passive_color=(), border=False, border_width=0, border_radius=0, border_color=None, display_text=False):
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
        self.display_text = display_text
        self.border = border
        self.input_box = False
        if self.border:
            self.border_width = border_width
            self.border_radius = border_radius
            if border_color == -1:
                self.border_color = passive_color
            else:
                self.border_color = border_color


    



    def is_button(self, active_color, sticky=False):
        self.button = True
        self.active_color = active_color
        self.sticky = sticky
    






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






    def draw_text(self, text, font, text_passive_color, text_active_color, text_x, text_y, clicked):
        if not(self.display_text):
            raise Exception("box.error object not able to display text")

        elif not(isinstance(text, str)):
            raise Exception("TypeError: expected str instance")
        if clicked:
            text_color = text_active_color
        else:
            text_color = text_passive_color
        self.text = font.render(text, True, text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = ((self.x+(self.width*text_x)), (self.y+(self.height*text_y)))

        self.WIN.blit(self.text, self.text_rect)

  
  
  
  
  
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

