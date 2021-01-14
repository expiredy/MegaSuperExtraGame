__all__ = ('Button', 'TextButton', 'InputField', 'TextViewer')


import pygame
from threading import Thread
from time import sleep


class Button():
    button_group = None
    animation_max_frame = 20
    def __init__(self, button_text, x_cord, y_cord, x_lenth, y_lenth, func=None, args=None, new_button_group=None,
                 text_color=(255, 0, 0), font_size=90, font_for_text="Lilita One Russian",
                 background=(75,85,255), backgroynd_tex=None, color_of_outline=None,
                 outline_lenth=None):
        self.button_text = str(button_text)
        self.x_cord, self.y_cord, self.x_lenth, self.y_lenth = x_cord, y_cord, x_lenth, y_lenth
        self.color_of_outline, self.outline_lenth = color_of_outline, outline_lenth
        self.is_animation_started = False

        try:
            self.x_cord, self.y_cord = x_cord, y_cord
        except ValueError:
            print('Not intenger, Try again, dude')
            raise ValueError()
        if not type(self.button_group):
            print("There is not group for buttons")
            raise ValueError()
        elif new_button_group:
            self.button_group = new_button_group
        self.name = button_text
        self.args = args
        self.main_function = func
        self.text_color = text_color
        self.present_animation_frame = 0
        self.background = background if not backgroynd_tex else backgroynd_tex
        self.font_for_text, self.font_size, self.start_font_size = font_for_text, font_size, font_size
        self.start_animation,  self.end_animation = False, False
        self.end_animarion_is_avtived, self.start_animation_is_avtived = False, False
        self.normal_size = True
        self.bigger_size = False
        self.last_pos = None

    def is_pressed(self, pos):
        if self.is_targeted(pos):
            print('Scanner of mouse deteced a fricking click')
            if self.main_function:
                if self.args:
                    self.main_function(*self.args)
                else:
                    self.main_function()

    def text_change(self, new_text, new_color, new_font=None):
        self.button_text = new_text
        self.text_color = new_color
        self.font_for_text = new_font

    def default_function_for_button(self):
        pass

    def animation(self, key):
        self.is_animation_started = True
        while self.is_animation_started:
            self.font_size += key
            if self.outline_lenth:
                self.outline_lenth += key
            sleep(0.05)
            self.present_animation_frame += key
            if self.present_animation_frame >= self.animation_max_frame or not self.is_targeted(self.last_pos):
                self.is_animation_started = False
                return
            if self.present_animation_frame <= 0 or self.is_targeted(self.last_pos):
                self.is_animation_started = False
                return

    def target_animation(self):
        if self.normal_size and not self.is_animation_started:
            self.new_animation = Thread(target=self.animation, args=(1,))
            self.new_animation.start()
        elif self.bigger_size and not self.is_animation_started:
            self.new_animation = Thread(target=self.animation, args=(-1,))
            self.new_animation.start()


    def is_targeted(self, pos, animation=False):
        self.last_pos = pos
        if animation:
            if self.x_cord <= pos[0] <= self.x_cord + self.x_lenth and self.y_cord <= pos[1] <= self.y_cord + self.y_lenth:
                self.start_animation = True
                self.end_animation = False
            else:
                self.start_animation = False
                self.end_animation = True
            self.target_animation()

        return self.x_cord <= pos[0] <= self.x_cord + self.x_lenth and self.y_cord\
               <= pos[1] <= self.y_cord + self.y_lenth

    def draw(self, canvas):
        pygame.font.init()
        myfont = pygame.font.SysFont(self.font_for_text, self.font_size)
        if self.outline_lenth:
            pygame.draw.rect(canvas, self.color_of_outline, (self.x_cord - self.outline_lenth,
                                                             self.y_cord - self.outline_lenth,
                                                             self.x_lenth + self.outline_lenth * 2,
                                                             self.y_lenth + self.outline_lenth * 2))
        textsurface = myfont.render(self.button_text, False, self.text_color)
        pygame.draw.rect(canvas, self.background, (self.x_cord, self.y_cord, self.x_lenth, self.y_lenth))

        canvas.blit(textsurface, (self.x_cord + (self.x_lenth - myfont.size(self.button_text)[0]) // 2,
                                  self.y_cord + (self.y_lenth - myfont.size(self.button_text)[1])//2))


class TextButton(Button):
    def __init__(self, button_text, x_cord, y_cord, x_lenth, y_lenth, func=None, args=None, new_button_group=None,
                 text_color=(255, 0, 0), font_size=90, font_for_text="Lilita One Russian",
                 background=(75,85,255), backgroynd_tex=None, color_of_outline=None,
                 outline_lenth=None):
        super().__init__(button_text, x_cord, y_cord, x_lenth, y_lenth, func, args, new_button_group,
                 text_color, font_size, font_for_text,
                 background, backgroynd_tex, color_of_outline,
                 outline_lenth)

    def draw(self, canvas):
        pygame.font.init()
        myfont = pygame.font.SysFont(self.font_for_text, self.font_size)
        textsurface = myfont.render(self.button_text, False, self.text_color)


class InputField(Button):
    max_animation_frame = 30
    def __init__(self, x_cord, y_cord, x_lenth, y_lenth, font_for_text="Rockin' Record",
                 font_size=50, text_color=(255, 0, 0), initial_text='', func=None,
                 background=(155,155,155), input_is_active=True):
        self.x_cord, self.y_cord, self.x_lenth, self.y_lenth = x_cord, y_cord, x_lenth, y_lenth
        self.input_is_active = input_is_active
        self.font_size, self.font_for_text = font_size, font_for_text
        self.is_animation_started = False
        self.present_animation_frame = 0
        self.text_color = text_color
        self.background = background
        self.text = initial_text
        self.func = func
        self.is_separator = False
        self.now_position = len(self.text)
        self.is_upper = False

    def checker_for_upper_letter(self, event):
        if event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT]:
                self.is_upper = False

    def activate_input(self, event):
        if self.input_is_active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:self.now_position][:-1] + self.text[self.now_position:]
                self.now_position -= 1 if self.now_position >= 1 else 0
                if len(self.text) <= self.now_position:
                    self.now_position = len(self.text)
            elif event.key == pygame.K_DELETE:
                self.text = self.text[:self.now_position] + self.text[self.now_position:][1:]
                self.now_position -= 1 if self.now_position >= 1 else 0
                if len(self.text) <= self.now_position:
                    self.now_position = len(self.text)
            elif event.key == pygame.K_CLEAR:
                pass
            elif event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                if self.func:
                    self.thread = Thread(target=self.func, args=(self.text))
                    self.thread.start()
                self.input_is_active = False
            elif event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT]:
                self.is_upper = True
            elif event.key == pygame.K_LEFT:
                self.now_position -= 1 if self.now_position > 0 else 0
            elif event.key == pygame.K_RIGHT:
                self.now_position += 1 if self.now_position < len(self.text) else 0
            elif event.key == pygame.K_UP:
                self.now_position = 0
            elif event.key == pygame.K_DOWN:
                self.now_position = len(self.text)
            else:
                try:
                    self.text = self.text[:self.now_position] + chr(event.key).upper() + self.text[self.now_position:]\
                        if self.is_upper else self.text[:self.now_position]\
                                              + chr(event.key) + self.text[self.now_position:]
                    self.now_position  += 1
                except ValueError:
                    pass
                print(self.text, self.now_position)

    def is_pressed(self, pos):
        if super().is_targeted(pos):
            self.input_is_active = True
        else:
            self.input_is_active = False


    def draw(self, canvas):
        pygame.font.init()
        myfont = pygame.font.SysFont(self.font_for_text, self.font_size)
        textsurface = myfont.render(self.text, False, self.text_color)
        pygame.draw.rect(canvas, self.background, (self.x_cord, self.y_cord, self.x_lenth, self.y_lenth))
        canvas.blit(textsurface, (self.x_cord, self.y_cord + (self.y_lenth - myfont.size(self.text)[1]) // 2))
        if self.input_is_active:
            self.present_animation_frame += 1
            self.present_animation_frame %= self.max_animation_frame
            if self.present_animation_frame == 0:
                self.is_separator = not self.is_separator
            if self.is_separator:
                text_separator = myfont.render('|', False, (255, 255, 255))
                canvas.blit(text_separator, (self.x_cord + myfont.size(self.text[:self.now_position])[0],
                                          self.y_cord + (self.y_lenth - myfont.size(self.text)[1]) // 2))

    def __str__(self):
        return self.text


class ButtonGroup():
    def __init__(self, *buttons):
        self.buttons = buttons


class ScrollArea():
    pass

class TextViewer():
    def __init__(self, text, x_cord, y_cord, x_lenth, y_lenth,
                 text_color=(255, 0, 0), font_size=90, font_for_text="Lilita One Russian",
                 background=None, backgroynd_tex=None, color_of_outline=None,
                 outline_lenth=None):
        self.x_cord, self.y_cord, self.x_lenth, self.y_lenth = x_cord, y_cord, x_lenth, y_lenth
        self.text = text
        self.font_size, self.font_for_text = font_size, font_for_text
        self.text_color = text_color
        self.background = background

    def draw(self, canvas):
        pygame.font.init()
        myfont = pygame.font.SysFont(self.font_for_text, self.font_size)
        textsurface = myfont.render(self.text, False, self.text_color)
        if self.background:
            pygame.draw.rect(canvas, self.background, (self.x_cord, self.y_cord, self.x_lenth, self.y_lenth))
        canvas.blit(textsurface, (self.x_cord, self.y_cord + (self.y_lenth - myfont.size(self.text)[1]) // 2))