
import pygame

from settings import Settings
from Flight import Flight
from Game_Stat import Game_Stat
from Game_Stat import ScoreBoard
from Game_Stat import LifeBoard

from button import Button
from button import replay_Button
from button import quit_Button
from button import record_Button
from button import back_Button

from game_record import Game_Record
import game_functions as gf
from pygame.sprite import Group

#from threading import Thread

def run_game():
    pygame.init()
    
    game_stat = Game_Stat()
    game_set = Settings()
    
    # 화면 설정
    screen = pygame.display.set_mode((game_set.screen_width, game_set.screen_height))
    pygame.display.set_caption("Game_Flight")
    
    flight = Flight(game_set, screen)
    bullets = Group() # 발사된 Bullet이 담길 Group
    enemies = Group() # 생성된 Enemy_Flight가 저장될 Group
    sb = ScoreBoard(game_set, screen, game_stat) # 게임 플레이 중 화면에 나타날 점수판
    lb = LifeBoard(game_set, screen, game_stat) # 게임 플레이 중 화면에 나타날 남은 목숨
    gr = Game_Record(game_set, screen, game_stat) # 게임 기록(점수) 표시
    play_button = Button(game_set, screen, "Play") # Play 버튼
    replay_button = replay_Button(game_set, screen, "Replay") # Replay 버튼
    quit_button = quit_Button(game_set, screen, "Quit") # Quit 버튼
    record_button = record_Button(game_set, screen, "Record") # Record 버튼
    back_button = back_Button(game_set, screen, "Back") # Back 버튼
    
    button = [play_button, replay_button, quit_button, record_button, back_button]
    
    #building_enemy = Thread(target=gf.build_enemy, args = (game_set, screen, enemies, game_stat))#적기 생성 스레드
    #building_enemy.start()
    
    while True:
        #키 입력 확인
        gf.check_events(game_set, screen, flight, bullets, game_stat, button, gr, enemies)
        
        if game_stat.game_play:
            flight.update(game_set)                             #비행기 위치좌표 업데이트
            bullets.update()                                    #탄환 위치좌표 업데이트
            gf.check_hit(game_set, enemies, bullets, game_stat) #탄환과 적기 충돌 확인
            gf.check_crash(game_set, flight, enemies, game_stat, lb)#적기와 주인공 충돌 확인
        
            for b in bullets.copy(): #화면 상단에 도달한 탄환 삭제
                if b.rect.bottom <= 0:
                    bullets.remove(b)              
            game_stat.check_life() # 현재 남은 목숨 확인하여 게임을 계속 직행시킬지 확인
        
            gf.check_enemy_bottom(game_set, enemies, game_stat) #화면 하단에 도착한 Enemy_Flight 확인하여 처리
        
        # 화면 상태 업데이트
        gf.update_screen(game_set, screen, flight, bullets, enemies, game_stat, sb, lb, button, gr)
        
run_game()