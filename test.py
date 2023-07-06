
import sqlite3
import pygame
import sys
import math
from UIComponents import Checkbox, Colors
pygame.init()
game_time = True
#Цвета
text_color = (75, 75, 75)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

clock = pygame.time.Clock()
time_seconds = 0
flag = 0
#БД
conn = sqlite3.connect('user.db')
cur = conn.cursor()

conn_skills =sqlite3.connect('Skills.db')
cur_skills = conn_skills.cursor()

#Размер окна
width = 800
height = 600

#Поля ввода
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.SysFont('courier', 20)


#Координаты кнопок
width_button_start = 300
height_button_start = 100
button_start_x = 250
button_start_y = 250

width_button_skills = 150
height_button_skills = 50
button_skills_x = 600
button_skills_y = 500

#флаги
forse = 0#сила
dexterity1 = 0#ловкость
dexterity2 = 0#ловкость
dexterity3 = 0#ловкость
intelligence1 = 0#интелект
intelligence2 = 0#интелект
intelligence3 = 0#интелект
intelligence4 = 0#интелект
intelligence5 = 0#интелект
wisdom1 = 0#мудрость
wisdom2 = 0#мудрость
wisdom3 = 0#мудрость
wisdom4 = 0#мудрость
wisdom5 = 0#мудрость
charisma1 = 0#харизма
charisma2 = 0#харизма
charisma3 = 0#харизма
charisma4 = 0#харизма

#создание окна
screen = pygame.display.set_mode((width, height))
icon = pygame.image.load("img/dnd_icon.png")
pygame.display.set_caption("DnD character assistant")
pygame.display.set_icon(icon)

