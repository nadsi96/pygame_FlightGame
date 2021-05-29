import pygame.font
import pygame
from pygame.sprite import Sprite

class Game_Record(Sprite):
    def __init__(self, setting, screen, game_stat):
        self.screen = screen
        self.setting = setting
        
        self.screen_rect = screen.get_rect()
        
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        self.filename = 'game_record.csv'
        
        self.board_top = 70
        #self.rect.centerx = self.screen_rect.centerx
        
        """
        self.record_list = []
        self.rank_list = []
        self.score_list = []
        self.name_list = []
        """
        
        self.span = 68 #글자 간격
        
        self.show = False
        
    def prep_record(self):
        self.board_top = 70
        self.rank_list = []
        self.score_list  = []
        self.name_list = []
        for rl in self.record_list:
            rank_str = str(rl[0])
            score_str = str(rl[1])
            name_str = str(rl[2])
        
            self.rs_image = self.font.render(rank_str, True, self.text_color, self.setting.bg_color)
            self.rs_rect = self.rs_image.get_rect()
            self.rs_rect.centerx = self.screen_rect.centerx - 300
            self.rs_rect.top = self.board_top
            self.ss_image = self.font.render(score_str, True, self.text_color, self.setting.bg_color)
            self.ss_rect = self.ss_image.get_rect()
            self.ss_rect.centerx = self.screen_rect.centerx
            self.ss_rect.top = self.board_top
            
            self.ns_image = self.font.render(name_str, True, self.text_color, self.setting.bg_color)
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
        self.board_top = 70
        cnt = 0
        self.record_list = []
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                record = (line.strip()).split(',')
                self.record_list.append(record)
                cnt += 1
                if cnt > 8:
                    break
            f.close()
        self.prep_record()
    
    def write_game_record(self, setting, screen, game_stat):
        temp1_record_list = []
        temp2_record_list = []
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                record = (line.strip()).split(',')
                temp1_record_list.append(record) #record[0] = rank, record[1] = score, record[2] = name
            
        
        del temp1_record_list[0]
        cnt1 = 0
        cnt2 = 0
        
        for items in temp1_record_list:
            cnt2 = 0
            for item in items:
                (temp1_record_list[cnt1])[cnt2] = int(item)
                cnt2 += 1
            cnt1 += 1
        
        temp1_record_list.append([0, game_stat.score, 0])
        temp1_record_list.sort(key = lambda temp1_record_list:temp1_record_list[1])
        temp1_record_list.reverse()
        print(temp1_record_list)
        bestow_rank = 1
        cnt1 = 0
        for records in temp1_record_list:
            (temp1_record_list[cnt1])[0] = bestow_rank
            bestow_rank += 1
            cnt1 += 1
        temp1_record_list.insert(0, ["rank", "score", "name"])
        
        with open(self.filename, 'w') as f:
            cnt1 = 0
            cnt2 = 0
            for lst in temp1_record_list:
                cnt1 = 0
                for l in lst:
                    cnt1 += 1
                    f.write(str(l))
                    if cnt1 < 3:
                        f.write(', ')
                f.write('\n')
            

"""
with open("num.txt") as f:
    con = f.read()
print(con)
nlst = []
numlst = []
nlst = con.split()
print(nlst)
for n in nlst:
    numlst.append(int(n))
print(numlst)
sum = 0
for n in numlst:
    sum = sum + n
print(sum)



======================
students = [
        ('홍길동', 3.9, 2016303),
        ('김철수', 3.0, 2016302),
        ('최자영', 4.3, 2016301),
]
>>> sorted(students, key=lambda student: student[2])
[('최자영', 4.3, 2016301), ('김철수', 3.0, 2016302), ('홍길동', 3.9, 2016303)]
"""
