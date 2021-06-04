
class Game_Stat():
    def __init__(self):
        self.life = 3
        self.score = 0
        self.game_play = False
        self.game_over = False
        self.hit_score = 10
        self.lose_score = -5
        self.lvchk = 200
        self.level = 1
        

    def score_hit(self):
        self.score = self.score + self.hit_score
        
    def score_enemy_bottom(self):
        self.score = self.score + self.lose_score
        
    def check_life(self):
        if self.life <= 0:
            self.game_over = True
            #self.game_play = False

        elif self.life > 0:
            self.game_play = True
            self.game_over = False
            
    def reset_game(self, flight, setting):
        self.life = 3
        self.score = 0
        flight.rect.centerx = flight.screen_rect.centerx
        flight.rect.bottom = flight.screen_rect.bottom
        self.lvchk = 200
        self.level = 1
        setting.enemy_build_delay_max = float(3.0)
        setting.enemy_build_delay_min = float(0.5)
        setting.enemy_speed = float(0.5)
    
    def quit_game(self):
        self.game_play = False
        self.game_over = False
        
    def check_level(self, setting):
        if self.score >= self.lvchk:
            self.level += 1
            self.lvchk += 300
            if self.level <= 5:
                setting.enemy_build_delay_max -= 0.2
                if self.level == 4:
                    setting.enemy_speed += 0.1
            elif self.level > 5 and self.level <= 8:
                setting.enemy_build_delay_min -= 0.1
                if self.level == 8:
                    setting.enemy_speed += 0.1
            elif self.level > 8 and self.level <= 10:
                setting.enemy_build_delay_max -= 0.2
                if self.level == 10:
                    setting.enemy_speed += 0.1
                
    

import pygame.font
class ScoreBoard():
    def __init__(self, setting, screen, game_stat):
        self.screen = screen
        self.setting = setting
        self.game_stat = game_stat
        
        self.screen_rect = screen.get_rect()
        
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        self.game_over_font = pygame.font.SysFont(None, 80)
        
        self.playing_score()
        
    def playing_score(self):
        score_str = str(self.game_stat.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.setting.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = 20
        
    def game_over_score(self):
        score_str = str(self.game_stat.score)
        self.score_image = self.game_over_font.render(score_str, True, self.text_color, self.setting.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = 50
        
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        
class LifeBoard():
    def __init__(self, setting, screen, game_stat):
        self.screen = screen
        self.setting = setting
        
        self.screen_rect = screen.get_rect()
        
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 30)
        
        self.prep_life(game_stat)
        
    def prep_life(self, game_stat):
        life_str = "Life : " + str(game_stat.life)
        self.life_image = self.font.render(life_str, True, self.text_color, self.setting.bg_color)
        self.life_rect = self.life_image.get_rect()
        self.life_rect.right = self.screen_rect.right - 20
        self.life_rect.top = 20
        
    def show_life(self):
        self.screen.blit(self.life_image, self.life_rect)