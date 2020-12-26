import pygame


class Button():
    button_group = None
    def __init__(self, button_text, x_cord, y_cord, x_lenth, y_lenth, func=None, new_button_group=None,
                 text_color=(255, 0, 0), background=(55,55,255), backgroynd_tex=None, color_of_outline=None,
                 outline_lenth=None):
        self.button_text = str(button_text)
        self.x_cord, self.y_cord, self.x_lenth, self.y_lenth = x_cord, y_cord, x_lenth, y_lenth
        self.color_of_outline, self.outline_lenth = color_of_outline, outline_lenth
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
        if func:
            self.main_function = func
        self.text_color = text_color
        self.background = background if not backgroynd_tex else backgroynd_tex


    def is_pressed(self, pos):
        if self.is_targeted(pos):
            print('Scanner of mouse deteced a fricking click')
            self.main_function()


    def add_to_dict(self):
        pass

    def text_change(self, new_text):
        pass

    def default_function_for_button(self):
        pass

    def target_animation(self):
        pass

    def is_targeted(self, pos):
        if self.x_cord <= pos[0] <= self.x_cord + self.x_lenth and self.y_cord <= pos[1] <= self.y_cord + self.y_lenth:
            return True
        return False

    def draw(self, canvas):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(self.button_text, False, self.text_color)
        pygame.draw.rect(canvas, self.background, (self.x_cord, self.y_cord, self.x_cord + self.x_lenth,
                                                 self.y_cord + self.y_lenth))
        if self.outline_lenth:
            pygame.draw.rect(canvas, self.color_of_outline,  (self.x_cord, self.y_cord, self.x_cord + self.x_lenth,
                                                 self.y_cord + self.y_lenth), self.outline_lenth)
        canvas.blit(textsurface, (self.x_cord, self.y_cord))


class ButtonGroup():
    def __init__(self, *buttons):
        self.buttons = buttons