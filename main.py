import time
import random
import pygame
import sqlite3
from button import Button
from threading import Thread
from screeninfo import get_monitors

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




class Card:
    def __init__(self, type, *parameters):
        self.description = ''

def dice(start=1, end=7):
    return random.randrange(start, end)


def main_menu_script():
    global main_menu_is_active, fps
    start_button = Button('Start', 10, 20, 200, 100, func=game_active, outline_lenth=10,
                          color_of_outline=(255,255,255))
    settings_button = Button('Settings', 225, 125, 200, 100, func=settings)
    while main_menu_is_active:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                if start_button.is_targeted(event.pos):
                    start_button.target_animation()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                start_button.is_pressed(event.pos)
        start_button.draw(window)
        settings_button.draw(window)
        pygame.display.flip()
        clock.tick(fps)

def game_active():
    global game_is_continue, main_menu_is_active, fps
    main_menu_is_active = False
    game_is_continue = True
    window.fill((0, 0, 0))
    while game_is_continue:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                print('UP')
            elif event.type == pygame.KEYDOWN:
                pass
        pygame.display.flip()
        clock.tick(fps)

def settings():
    pass


fps = 120
clock = pygame.time.Clock()
width, height = monitor.width, monitor.height
size = width, height
pygame.init()
window = pygame.display.set_mode(size)
pygame.display.flip()
clock.tick(fps)
game_is_continue = False
main_menu_is_active = True


# con = sqlite3.connect("cards.db")
# cur = con.cursor()
# result = cur.execute("""SELECT * FROM card
#             WHERE type = "yourself" """).fetchall()
#
# for id in result:
#     print(id)
# con.close()


print(dice())
main_menu_script()
pygame.quit()