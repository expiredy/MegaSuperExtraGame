import os
import pygame
import time
from threading import Thread

class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def move(self, dx, dy):

        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        self.rect.x += dx
        self.rect.y += dy

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom


class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class Timer:
    def __init__(self, min_value=50, max_value=150, pos_x=0, pos_y=0, font="Lilita One Russian", font_size=90):
        self.pos_x, self.pos_y = pos_x, pos_y
        self.font, self.font_size = font, font_size
        self.value = randint(min_value, max_value)
        self.counter = Thread(target=self.timer)

    def start(self):
        self.counter.start()

    def timer(self):
        while not game_is_end:
            time.sleep(1)
            self.value -= 1
            if self.value <= 0:
                game_is_end = True

    def draw(self, canvas):
        pass

def game_ending():
    print('U win')







level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W       WWWW   WW       WWW    W    WWWWWWW",
    "WW WWWW    W W        W W    W WWW  W     W",
    "W     W WW W W W W    W W   W  W    W WWW W",
    "WWWWW   W    W W WWWW W    W   W W  W WEW W",
    "W      WWWWWW  W      W W  W WW  W  W W   W",
    "W  WWWW      W W W  W  WWW W  W W  WW WWWWW",
    "W       WWWW     W   W     W    W         W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]


def maze_run(sceen):
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    walls = []
    player = Player()
    x = y = 0
    for row in level:
        for col in row:
            if col == "W":
                Wall((x, y))
            if col == "E":
                end_rect = pygame.Rect(x, y, 16, 16)
            x += 16
        y += 16
        x = 0

        def timer_():
            counter, text = 10, '10'.rjust(3)
            pygame.time.set_timer(pygame.USEREVENT, 1000)
            font = pygame.font.SysFont('Consolas', 30)
            while True:
                for e in pygame.event.get():
                    if e.type == pygame.USEREVENT:
                        counter -= 1
                        text = str(counter).rjust(3) if counter > 0 else 'слоупок'
                    if e.type == pygame.QUIT: break
                else:
                    screen.fill((255, 255, 255))
                    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
                    pygame.display.flip()
                    clock.tick(60)
                    continue
                break

    game_is_end = False
    running = True
    while running:
        clock.tick(60)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False

        key = pygame.key.get_pressed()
        if not game_is_end:
            if key[pygame.K_LEFT]:
                player.move(-2, 0)
            if key[pygame.K_RIGHT]:
                player.move(2, 0)
            if key[pygame.K_UP]:
                player.move(0, -2)
            if key[pygame.K_DOWN]:
                player.move(0, 2)
        elif key:
            pass


        if player.rect.colliderect(end_rect):
            game_is_end = True
            game_ending()

        screen.fill((0, 0, 0))
        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall.rect)
        pygame.draw.rect(screen, (255, 0, 0), end_rect)
        pygame.draw.rect(screen, (255, 200, 0), player.rect)
        pygame.display.flip()