class InputBox:

    def __init__(self, x, y, w , h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.flag = 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.flag = 1
                    start_screan()
                    screen.fill((0, 0, 0))
                    start_screan()
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    start_screan()
                    screen.fill((0, 0, 0))
                    start_screan()
                    pygame.display.update()
                else:
                    self.text += event.unicode
                    start_screan()
                    screen.fill((0, 0, 0))
                    start_screan()
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(self.rect.h, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.display.update()
        pygame.draw.rect(screen, self.color, self.rect, 2)


class Personal_card:
    def __init__ (self,):
        self.name_personal = ''
        self.class_personal = ''
        self.level_personal = 0
        self.race_personal = ''
        self.name_player = ''
        #характеристики
        self.forse = 0
        self.dexterity = 0
        self.endurance = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.slkill_bonus = 0
        self.passive_mindfulness = 0
#обработка кликов
a =5
def checked():
    if checkbox_acrobatics.checked:
        checkbox_acrobatics.text = a + 2
    else:
        checkbox_acrobatics.text = a

def first():
    data = "SELECT saving_throws_f from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def second():
    data = "SELECT saving_throws_s from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def col_skills():
    data = "SELECT col_skiils from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
colskils = 0

def check_acrobatics():
    data = "SELECT acrobatics from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def check_athletics():
    data = "SELECT athletics from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def check_attention():
    data = "SELECT attention from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def check_survival():
    data = "SELECT survival from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def check_training():
    data = "SELECT training from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def check_intimidation():
    data = "SELECT intimidation from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def check_execution():
    data = "SELECT execution from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def check_history():
    data = "SELECT history from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def check_dexteterity():
    data = "SELECT dexterity from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def check_magic():
    data = "SELECT magic from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def check_medicine():
    data = "SELECT medicine from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def check_deception():
    data = "SELECT deception from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def check_nature():
    data = "SELECT nature from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def check_insight():
    data = "SELECT insight from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def check_investigation():
    data = "SELECT investigation from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def check_religion():
    data = "SELECT religion from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def check_stealth():
    data = "SELECT stealth from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
def check_conviction():
    data = "SELECT conviction from play_class WHERE class = ?"
    cur.execute(data, (card.class_personal,))
    record = cur.fetchone()
    return record[0]
#вывод стартовоко текста по тамеру на scream
def text_start():
    f1 = pygame.font.SysFont('courier', 20)
    if time_seconds >= 1:
        text_st = f1.render(f"Вас приветствует программа DnD character assistant", False, (white))
        screen.blit(text_st, (0, 0))
        pygame.display.update()

    if time_seconds >= 2:
        text_st = f1.render(f"Для начала нажмите кнопку.", False, (white))
        screen.blit(text_st, (0, 30))
        pygame.display.update()

    if time_seconds >= 3:
        f1 = pygame.font.SysFont('courier', 33)
        text_st = f1.render(f"Итак начнем создавать персонажа для DnD!", False, (red))
        screen.blit(text_st, (0, 70))
        pygame.display.update()

    if time_seconds >= 4:
        f1 = pygame.font.SysFont('courier', 40)
        text_st = f1.render(f"START", False, (white))
        screen.blit(text_st, (335, 275))
        f1 = pygame.font.SysFont('courier', 20)
        text_st = f1.render(f"Работу выполнил Вагизов Р.Р.", False, (text_color))
        screen.blit(text_st, (450, 540))
        text_st = f1.render(f"Студента группы П2-20", False, (text_color))
        screen.blit(text_st, (450, 570))
        pygame.draw.rect(screen, white, (button_start_x, button_start_y, width_button_start, height_button_start), 10)
        if pygame.mouse.get_pos()[0] >= button_start_x and pygame.mouse.get_pos()[1] >= button_start_y:
            if pygame.mouse.get_pos()[0] <= button_start_x + width_button_start and pygame.mouse.get_pos()[1] <= button_start_y + height_button_start:
                pygame.draw.rect(screen, blue, (button_start_x, button_start_y, width_button_start, height_button_start), 10)
                f1 = pygame.font.SysFont('courier', 40)
                text_st = f1.render(f"START", False, (blue))
                screen.blit(text_st, (335, 275))
#Для верхне инфы
input_name_personal = InputBox(10, 70, 140, 32)
input_class_personal = InputBox(430, 70, 140, 32)
input_level_personal = InputBox(10, 140, 140, 32)
input_race_personal = InputBox(430, 140, 140, 32)
input_name_player = InputBox(10, 210, 140, 32)
input_boxes_card = [input_name_personal, input_name_player, input_class_personal, input_race_personal, input_level_personal]
#для характеристик
input_forse = InputBox(180, 305, 50, 32, "0")
input_dexterity = InputBox(180, 345 , 50, 32, "0")
input_endurance = InputBox(180, 385, 50, 32, "0")
input_intelligence = InputBox(180, 425, 50, 32, "0")
input_wisdom = InputBox(180, 465, 50, 32, "0")
input_charisma = InputBox(180, 505, 50, 32, "0")
input_boxes_characteristics = [input_charisma, input_wisdom, input_intelligence, input_endurance, input_dexterity, input_forse]
card = Personal_card()
point = 0
#для скилов
checkbox_acrobatics = Checkbox((10, 50, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)
checkbox_athletics = Checkbox((10, 90, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)
checkbox_attention = Checkbox((10, 130, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)
checkbox_survival = Checkbox((10, 170, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)
checkbox_training = Checkbox((10, 210, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)
checkbox_intimidation = Checkbox((10, 250, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)
checkbox_execution = Checkbox((10, 290, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)
checkbox_history = Checkbox((10, 330, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)
checkbox_dexterity = Checkbox((10, 370, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)
checkbox_magic = Checkbox((260, 50, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)
checkbox_medicine = Checkbox((260, 90, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)
checkbox_deception = Checkbox((260, 130, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)
checkbox_nature = Checkbox((260, 170, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)
checkbox_insight = Checkbox((260, 210, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)
checkbox_investigation = Checkbox((260, 250, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)
checkbox_religion = Checkbox((260, 290, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)
checkbox_stealth = Checkbox((260, 330, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)
checkbox_conviction = Checkbox((260, 370, 250, 20), Colors().white, Colors().red, 'Check Me!', click_function=checked)

def correspond():
    if input_name_personal.flag == 1:
        card.name_personal = input_name_personal.text
        input_name_personal.flag = 0

    if input_class_personal.flag == 1:
        card.class_personal = input_class_personal.text
        input_class_personal.flag = 0

    if input_level_personal.flag == 1:
        card.level_personal = input_level_personal.text
        input_level_personal.flag = 0

    if input_race_personal.flag == 1:
        card.race_personal = input_race_personal.text
        input_race_personal.flag = 0

    if input_name_player.flag == 1:
        card.name_player = input_name_player.text
        input_name_player.flag = 0

def correspond_characteristics():
    if input_dexterity.flag == 1 and input_dexterity.text != '':
        card.dexterity = int(input_dexterity.text)
        input_dexterity.flag = 0

    if input_forse.flag == 1 and input_forse.text != '':
        card.forse = int(input_forse.text)
        input_forse.flag = 0

    if input_endurance.flag == 1 and input_endurance.text != '':
        card.endurance = int(input_endurance.text)
        input_endurance.flag = 0

    if input_intelligence.flag == 1 and input_intelligence.text != '':
        card.intelligence = int(input_intelligence.text)
        input_intelligence.flag = 0

    if input_wisdom.flag == 1 and input_wisdom.text != '':
        card.wisdom = int(input_wisdom.text)
        input_wisdom.flag = 0

    if input_charisma.flag == 1 and input_charisma.text != '':
        card.charisma = int(input_charisma.text)
        input_charisma.flag = 0

def start_screan():
    if time_seconds >= 1:
        f1 = pygame.font.SysFont('courier', 20)
        text_st = f1.render(f"И так ты осмелился создать персонажа в днд, НАЧНЕМ:", False, (white))
        screen.blit(text_st, (0, 0))
        pygame.display.update()
    if time_seconds >= 2:
        f1 = pygame.font.SysFont('courier', 20)
        text_st = f1.render(f"Вля начала введем имя, класс, уровень, расу и имя игрока", False, (white))
        screen.blit(text_st, (0, 30))
        pygame.display.update()
    if time_seconds >= 3:
        f1 = pygame.font.SysFont('courier', 20)
        text_st = f1.render(f"Имя персонажа", False, (white))
        screen.blit(text_st, (10, 100))
        text_st = f1.render(f"Класс персонажа", False, (white))
        screen.blit(text_st, (430, 100))
        text_st = f1.render(f"Уровень", False, (white))
        screen.blit(text_st, (10, 170))
        text_st = f1.render(f"Раса", False, (white))
        screen.blit(text_st, (430, 170))
        text_st = f1.render(f"Имя игрока", False, (white))
        screen.blit(text_st, (10, 240))
        pygame.display.update()

    if point == 1 and time_seconds >= 4:
        f1 = pygame.font.SysFont('courier', 20)
        text_st = f1.render(f"Теперь нужно заполнить характеристики:", False, (white))
        screen.blit(text_st, (0, 280))
        text_st = f1.render(f"Сила:", False, (white))
        screen.blit(text_st, (10, 305))
        text_st = f1.render(f"Ловкость:", False, (white))
        screen.blit(text_st, (10, 345))
        text_st = f1.render(f"Телосложение:", False, (white))
        screen.blit(text_st, (10, 385))
        text_st = f1.render(f"Интелект:", False, (white))
        screen.blit(text_st, (10, 425))
        text_st = f1.render(f"Мудрость:", False, (white))
        screen.blit(text_st, (10, 465))
        text_st = f1.render(f"Харизма:", False, (white))
        screen.blit(text_st, (10, 505))
        text_st = f1.render(f"Бонус умения:", False, (white))
        screen.blit(text_st, (300, 310))
        if card.level_personal != '':
            card.slkill_bonus = (int (card.level_personal) // 4) + 2
            text_st = f1.render(f"{(int (card.level_personal) // 4) + 2}", False, (white))
        else:
            text_st = f1.render(f"ERROR", False, (white))
        screen.blit(text_st, (460, 310))
        text_st = f1.render(f"Пасивная внимание:", False, (white))
        screen.blit(text_st, (300, 340))
        if input_wisdom.text != '':
            text_st = f1.render(f"{ 8 + card.slkill_bonus + (int(input_wisdom.text) - 10) // 2}", False, (white))
        else:
            text_st = f1.render(f"ERROR", False, (white))
        screen.blit(text_st, (520, 340))
        text_st = f1.render(f"Инициатива:", False, (white))
        screen.blit(text_st, (300, 360))
        if input_dexterity.text != '':
            text_st = f1.render(f"{(int(input_dexterity.text) - 10) // 2}", False, (white))
        else:
            text_st = f1.render(f"ERROR", False, (white))
        screen.blit(text_st, (520, 360))
        if input_forse.text != '':
            text_st = f1.render(f"{(int(input_forse.text) - 10) // 2}", False, (white))
        else:
            text_st = f1.render(f"ERROR", False, (white))
        screen.blit(text_st, (230, 310))
        if input_dexterity.text != '':
            text_st = f1.render(f"{(int(input_dexterity.text) - 10) // 2}", False, (white))
        else:
            text_st = f1.render(f"ERROR", False, (white))
        screen.blit(text_st, (230, 350))
        if input_endurance.text != '':
            text_st = f1.render(f"{(int(input_endurance.text) - 10) // 2}", False, (white))
        else:
            text_st = f1.render(f"ERROR", False, (white))
        screen.blit(text_st, (230, 390))
        if input_intelligence.text != '':
            text_st = f1.render(f"{(int(input_intelligence.text) - 10) // 2}", False, (white))
        else:
            text_st = f1.render(f"ERROR", False, (white))
        screen.blit(text_st, (230, 430))
        if input_wisdom.text != '':
            text_st = f1.render(f"{(int(input_wisdom.text) - 10) // 2}", False, (white))
        else:
            text_st = f1.render(f"ERROR", False, (white))
        screen.blit(text_st, (230, 470))
        if input_charisma.text != '':
            text_st = f1.render(f"{(int(input_charisma.text) - 10) // 2}", False, (white))
        else:
            text_st = f1.render(f"ERROR", False, (white))
        screen.blit(text_st, (230, 510))

        f1 = pygame.font.SysFont('courier', 20)
        text_st = f1.render(f"Испытания:", False, (white))
        screen.blit(text_st, (300, 400))
        text_st = f1.render(f"Сила:", False, (white))
        screen.blit(text_st, (300, 420))
        text_st = f1.render(f"Ловкость:", False, (white))
        screen.blit(text_st, (300, 440))
        text_st = f1.render(f"Телосложение:", False, (white))
        screen.blit(text_st, (300, 460))
        text_st = f1.render(f"Интелект:", False, (white))
        screen.blit(text_st, (300, 480))
        text_st = f1.render(f"Мудрость:", False, (white))
        screen.blit(text_st, (300, 500))
        text_st = f1.render(f"Харизма:", False, (white))
        screen.blit(text_st, (300, 520))

        f2 = pygame.font.SysFont('courier', 20)
        text_st = f2.render(f"NEXT", False, (white))
        screen.blit(text_st, (650, 515))
        pygame.draw.rect(screen, white, (button_skills_x, button_skills_y, width_button_skills, height_button_skills), 5)
        if pygame.mouse.get_pos()[0] >= button_skills_x and pygame.mouse.get_pos()[1] >= button_skills_y:
            if pygame.mouse.get_pos()[0] <= button_skills_x + width_button_skills and pygame.mouse.get_pos()[
                1] <= button_skills_y + height_button_skills:
                pygame.draw.rect(screen, blue,(button_skills_x, button_skills_y, width_button_skills, height_button_skills), 5)
                f2 = pygame.font.SysFont('courier', 20)
                text_st = f2.render(f"NEXT", False, (blue))
                screen.blit(text_st, (650, 515))


        if input_forse.text != '':
            if first() == 1 or second() == 1:
                text_st = f1.render(f"{((int(input_forse.text) - 10) // 2) + card.slkill_bonus}", False, (white))
                card.forse = ((int(input_forse.text) - 10) // 2)
            else:
                text_st = f1.render(f"{(int(input_forse.text) - 10) // 2}", False, (white))
                card.forse = (int(input_forse.text) - 10) // 2
        else:
            text_st = f1.render(f"ERROR", False, (white))
        screen.blit(text_st, (500, 420))

        if input_dexterity.text != '':
            if first() == 2 or second() == 2:
                text_st = f1.render(f"{((int(input_dexterity.text) - 10) // 2) + card.slkill_bonus}", False, (white))
                card.dexterity = ((int(input_dexterity.text) - 10) // 2)
            else:
                text_st = f1.render(f"{(int(input_dexterity.text) - 10) // 2}", False, (white))
                card.dexterity = (int(input_dexterity.text) - 10) // 2
        else:
            text_st = f1.render(f"ERROR", False, (white))
        screen.blit(text_st, (500, 440))

        if input_endurance.text != '':
            if first() == 3 or second() == 3:
                text_st = f1.render(f"{((int(input_endurance.text) - 10) // 2) + card.slkill_bonus}", False, (white))
                card.endurance = ((int(input_endurance.text) - 10) // 2)
            else:
                text_st = f1.render(f"{(int(input_endurance.text) - 10) // 2}", False, (white))
                card.endurance = (int(input_endurance.text) - 10) // 2
        else:
            text_st = f1.render(f"ERROR", False, (white))
        screen.blit(text_st, (500, 460))

        if input_intelligence.text != '':
            if first() == 4 or second() == 4:
                text_st = f1.render(f"{((int(input_intelligence.text) - 10) // 2) + card.slkill_bonus}", False, (white))
                card.intelligence = ((int(input_intelligence.text) - 10) // 2)
            else:
                text_st = f1.render(f"{(int(input_intelligence.text) - 10) // 2}", False, (white))
                card.intelligence = (int(input_intelligence.text) - 10) // 2
        else:
            text_st = f1.render(f"ERROR", False, (white))
        screen.blit(text_st, (500, 480))

        if input_wisdom.text != '':
            if first() == 5 or second() == 5:
                text_st = f1.render(f"{((int(input_wisdom.text) - 10) // 2) + card.slkill_bonus}", False, (white))
                card.wisdom = ((int(input_wisdom.text) - 10) // 2)
            else:
                text_st = f1.render(f"{(int(input_wisdom.text) - 10) // 2}", False, (white))
                card.wisdom = (int(input_wisdom.text) - 10) // 2
        else:
            text_st = f1.render(f"ERROR", False, (white))
        screen.blit(text_st, (500, 500))

        if input_charisma.text != '':
            if first() == 6 or second() == 6:
                text_st = f1.render(f"{((int(input_charisma.text) - 10) // 2) + card.slkill_bonus}", False, (white))
                card.charisma = ((int(input_charisma.text) - 10) // 2)
            else:
                text_st = f1.render(f"{(int(input_charisma.text) - 10) // 2}", False, (white))
                card.charisma = (int(input_charisma.text) - 10) // 2
        else:
            text_st = f1.render(f"ERROR", False, (white))
        screen.blit(text_st, (500, 520))

        pygame.display.update()
def skills_screan():
    if time_seconds >= 1:
        f1 = pygame.font.SysFont('courier', 20)
        text_st = f1.render(f"Далее мы распрделим скилы и узнаем что умеет твой персонаж:", False, (white))
        screen.blit(text_st, (0, 0))
        pygame.display.update()
    if time_seconds >= 2:

        #inf_skills()
        #print(arr_skills)
        if check_acrobatics() == 1:
            checkbox_acrobatics.draw(screen)

        if check_athletics() == 1:
            checkbox_athletics.draw(screen)

        if check_attention() == 1:
            checkbox_attention.draw(screen)

        if check_survival() == 1:
            checkbox_survival.draw(screen)

        if check_training() == 1:
            checkbox_training.draw(screen)

        if check_intimidation() == 1:
            checkbox_intimidation.draw(screen)

        if check_execution() == 1:
            checkbox_execution.draw(screen)

        if check_history() == 1:
            checkbox_history.draw(screen)

        if check_dexteterity() == 1:
            checkbox_dexterity.draw(screen)

        if check_magic() == 1:
            checkbox_magic.draw(screen)

        if check_medicine() == 1:
            checkbox_medicine.draw(screen)

        if check_deception() == 1:
            checkbox_deception.draw(screen)

        if check_nature() == 1:
            checkbox_nature.draw(screen)

        if check_insight() == 1:
            checkbox_insight.draw(screen)

        if check_intimidation() == 1:
            checkbox_investigation.draw(screen)

        if check_religion() == 1:
            checkbox_religion.draw(screen)

        if check_stealth() == 1:
            checkbox_stealth.draw(screen)

        if check_conviction() == 1:
            checkbox_conviction.draw(screen)

        f1 = pygame.font.SysFont('courier', 20)
        text_st = f1.render(f"Акробатика: {card.dexterity + dexterity1}", False, (white))
        screen.blit(text_st, (50, 50))
        text_st = f1.render(f"Атлетика: {card.forse + forse}", False, (white))
        screen.blit(text_st, (50, 90))
        text_st = f1.render(f"Внимание: {card.wisdom + wisdom1}", False, (white))
        screen.blit(text_st, (50, 130))
        text_st = f1.render(f"Выживание: {card.wisdom + wisdom2}", False, (white))
        screen.blit(text_st, (50, 170))
        text_st = f1.render(f"Дрессировка: {card.wisdom + wisdom3}", False, (white))
        screen.blit(text_st, (50, 210))
        text_st = f1.render(f"Запугивание:  {card.charisma + charisma1}", False, (white))
        screen.blit(text_st, (50, 250))
        text_st = f1.render(f"Исполнение: {card.charisma + charisma2}", False, (white))
        screen.blit(text_st, (50, 290))
        text_st = f1.render(f"История: {card.intelligence + intelligence1}", False, (white))
        screen.blit(text_st, (50, 330))
        text_st = f1.render(f"Ловкость рук: {card.dexterity + dexterity2}", False, (white))
        screen.blit(text_st, (50, 370))
        text_st = f1.render(f"Магия: {card.intelligence + intelligence2}", False, (white))
        screen.blit(text_st, (300, 50))
        text_st = f1.render(f"Медицина: {card.wisdom + wisdom4}", False, (white))
        screen.blit(text_st, (300, 90))
        text_st = f1.render(f"Обман: {card.charisma + charisma3}", False, (white))
        screen.blit(text_st, (300, 130))
        text_st = f1.render(f"Природа: {card.intelligence + intelligence3}", False, (white))
        screen.blit(text_st, (300, 170))
        text_st = f1.render(f"Проницательность: {card.wisdom + wisdom5}", False, (white))
        screen.blit(text_st, (300, 210))
        text_st = f1.render(f"Расследование: {card.intelligence + intelligence4}", False, (white))
        screen.blit(text_st, (300, 250))
        text_st = f1.render(f"Религия: {card.intelligence + intelligence5}", False, (white))
        screen.blit(text_st, (300, 290))
        text_st = f1.render(f"Скрытность: {card.dexterity + dexterity3}", False, (white))
        screen.blit(text_st, (300, 330))
        text_st = f1.render(f"Убеждение: {card.charisma + charisma4}", False, (white))
        screen.blit(text_st, (300, 370))

        f1 = pygame.font.SysFont('courier', 25)
        text_st = f1.render(f"У вас осталось не распределенных очнов навыков: {colskils}", False, (white))
        screen.blit(text_st, (10, 400))
        pygame.display.update()

def button_start_click():
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if pygame.mouse.get_pos()[0] >= button_start_x  and pygame.mouse.get_pos()[1] >= button_start_y and pygame.mouse.get_pos()[0] <= button_start_x + width_button_start and pygame.mouse.get_pos()[1] <= button_start_y + height_button_start:
                return True
def button_skills_click():
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if pygame.mouse.get_pos()[0] >= button_skills_x  and pygame.mouse.get_pos()[1] >= button_skills_y and pygame.mouse.get_pos()[0] <= button_skills_x + width_button_skills and pygame.mouse.get_pos()[1] <= button_skills_y + height_button_skills:
                return True
#Цикл отрисовки
number_screan = 1
while game_time:
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            game_time = False

        elif event.type == pygame.MOUSEBUTTONDOWN and number_screan == 3:
            if checkbox_acrobatics.clicked(pygame.mouse.get_pos()) and check_acrobatics() == 1 :
                if dexterity1 == 0  and colskils > 0:
                    dexterity1 = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif dexterity1 == card.slkill_bonus:
                    dexterity1 = 0
                    colskils +=1
                    screen.fill((black))
            if checkbox_athletics.clicked(pygame.mouse.get_pos()) and check_athletics() == 1 :
                if forse == 0 and colskils > 0:
                    forse = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif forse == card.slkill_bonus:
                    forse = 0
                    colskils += 1
                    screen.fill((black))
            if checkbox_attention.clicked(pygame.mouse.get_pos()) and check_attention() == 1:
                if wisdom1 == 0 and colskils > 0:
                    wisdom1 = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif wisdom1 == card.slkill_bonus:
                    wisdom1 = 0
                    colskils += 1
                    screen.fill((black))
            if checkbox_survival.clicked(pygame.mouse.get_pos()) and check_survival() == 1:
                if wisdom2 == 0 and colskils > 0:
                    wisdom2 = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif wisdom2 == card.slkill_bonus:
                    wisdom2 = 0
                    colskils += 1
                    screen.fill((black))
            if checkbox_training.clicked(pygame.mouse.get_pos()) and check_training() == 1:
                if wisdom3 == 0 and colskils > 0:
                    wisdom3 = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif wisdom3 == card.slkill_bonus:
                    wisdom3 = 0
                    colskils += 1
                    screen.fill((black))
            if checkbox_intimidation.clicked(pygame.mouse.get_pos()) and check_intimidation() == 1:
                if charisma1 == 0 and colskils > 0:
                    charisma1 = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif charisma1 == card.slkill_bonus:
                    charisma1 = 0
                    colskils += 1
                    screen.fill((black))
            if checkbox_execution.clicked(pygame.mouse.get_pos()) and check_execution() == 1:
                if charisma2 == 0 and colskils > 0:
                    charisma2 = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif charisma2 == card.slkill_bonus:
                    charisma2 = 0
                    colskils += 1
                    screen.fill((black))
            if checkbox_history.clicked(pygame.mouse.get_pos()) and check_history() == 1:
                if intelligence1 == 0 and colskils > 0:
                    intelligence1 = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif intelligence1 == card.slkill_bonus:
                    intelligence1 = 0
                    colskils += 1
                    screen.fill((black))
            if checkbox_dexterity.clicked(pygame.mouse.get_pos()) and check_dexteterity() == 1:
                if dexterity2 == 0 and colskils > 0:
                    dexterity2 = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif dexterity2 == card.slkill_bonus:
                    dexterity2 = 0
                    colskils += 1
                    screen.fill((black))
            if checkbox_magic.clicked(pygame.mouse.get_pos()) and check_magic() == 1:
                if intelligence2 == 0 and colskils > 0:
                    intelligence2 = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif intelligence2 == card.slkill_bonus:
                    intelligence2 = 0
                    colskils += 1
                    screen.fill((black))
            if checkbox_medicine.clicked(pygame.mouse.get_pos()) and check_medicine() == 1 :
                if wisdom4 == 0 and colskils > 0:
                    wisdom4 = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif wisdom4 == card.slkill_bonus:
                    wisdom4 = 0
                    colskils += 1
                    screen.fill((black))
            if checkbox_deception.clicked(pygame.mouse.get_pos()) and check_deception() == 1 :
                if charisma3 == 0 and colskils > 0:
                    charisma3 = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif charisma3 == card.slkill_bonus:
                    charisma3 = 0
                    colskils += 1
                    screen.fill((black))
            if checkbox_nature.clicked(pygame.mouse.get_pos()) and check_nature() == 1 :
                if intelligence3 == 0 and colskils > 0:
                    intelligence3 = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif intelligence3 == card.slkill_bonus:
                    intelligence3 = 0
                    colskils += 1
                    screen.fill((black))
            if checkbox_insight.clicked(pygame.mouse.get_pos()) and check_insight() == 1 :
                if wisdom5 == 0 and colskils > 0:
                    wisdom5 = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif wisdom5 == card.slkill_bonus:
                    wisdom5 = 0
                    colskils += 1
                    screen.fill((black))
            if checkbox_investigation.clicked(pygame.mouse.get_pos()) and check_investigation() == 1 :
                if intelligence4 == 0 and colskils > 0:
                    intelligence4 = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif intelligence4 == card.slkill_bonus:
                    intelligence4 = 0
                    colskils += 1
                    screen.fill((black))
            if checkbox_religion.clicked(pygame.mouse.get_pos()) and check_religion() == 1  :
                if intelligence5 == 0 and colskils > 0:
                    intelligence5 = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif intelligence5 == card.slkill_bonus:
                    intelligence5 = 0
                    colskils += 1
                    screen.fill((black))
            if checkbox_stealth.clicked(pygame.mouse.get_pos()) and check_stealth() == 1 :
                if dexterity3 == 0 and colskils > 0:
                    dexterity3 = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif dexterity3 == card.slkill_bonus:
                    dexterity3 = 0
                    colskils += 1
                    screen.fill((black))
            if checkbox_conviction.clicked(pygame.mouse.get_pos()) and check_conviction() == 1 :
                if charisma4 == 0 and colskils > 0:
                    charisma4 = card.slkill_bonus
                    colskils -= 1
                    screen.fill((black))
                elif charisma4 == card.slkill_bonus:
                    charisma4 = 0
                    colskils += 1
                    screen.fill((black))
        for box in input_boxes_card:
            box.handle_event(event)
        for box in input_boxes_characteristics:
            box.handle_event(event)

    time_millis = clock.tick(30)
    time_str = str(int(time_seconds * 10) / 10)
    time_seconds += time_millis / 1000
    if number_screan == 1:
        text_start()
        if button_start_click():
            screen.fill((black))
            time_seconds = 0
            number_screan = 2

    if number_screan == 2:
        start_screan()
        if time_seconds >= 3:
            for box in input_boxes_card:
                box.update()
            for box in input_boxes_card:
                box.draw(screen)
        if point == 1:
            for box in input_boxes_characteristics:
                box.update()
            for box in input_boxes_characteristics:
                box.draw(screen)
        if button_skills_click():
            screen.fill((black))
            time_seconds = 0
            colskils = col_skills()
            number_screan = 3

    if number_screan == 3:
        skills_screan()

    correspond()
    if card.name_personal != ''  and card.level_personal != '' and card.class_personal != '' and card.race_personal != '' and card.name_player != '':
        point = 1
    correspond_characteristics()

    #pygame.display.flip()
    pygame.display.update()
    pygame.display.flip()
pygame.quit()




