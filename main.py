import time
import random
import pygame
import sqlite3
from button import Button
from threading import Thread
from screeninfo import get_monitors


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

def main_menu_script():
    while main_menu_is_active:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                if start_button.is_targeted(event.pos):
                    start_button.target_animation()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # start_button.is_pressed((11, 22))
                print(event.pos)
                start_button.is_pressed(event.pos)
        start_button.draw(window)
        settings_button.draw(window)
        pygame.display.flip()
        clock.tick(fps)
    window.fill((0, 0, 0))

def conection_window():
    while waiting_for_start:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                if stop_button.is_targeted(event.pos):
                    stop_button.target_animation()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # stop_button.is_pressed((110, 201))
                print(event.pos)
                stop_button.is_pressed(event.pos)
        stop_button.draw(window)
        pygame.display.flip()
        clock.tick(fps)

    window.fill((0, 0, 0))

def main_game_script():
    while game_is_continue:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                print('UP')
            elif event.type == pygame.KEYDOWN:
                pass

        pygame.display.flip()
        clock.tick(fps)
    window.fill((0, 0, 0))

def settings_window():
    while settings_is_active:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                print('UP')
            elif event.type == pygame.KEYDOWN:
                pass

        pygame.display.flip()
        clock.tick(fps)
    window.fill((0, 0, 0))

def game_active():
    global game_is_continue, main_menu_is_active, waiting_for_start, app_is_active, fps
    window.fill((0, 0, 0))
    # loading = AnimatedSprite(load_image("loading.png"), 8, 2, 50, 50)
    stop_button = Button('No, I am out of there', 100, 200, 200, 100, func=game_exit, outline_lenth=10,
                          color_of_outline=(255, 255, 255))
    start_button = Button('Start', 10, 20, 200, 100, func=activate_game, outline_lenth=10,
                          color_of_outline=(255, 255, 255))
    settings_button = Button('Settings', 225, 125, 200, 100, func=settings)
    window.fill((0, 0, 0))
    while app_is_active:
        main_menu_script()
        connection_window()
        settings_window()
        main_game_script()



def settings():
    pass

def activate_game():
    global waiting_for_start, main_menu_is_active
    waiting_for_start = True
    main_menu_is_active = False

def game_exit():
    global waiting_for_start, main_menu_is_active
    waiting_for_start = False
    main_menu_is_active = True

def dice(start=1, end=7):
    return random.randrange(start, end)

if __name__ == '__main__':
    monitors_data = [monitor for monitor in get_monitors()]
    if len(monitors_data) > 1:
        for i in range(10):
            try:
                number_of_monitor = int(input("Введите номер монитора на котором вы хотите запустить игру")) - 1
                monitor = monitors_data[number_of_monitor]
                break
            except ValueError:
                print(f"Вы ввели неволидное значение, попробуйте ещё раз.\nБип-буп, у вас осталось {i + 1} попыток")
        else:
            print("Похоже вы не хотите играть, до свидания")
    else:
        monitor = monitors_data[0]

    total_cards = {}
    buttons = {}
    fps = 120
    clock = pygame.time.Clock()
    width, height = monitor.width, monitor.height
    size = width, height
    pygame.init()
    window = pygame.display.set_mode(size)
    pygame.display.flip()
    clock.tick(fps)
    game_is_continue = False
    waiting_for_start = False
    main_menu_is_active = True
    settings_is_active = False
    app_is_active = True



    # con = sqlite3.connect("cards.db")
    # cur = con.cursor()
    # result = cur.execute("""SELECT * FROM card
    #             WHERE type = "yourself" """).fetchall()
    #
    # for id in result:
    #     print(id)
    # con.close()


    print(dice())
    game_active()
    pygame.quit()