import pygame.font
import pygame
from pygame.sprite import Sprite
import db_handler


class Game_Record(Sprite):
    def __init__(self, setting, screen, game_stat):
        self.screen = screen
        self.setting = setting
        
        self.screen_rect = screen.get_rect()
        
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        self.filename = 'game_record.csv'
        
        self.board_top = 70
        
        self.span = 68 #글자 간격
        
        self.show = False
        
    def prep_record(self, rankList, ScoreList, NameList):
        self.board_top = 70
        self.rank_list = []
        self.score_list  = []
        self.name_list = []
        
        rankList.insert(0, "RANK")
        ScoreList.insert(0, "SCORE")
        NameList.insert(0, "NAME")

        for rank, score, name in zip(rankList, ScoreList, NameList):
            rank_str = str(rank)
            score_str = str(score)
            
            self.rs_image = self.font.render(rank_str, True, self.text_color, self.setting.bg_color)
            self.rs_rect = self.rs_image.get_rect()
            self.rs_rect.centerx = self.screen_rect.centerx - 300
            self.rs_rect.top = self.board_top
            self.ss_image = self.font.render(score_str, True, self.text_color, self.setting.bg_color)
            self.ss_rect = self.ss_image.get_rect()
            self.ss_rect.centerx = self.screen_rect.centerx
            self.ss_rect.top = self.board_top
            
            self.ns_image = self.font.render(name, True, self.text_color, self.setting.bg_color)
            self.ns_rect = self.ns_image.get_rect()
            self.ns_rect.centerx = self.screen_rect.centerx + 300
            self.ns_rect.top = self.board_top
            
            self.rank_list.append((self.rs_image, self.rs_rect))
            self.score_list.append((self.ss_image, self.ss_rect))
            self.name_list.append((self.ns_image, self.ns_rect))
            
            self.board_top += self.span
        self.show_record()
        
    def show_record(self):
        for rl in self.rank_list:
            self.screen.blit(rl[0], rl[1])
        for sl in self.score_list:
            self.screen.blit(sl[0], sl[1])
        for nl in self.name_list:
            self.screen.blit(nl[0], nl[1])
    
    def show_game_record(self):
        db = db_handler.DB_Handler.instance()
        df = db.get_Scores()
#        self.record_list = [df.index, df["Score"], df["Name"]]
        self.prep_record(list(df.index), list(df["Score"]), list(df["Name"]))
        return
            
    def input_game_record(self, setting, screen, game_stat):
        db = db_handler.DB_Handler.instance()
        db.insert_Score(game_stat.score)
        return