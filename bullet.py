import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self, setting, screen, flight):
        super(Bullet, self).__init__()
        self.screen = screen
                                #(가로위치, 세로위치, 가로길이, 세로길이)
        self.rect = pygame.Rect(0,0, setting.bullet_width, setting.bullet_height)
        self.rect.centerx = flight.rect.centerx
        self.rect.top = flight.rect.top
        
        self.color = setting.bullet_color
        self.speed_factor = setting.bullet_speed_factor
        
    def update(self):
        self.rect.y -= self.speed_factor
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)