import pygame
import sys

# Обязательная строчка во всех программах - играх, для подготовки модулей к работе
pygame.init()

def Menu1():
    # загрузили изображение
    Menu1_surf = pygame.image.load('tiles\\Menu1.png')
    # Передали изображение в дисплей
    screen.blit(Menu1_surf, (0, 0))
# ----------------------------------------------Задание текста----------------------------------------------------------
    # Белый цвет
    color = (255, 255, 255)
    # светлый оттенок кнопки
    color_light = (170, 170, 170)
    # темный оттенок кнопки при нажатии
    color_dark = (100, 100, 100)
    # Настройки шрифта кнопки
    smallfont = pygame.font.SysFont('Times New Roman', 35)
    # Рендеринг текста с параметрами, опсианными выше
    text = smallfont.render('Выход', True, color)
# ----------------------------------------------------------------------------------------------------------------------
    while True:
        # Записываем в массив mouse_pos координаты (x, y) курсора
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Завершаем работу модулей
                pygame.quit()
                # заврешаем работу программы
                sys.exit()
            # Проверяет нажата ли кнопка мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Если кнопка мыши нажата по координатам в условии, мы завершаем игру
                if width / 2 - 25 <= mouse_pos[0] <=width / 2 + 20 and height /2 + 140 <= mouse_pos[1] <= height/2 + 200:
                    # Завершаем работу модулей
                    pygame.quit()
                    # заврешаем работу программы
                    sys.exit()
                if width / 2 - 50 <= mouse_pos[0] <=width / 2 + 20 and height / 2 <= mouse_pos[1] <= height / 2 + 50:
                    Settings()
            # ----------------- Если курсор наведен на текст, он меняет свой оттенок -----------------------------------
            if width / 2 - 25 <= mouse_pos[0] <= width /2 + 20 and height / 2 + 140 <= mouse_pos[1] <= height / 2 + 200:
                color_exit = color_dark
            else:
                color_exit = color_light
            if width / 2 - 50 <= mouse_pos[0] <= width / 2 + 20 and height / 2 <= mouse_pos[1] <= height / 2 + 50:
                color_settings = color_dark
            else:
                color_settings = color_light
            # ----------------------------------------------------------------------------------------------------------
            # Рендеринг текста с параметрами, опсианными выше
            Exit = smallfont.render('Exit', True, color_exit)
            # Рендеринг текста с параметрами, опсианными выше
            goto_settings = smallfont.render('Settings', True, color_settings)
            # Наложение текста на кнопку
            screen.blit(Exit, (width / 2 - 25, height / 2 + 150))
            screen.blit(goto_settings, (width / 2 - 50, height / 2))
            # Обновили дисплей
            pygame.display.update()

def Game():
    # загрузили изображение
    Menu1_surf = pygame.image.load('tiles\\Game.png')
    # Передали изображение в дисплей
    screen.blit(Menu1_surf, (0, 0))


def Loose():
    # загрузили изображение
    Menu1_surf = pygame.image.load('tiles\\Loose.png')
    # Передали изображение в дисплей
    screen.blit(Menu1_surf, (0, 0))


def Menu2():
    # загрузили изображение
    Menu1_surf = pygame.image.load('tiles\\Menu2.png')
    # Передали изображение в дисплей
    screen.blit(Menu1_surf, (0, 0))


def Settings():
    # загрузили изображение
    Menu1_surf = pygame.image.load('tiles\\Settings.png')
    # Передали изображение в дисплей
    screen.blit(Menu1_surf, (0, 0))

# Создаем окно screen с разрешением - 1280х720
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

# ----------------------------------------------Задание текста----------------------------------------------------------
# Белый цвет
#color = (255, 255, 255)
# светлый оттенок кнопки
#color_light = (170, 170, 170)
# темный оттенок кнопки при нажатии
#color_dark = (100, 100, 100)
# Настройки шрифта кнопки
#smallfont = pygame.font.SysFont('Times New Roman', 35)
# Рендеринг текста с параметрами, опсианными выше
#text = smallfont.render('Mytext', True, color)
# ----------------------------------------------------------------------------------------------------------------------
Menu1()