import time
import random
import pygame
import sqlite3
import sys
import os
import BackgroundVideo
import config
from button import Button, TextButton, InputField
from threading import Thread
from screeninfo import get_monitors

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__()
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

class FolederWithSprites(pygame.sprite.Sprite):
    max_frame = 0
    def __init__(self, path, base_name, start_value='000', targeted_max_value='100', image_resolution='png',
                 x_cord=0, y_cord=0, x_lenth=1920, y_lenth=1080,
                 is_loop=True):
        super().__init__()
        self.is_loop = is_loop
        self.path = path
        self.base_name = base_name
        self.x_cord, self.y_cord, self.x_lenth, self.y_lenth = x_cord, y_cord, x_lenth, y_lenth
        self.image_resolution = image_resolution
        self.start_value, self.present_value, self.targeted_max_value = start_value, start_value, targeted_max_value
        self.frame_counter = self.max_frame

    def update(self):
        if self.frame_counter == self.max_frame:
            self.image = load_image(self.path + '\\' + self.base_name + self.present_value + self.image_resolution)
            self.rect = pygame.Rect(self.x_cord, self.y_cord, self.x_lenth, self.y_lenth)
            present_value = str((int(self.present_value) + 1) % int(self.targeted_max_value))
            present_value = present_value if present_value >= self.start_value else self.start_value
            self.present_value = '0' * (len(self.targeted_max_value) - len(present_value)) + present_value
            self.frame_counter = 0
        else:
            self.frame_counter += 1

class logo_constructor(pygame.sprite.Sprite):
    def __init__(self, name, x_cord=0, y_cord=0, x_lenth=1920, y_lenth=1080):
        self.image = load_image(name)
        self.image = pygame.transform.scale(self.image, (x_lenth, y_lenth))
        print(x_cord, y_cord, x_lenth, y_lenth)
        self.x_cord, self.y_cord, self.x_lenth, self.y_lenth = x_cord, y_cord, x_lenth, y_lenth
        self.rect = pygame.Rect(self.x_cord, self.y_cord, self.x_lenth, self.y_lenth)

