import pygame.font


# 버튼 기본 틀
class Button():
    def __init__(self, setting, screen, msg):
        # msg = 버튼에 입력될 text
        # self.prep_msg(msg) 통해 해당 버튼에 text 입력
        self.screen = screen
        self.setting = setting
        self.screen_rect = screen.get_rect()
        
        self.width, self.height = 200, 50
        self.button_color = (50, 50, 50)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)
        
        self.rect = pygame.Rect(0,0,self.width, self.height)
        # 버튼의 rect객체 생성, 중앙에 배치
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        self.show_button = True
        self.prep_msg(msg)
        
        self.button_span = 70
        
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        

# 다시 게임 시작 버튼
class replay_Button(Button):
    def __init__(self, setting, screen, msg):
        super().__init__(setting, screen, msg)
        self.button_color = (100, 100, 100)
        self.show_button = False
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center
        
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)
        
        
# 종료 버튼
class quit_Button(Button):
    def __init__(self, setting, screen, msg):
        super().__init__(setting, screen, msg)
        self.button_color = (150, 150, 150)
       # self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery + self.button_span
        self.show_button = False
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        
        self.msg_img_rect.centerx = self.rect.centerx
        self.msg_img_rect.centery = self.rect.centery
        
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)

# 점수 확인 버튼
class record_Button(Button):
    def __init__(self, setting, screen, msg):
        super().__init__(setting, screen, msg)
        self.button_color = (150, 150, 150)
       # self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery + self.button_span
        #self.show_button = False
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        
        self.msg_img_rect.centerx = self.rect.centerx
        self.msg_img_rect.centery = self.rect.centery
        
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)


# 뒤로가기 버튼
class back_Button(Button):
    def __init__(self, setting, screen, msg):
        super().__init__(setting, screen, msg)
        self.rect.centery = self.setting.screen_height - 70
        self.prep_msg(msg)
    def prep_msg(self, msg):
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        
        self.msg_img_rect.centerx = self.rect.centerx
        self.msg_img_rect.centery = self.rect.centery
        
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)
        