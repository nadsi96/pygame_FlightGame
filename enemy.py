import pygame
from pygame.sprite import Sprite

class Enemy_Flight(Sprite):
    def __init__(self, setting, screen, rand):
        # rand = 0부터 화면의 폭까지의 임의의 숫자
        super(Enemy_Flight, self).__init__()
        self.screen = screen
        self.setting = setting
        
        self.temp_image = pygame.image.load('비행기2.png')
#        self.temp_image = pygame.image.load('1111.jpg')
        self.image = pygame.transform.scale(self.temp_image, (setting.flight_width ,setting.flight_height))
        self.rect = self.image.get_rect()
        """
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        """
        
        # 생성시 x좌표는 임의의 위치
        self.rect.x = rand
        self.rect.y = 0
        
        self.y = float(self.rect.y)
        
        self.speed_factor = setting.enemy_speed
        
    def update(self):
        self.y += self.speed_factor
        self.rect.y = self.y
        
    def blitme(self):
        # 화면에 상태 업데이트
        self.screen.blit(self.image, self.rect)
        
        
"""
import random
random.randInt(a, b) 위치 무작위로 소환


3초에 하나씩 등장
import time
                #time.time() (현재 시간)
start = time.time() #while구문 전


if time.time() - start > 5  #5초뒤 시작
적비행기 생성 시작
if time.time()%3 == 0
적 비행기 생성
"""