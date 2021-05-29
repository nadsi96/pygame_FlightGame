
class Settings():
    
    def __init__(self):
        #비행기 설정
        self.flight_width = 75
        self.flight_height = 54
        self.flight_speed = 2
        #충돌 범위 설정
        self.crash_width = 20
        
        #screen 설정
        self.screen_width = 1080
        self.screen_height = 720
        self.bg_color = (230,230,230)
        
        #bullet 설정
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        
        #적기 설정
        self.enemy_speed = 0.5
        self.enemy_build_delay_min = 0.5
        self.enemy_build_delay_max = float(3)
        