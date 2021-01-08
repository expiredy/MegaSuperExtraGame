import pygame


class Button():
    button_group = None
    animation_max_frame = 15
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
        self.font_for_text, self.font_size = font_for_text, font_size

    def is_pressed(self, pos):
        if self.is_targeted(pos):
            print('Scanner of mouse deteced a fricking click')
            if self.main_function:
                if self.args:
                    self.main_function(*self.args)
                else:
                    self.main_function()

    def text_change(self, new_text, new_color, new_font=None):
        pass

    def default_function_for_button(self):
        pass

    def target_animation(self):
        if self.is_animation_started and self.present_animation_frame < self.animation_max_frame:
                self.present_animation_frame += 1
                self.font_size += 1
        if not self.is_animation_started and self.present_animation_frame > 0:
            self.present_animation_frame -= 1
            self.font_size -= 1

    def is_targeted(self, pos):
        if self.x_cord <= pos[0] <= self.x_cord + self.x_lenth and self.y_cord <= pos[1] <= self.y_cord + self.y_lenth:
            self.is_animation_started = True
            return True
        else:
            self.target_animation()
            self.is_animation_started = False
            return False

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
        canvas.blit(textsurface, (self.x_cord + (self.x_lenth - myfont.size(self.button_text)[0]) // 2,
                                  self.y_cord + (self.y_lenth - myfont.size(self.button_text)[1]) // 2))


class InputField(Button):
    def __init__(self, x_cord, y_cord, x_lenth, y_lenth, font_for_text="Rockin' Record", text_color=(255, 0, 0),
                 background=(0,0,0), input_is_active=True):
        self.x_cord, self.y_cord, self.x_lenth, self.y_lenth = x_cord, y_cord, x_lenth, y_lenth
        self.input_is_active = input_is_active

    def activate_input():
        pass

    def is_pressed(self, pos):
        if super().is_targeted(pos):
            self.input_is_active = True
        else:
            self.input_is_active = False


    def draw(self, canvas):
        pygame.draw.rect(canvas, self.background, (self.x_cord, self.y_cord, self.x_lenth, self.y_lenth))

class ButtonGroup():
    def __init__(self, *buttons):
        self.buttons = buttons