def load_image(name, colorkey=None):
    fullname = os.path.join('Sprites', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

def main_menu_event_checker(event, start_button, settings_button, exit_button, customize_yourself):
    if event.type == pygame.QUIT:
        app_exit()
    if event.type == pygame.MOUSEMOTION:
        if start_button.is_targeted(event.pos):
            start_button.target_animation()
        elif settings_button.is_targeted(event.pos):
            pass
        elif exit_button.is_targeted(event.pos):
            exit_button.target_animation()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        customize_yourself.is_pressed(event.pos)
        start_button.is_pressed(event.pos)
        exit_button.is_pressed(event.pos)

def main_menu_script():
    global width, height
    start_button = Button('Start', width // 2 - 150, height // 2 - 100, 300, 150, func=choice_game_mode,
                          outline_lenth=10, background=(0, 0, 0), color_of_outline=(205, 205, 205),
                          text_color=(255, 255, 255))
    exit_button = Button('Exit', width // 2 - 150, height * 0.815, 300, 150, func=app_exit, outline_lenth=10,
                         background=(0, 0, 0), color_of_outline=(205, 205, 205),
                         text_color=(255, 255, 255))
    settings_button = Button('Settings', width // 2 - 150, height * 0.6, 300, 150, func=settings,
                             text_color=(255, 255, 255))

    customize_yourself = Button('Profile settings', width * 0.8, height * 0.8, 300, 150, func=set_info_for_game,
                             text_color=(255, 255, 255), font_size=40)

    background_video = FolederWithSprites(r'BackgroundCitySprites',
                                          "BackgroundCity ", "0001", "0995", ".jpg", x_cord=0, y_cord=0,
                                          x_lenth=width, y_lenth=height)

    mafia_logo = logo_constructor('text_mafia.png', width * 0.25, 0, 1000, 800)
    # background_video = BackgroundVideo.run(window, 'Sprites\BackgroundCity.mp4')
    background_video = FolederWithSprites(r'BackgroundCitySprites',
                                          "BackgroundCity ", "0001", "0995", ".jpg", x_cord=0, y_cord=0,
                                          x_lenth=width, y_lenth=height)
    # thread_with_logo = Thread(target=background_drawer, args=(mafia_logo,))
    # thread_with_logo.start()
    while main_menu_is_active:
        for event in pygame.event.get():
            new_event = Thread(target=main_menu_event_checker, args=(event, start_button, settings_button,
                                                                     exit_button, customize_yourself))
            new_event.start()
        background_video.update()
        window.blit(background_video.image, background_video.rect)
        window.blit(mafia_logo.image, mafia_logo.rect)
        start_button.draw(window)
        settings_button.draw(window)
        customize_yourself.draw(window)
        exit_button.draw(window)
        pygame.display.flip()
        clock.tick(fps)
    window.fill((0, 0, 0))
    new_event.join()

def connection_window():
    stop_button = Button('No, I am out of there', width // 2 - 150, height * 0.8, 300, 150, func=set_info_for_game,
                         args=(False,), outline_lenth=10, background=(0, 0, 0), color_of_outline=(205, 205, 205))
    while waiting_for_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app_exit()
            if event.type == pygame.MOUSEMOTION:
                if stop_button.is_targeted(event.pos):
                    stop_button.target_animation()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                stop_button.is_pressed(event.pos)
        stop_button.draw(window)
        pygame.display.flip()
        clock.tick(fps)

    window.fill((0, 0, 0))

def main_game_script():
    while game_is_continue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app_exit()
            if event.type == pygame.KEYUP:
                print('UP')
            elif event.type == pygame.KEYDOWN:
                pass

        pygame.display.flip()
        clock.tick(fps)
    window.fill((0, 0, 0))

def choicing_game_mode_window():
    global choising_game_mode
    back_button = Button('Back', width // 2 - 150, height * 0.8, 300, 150, func=choice_game_mode, args=(False,),
                         outline_lenth=10, background=(0, 0, 0), color_of_outline=(205, 205, 205))
    window.fill((0, 0, 0))
    while choising_game_mode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app_exit()
            if event.type == pygame.KEYUP:
                print('UP')
            elif event.type == pygame.KEYDOWN:
                pass
            elif event.type == pygame.MOUSEMOTION:
                if back_button.is_targeted(event.pos, True):
                    back_button.target_animation()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                back_button.is_pressed(event.pos)


        back_button.draw(window)
        pygame.display.flip()
        clock.tick(fps)
    window.fill((0, 0, 0))

def setting_inforamtion():
    name_input = InputField(width // 2 - 250, height * 0.1, 500, 150)
    back_button = Button('Back', width // 2 - 150, height * 0.8, 300, 150, func=set_info_for_game, args=(False,),
                         outline_lenth=10, background=(0, 0, 0), color_of_outline=(205, 205, 205))
    save_button = Button('Save', width // 2 + 150, height * 0.8, 300, 150, func=save_and_back_to_main_menu,
                         args=(name_input,),
                         outline_lenth=10, background=(0, 0, 0), color_of_outline=(205, 205, 205))

    while set_information:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app_exit()
            if event.type == pygame.KEYUP:
                name_input.checker_for_upper_letter(event)
            elif event.type == pygame.KEYDOWN:
                name_input.activate_input(event)
            elif event.type == pygame.MOUSEMOTION:
                if back_button.is_targeted(event.pos):
                    back_button.target_animation()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                name_input.is_pressed(event.pos)
                back_button.is_pressed(event.pos)
                save_button.is_pressed(event.pos)
        name_input.draw(window)
        save_button.draw(window)
        back_button.draw(window)
        pygame.display.flip()
        clock.tick(fps)
    window.fill((0, 0, 0))

def settings_window():
    while settings_is_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app_exit()
            if event.type == pygame.KEYUP:
                print('UP')
            elif event.type == pygame.KEYDOWN:
                pass

        pygame.display.flip()
        clock.tick(fps)
    window.fill((0, 0, 0))

def save_and_back_to_main_menu(name_input):
    data_save(name_input)
    choice_game_mode(False)

def enter_game():
    global game_entering_window
    crearing_room_button = Button('Create', width // 2 - 150, height // 2 - 100, 300, 150, func=choice_game_mode,
                          outline_lenth=10, background=(0, 0, 0), color_of_outline=(205, 205, 205),
                          text_color=(255, 255, 255))
    connecting_to_room_button = Button('Connect', width // 2 - 150, height * 0.815, 300, 150, func=app_exit, outline_lenth=10,
                         background=(0, 0, 0), color_of_outline=(205, 205, 205),
                         text_color=(255, 255, 255))

    while game_entering_window:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app_exit()
            if event.type == pygame.KEYUP:
                print('UP')
            elif event.type == pygame.KEYDOWN:
                pass

        pygame.display.flip()
        clock.tick(fps)
    window.fill((0, 0, 0))

def settings():
    pass

def game_active():
    global waiting_for_start,  set_information
    waiting_for_start, set_information = True, False

def set_info_for_game(value=True):
    global main_menu_is_active, set_information
    set_information = value
    main_menu_is_active = not value

def choice_game_mode(value=True):
    global choising_game_mode, main_menu_is_active
    choising_game_mode, main_menu_is_active = value, not value

def main_script():
    global game_is_continue, main_menu_is_active, waiting_for_start, app_is_active, fps
    # loading = AnimatedSprite(load_image("loading.png"), 8, 2, 50, 50)
    window.fill((0, 0, 0))
    while app_is_active:
        main_menu_script()
        connection_window()
        settings_window()
        main_game_script()
        setting_inforamtion()
        choicing_game_mode_window()

def game_exit():
    global waiting_for_start, main_menu_is_active
    waiting_for_start = False
    main_menu_is_active = True

def data_save(name_input=None):
    if name_input:
        config.player_name = str(name_input)
    print(config.player_name)

def app_exit():
    global game_is_continue, waiting_for_start, main_menu_is_active, settings_is_active, app_is_active,\
        set_information, choising_game_mode, game_entering_window
    data_save()
    set_information = False
    game_is_continue = False
    waiting_for_start = False
    main_menu_is_active = False
    settings_is_active = False
    app_is_active = False
    choising_game_mode = False
    game_entering_window = False

    print(exit)

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
    fps = 144
    clock = pygame.time.Clock()
    width, height = monitor.width, monitor.height
    size = width, height
    pygame.init()
    window = pygame.display.set_mode(size)
    pygame.display.flip()
    clock.tick(fps)
    app_is_active = True
    main_menu_is_active = True
    set_information = False
    settings_is_active = False
    waiting_for_start = False
    game_is_continue = False
    choising_game_mode = False
    game_entering_window = False

    main_script()
    pygame.quit()