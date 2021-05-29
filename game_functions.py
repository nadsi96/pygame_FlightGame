import sys
import pygame
from bullet import Bullet
from enemy import Enemy_Flight
import time
import random
from threading import Thread

def check_events(setting, screen, flight, bullets, game_stat, button, game_record, enemies):
    #키 입력 확인
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 닫기 버튼이 눌렸다면 종료
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스 클릭이 있는 경우
            # 마우스가 클릭된 위치 좌표를 mouse_x, mouse_y에 저장
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # mouse_x, mouse_y과 button의 활성화 여부를 확인하여 버튼이 클릭되었는지 확인
            check_press_button(setting, screen, game_stat, enemies, button, mouse_x, mouse_y, game_record, flight)
            
        elif event.type == pygame.KEYDOWN:
            # 키보드 방향키가 눌린 경우
            if event.key == pygame.K_RIGHT:
                flight.right_flag = True
            elif event.key == pygame.K_LEFT:
                flight.left_flag = True
            elif event.key == pygame.K_UP:
                flight.up_flag = True
            elif event.key == pygame.K_DOWN:
                flight.down_flag = True
            elif event.key == pygame.K_SPACE:
                # spacebar가 눌렸다면 Bullet 생성(총알 발사)
                new_bullet = Bullet(setting, screen, flight)
                bullets.add(new_bullet) #쏘면 그룹에 총알 추가
                
        elif event.type == pygame.KEYUP:
            # 키보드 방향키에서 손을 땐 경우
            if event.key == pygame.K_RIGHT:
                flight.right_flag = False
            elif event.key == pygame.K_LEFT:
                flight.left_flag = False
            elif event.key == pygame.K_UP:
                flight.up_flag = False
            elif event.key == pygame.K_DOWN:
                flight.down_flag = False
    
    
# Enemy_Flight 생성 스레드 시작시키는 함수
# build_enemy 함수 실행시킴
def build_enemy_thread(setting, screen, enemies, game_stat):
    building_enemy = Thread(target=build_enemy, args = (setting, screen, enemies, game_stat))
    building_enemy.start()

#적기 생성. 화면 상단에서 랜덤한 위치에서 생성, 생성 시간차 0.5 ~ 3초
def build_enemy(setting, screen, enemies, game_stat):
    
    # 현재 게임 상황 확인
    game_stat.check_life()
    #while game_stat.game_play and not game_stat.game_over:
    
    # 게임오버가 될 때까지 화면 상단의 임의의 x위치에 Enemy_Flight 생성하여 enemies Group에 추가
    # 매 동작의 마지막에 남은 목숨 수를 확인하여 게임 오버 여부 확인
    # 게임 오버시 반복문을 끝내고 스레드 종료됨
    while game_stat.game_over == False:
        game_stat.check_level(setting)
        time.sleep(random.uniform(setting.enemy_build_delay_min, setting.enemy_build_delay_max)) #random.uniform(a, b) a~b 실수 난수 생성
        randx = random.randint(0, setting.screen_width-setting.flight_width)
        new_enemy = Enemy_Flight(setting, screen, randx)
        enemies.add(new_enemy)
        print("spawn enemy")
        game_stat.check_life()
    
        
def check_hit(setting, enemies, bullets, game_stat):#총알이 적기를 맞췄을 때
                                            #bullet과 enemy rect가 겹쳤을 때 제거
    #collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for e in enemies:
        for b in bullets:
            if b.rect.centerx >= (e.rect.x) and b.rect.centerx <= (e.rect.x + setting.flight_width):
                if b.rect.y <= e.rect.y + setting.flight_height:
                    game_stat.score_hit()
                    print(game_stat.score)
                    bullets.remove(b)
                    enemies.remove(e)

def check_crash(setting, flight, enemies, game_stat, lifeboard):#적기와 충돌한 경우
    for e in enemies:
        if flight.rect.centerx >= e.rect.x-setting.crash_width and flight.rect.centerx <= e.rect.x + setting.flight_width + setting.crash_width:
            if flight.rect.bottom <= e.rect.y + setting.flight_height and flight.rect.bottom + setting.flight_height >= e.rect.y:
                game_stat.life -= 1
                #lifeboard.prep_life(game_stat)
                print(" Flight hit")
                # 충돌한 Enemy_Flight 제거
                enemies.remove(e)
                # Flight의 위치 화면 하단 중앙으로 변경
                flight.rect.centerx = flight.screen_rect.centerx
                flight.rect.bottom = flight.screen_rect.bottom

