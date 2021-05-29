import pygame


# 사용자가 조작할 비행가
class Flight():
    def __init__(self, setting, screen):
        self.screen = screen
        
        # temp_image로 이미지를 불러온 뒤
        # image에 크기가 조정된 image 저장
        self.temp_image = pygame.image.load('비행기.png')
        self.image = pygame.transform.scale(self.temp_image, (setting.flight_width ,setting.flight_height))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 방향키가 눌려있는지 여부를 나타내는 flag
        self.right_flag = False
        self.left_flag = False
        self.up_flag = False
        self.down_flag = False
        
    def update(self, setting):
        if self.right_flag and self.rect.centerx <= setting.screen_width:
            # 오른쪽 키가 눌려있고, Flight의 Rect객체의 중심 x좌표가 화면의 폭보다 작으면 이동
            # ==>  오른쪽 끝을 넘어가면 더 이상 오른쪽으로 이동하지 않음
            self.rect.centerx += setting.flight_speed
        elif self.left_flag and self.rect.centerx >= 0:
            # 왼쪽 키가 눌려있고, Flight의 Rect객체의 중심 x좌표가 0보다 크면 이동
            # ==>  왼쪽 끝을 넘어가면 더 이상 왼쪽으로 이동하지 않음
            self.rect.centerx -= setting.flight_speed
        elif self.down_flag and self.rect.bottom <= setting.screen_height:
            # 아래쪽 키가 눌려있고, Flight의 Rect객체의 하단 y좌표가 화면의 화면의 높이보다 작으면 이동
            # ==>  하단 끝을 넘어가면 더 이상 아래로 이동하지 않음
            self.rect.bottom += setting.flight_speed
        elif self.up_flag and self.rect.bottom >= 0:
            # 위쪽 키가 눌려있고, Flight의 Rect객체의 하단 y좌표가 0보다 크면 작으면 이동
            # ==>  상단 끝을 넘어가면 더 이상 위로 이동하지 않음
            self.rect.bottom -= setting.flight_speed
        
    def blitme(self):
        #비행기 현재 위치에 그림
        self.screen.blit(self.image, self.rect)