def check_enemy_bottom(setting, enemies, game_stat,):#화면 하단에 도달한 적기 삭제
    for e in enemies:
        if e.rect.y >= setting.screen_height:
            game_stat.score_enemy_bottom()
            enemies.remove(e)
            print(game_stat.score)

def check_press_button(setting, screen, game_stat, enemies, button, mouse_x, mouse_y, game_record, flight):
    #마우스의 위치가 버튼의 rect좌표 안인 경우
    if button[0].rect.collidepoint(mouse_x, mouse_y) and not game_stat.game_play:
        # ==> 초기화면 상태 (play, record 버튼 활성화)
        # play 버튼 좌표와 겹치는지 확인
        game_stat.reset_game(flight, setting)        #play button
        game_stat.check_life()
        button[0].show_button = False
        #building_enemy.start()
        build_enemy_thread(setting, screen, enemies, game_stat)
        
    elif button[1].rect.collidepoint(mouse_x, mouse_y) and game_stat.game_play and game_stat.game_over:
        # ==> 게임 오버 화면 상태 (replay, quit 버튼 활성화)
        # replay 버튼 좌표와 겹치는지 확인
        game_stat.reset_game(flight, setting)   #replay button
        game_stat.check_life()
        build_enemy_thread(setting, screen, enemies, game_stat)
        
    elif button[2].rect.collidepoint(mouse_x, mouse_y) and game_stat.game_play and game_stat.game_over:
        # ==> 게임 오버 화면 상태 (replay, quit 버튼 활성화)
        # quit 버튼 좌표와 겹치는지 확인
        game_stat.game_play = False   #quit button
        game_stat.game_over = False
        
    elif button[3].rect.collidepoint(mouse_x, mouse_y) and not game_stat.game_play: 
        # ==> 초기화면 상태 (play, record 버튼 활성화)
        # record 버튼 좌표와 겹치는지 확인
        
        #game_record.show_game_record()   #record button
        game_record.show = True
        
    elif button[4].rect.collidepoint(mouse_x, mouse_y) and not game_stat.game_play:
        # ==> 점수화면 표시 상태 (back 버튼 활성화)
        # back 버튼 좌표와 겹치는지 확인
        
        game_record.show = False #back button\
    """    
    for b in button: #button들 안보이게
        b.show_button = False
    """

# 화면 상태 업데이트
# Flight, enemies, bullets의 위치 업데이트
# 점수판과 남은 목숨 텍스트 업데이트
# 프로그램 상태에 따른 버튼 활성화 상태 업데이트
def update_screen(setting, screen, flight, bullets, enemies, game_stat, sb, lb, button, game_record):
    
    screen.fill(setting.bg_color)
    if game_stat.game_play and not game_stat.game_over: #게임 플레이 중
        flight.blitme()#비행기 위치 표시
        sb.playing_score()
        sb.show_score()
        lb.prep_life(game_stat)
        lb.show_life()
        for bullet in bullets.sprites(): # bullets그룹에 있는 모든 스프라이트에서 호출
            bullet.draw_bullet()
        for enemy in enemies.sprites():
            enemy.update()
            enemy.blitme()
    elif not game_stat.game_play and not game_stat.game_over and not game_record.show:
        button[0].draw_button()#play button
        button[3].draw_button()#record button
    elif game_record.show and not game_stat.game_over:
        game_record.show_game_record()
        button[4].draw_button()#back button
    elif game_stat.game_over and game_stat.game_play:
        """
        for b in bullets:
            bullets.remove(b)
        for e in enemies:
            enemies.remove(e)
        """
        if game_stat.life == 0:
            game_record.write_game_record(setting, screen, game_stat)
            time.sleep(3)
            game_stat.life = -1
        bullets.empty()
        enemies.empty()
        sb.game_over_score()
        sb.show_score()
        button[1].draw_button()#replay button
        button[2].draw_button()#quit button
        #game_record.show_game_record()
    #elif game_stat.game_over and not game_stat.game_play:
        #game_record.show_game_record(setting, screen, game_stat)
        
    pygame.display.flip()#가장 최근에 그려지는 화면 표시
