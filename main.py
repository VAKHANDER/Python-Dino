import pygame
import sys
from random import randint

# Обязательная строчка во всех программах - играх, для подготовки модулей к работе
pygame.init()

def Menu1(width, height):
    # загрузили изображение
    Menu1_surf = pygame.image.load('tiles\\Menu1.png')
    # Передали изображение в дисплей
    screen.blit(Menu1_surf, (0, 0))
# ----------------------------------------------Задание текста----------------------------------------------------------
    # светлый оттенок кнопки
    color_light = (170, 170, 170)
    # темный оттенок кнопки при нажатии
    color_dark = (100, 100, 100)
    # Настройки шрифта кнопки
    smallfont = pygame.font.SysFont('Times New Roman', 35)
    # Рендеринг текста с параметрами, опсианными выше
    text = smallfont.render('Выход', True, color_light)
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
                    # загрузили изображение
                    tmp_surf = pygame.image.load('tiles\\tmp.png')
                    # Передали изображение в дисплей
                    screen.blit(tmp_surf, (0, 0))
                    Settings(width, height)
                    screen.blit(Menu1_surf, (0, 0))
                if width / 2 - 25 <= mouse_pos[0] <= width/2 + 20 and height /2 - 160 <= mouse_pos[1] <= height/2 - 100:
                    # Завершаем работу модулей
                    tmp_surf = pygame.image.load('tiles\\tmp.png')
                    screen.blit(tmp_surf, (0, 0))
                    Game()
                    screen.blit(Menu1_surf, (0, 0))
            # ----------------- Если курсор наведен на текст, он меняет свой оттенок -----------------------------------
            if width / 2 - 25 <= mouse_pos[0] <= width /2 + 20 and height / 2 + 140 <= mouse_pos[1] <= height / 2 + 200:
                color_exit = color_dark
            else:
                color_exit = color_light
            if width / 2 - 50 <= mouse_pos[0] <= width / 2 + 20 and height / 2 <= mouse_pos[1] <= height / 2 + 50:
                color_settings = color_dark
            else:
                color_settings = color_light
            if width / 2 - 25 <= mouse_pos[0] <= width /2 + 20 and height / 2 - 160 <= mouse_pos[1] <= height / 2 - 100:
                color_play = color_dark
            else:
                color_play = color_light
            # ----------------------------------------------------------------------------------------------------------
            # Рендеринг текста с параметрами, опсианными выше
            Exit = smallfont.render('Exit', True, color_exit)
            Play = smallfont.render('Play', True, color_play)
            goto_settings = smallfont.render('Settings', True, color_settings)
            # Закидываем объект с текстом на экран
            screen.blit(Play, (width / 2 - 25, height /2 - 150))
            screen.blit(Exit, (width / 2 - 25, height / 2 + 150))
            screen.blit(goto_settings, (width / 2 - 50, height / 2))
            # Обновили дисплей
            pygame.display.update()

def Game():
    # загрузили изображение
    Game_surf1 = pygame.image.load('tiles\\Game\\Background.png')
    Game_surf2 = pygame.image.load('tiles\\Game\\Background2.png')
    Dino = pygame.image.load('tiles\\Game\\Dino1.png')
    Kaktus1 = pygame.image.load('tiles\\Game\\Kaktus1.png')
    Kaktus2 = pygame.image.load('tiles\\Game\\Kaktus2.png')
    Kaktus3 = pygame.image.load('tiles\\Game\\Kaktus3.png')
    tmp = pygame.image.load('tiles\\Game\\tmp.png')
    kaktus = 0
    color_light = (170, 170, 170)
    Score_text = pygame.font.SysFont('Times New Roman', 35)
    x1 = 0
    x2 = 1280
    score = 0
    y_dino = 480
    speed = 5
    flag = 0
    # Передали изображение в дисплей
    screen.blit(Game_surf1, (x1, 0))
    screen.blit(Game_surf2, (x2, 0))
    screen.blit(Dino, (100, y_dino))
    FPS = pygame.time.Clock()
    # Количество fps
    fps = 75
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Завершаем работу модулей
                pygame.quit()
                # заврешаем работу программы
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flag = 80
                if event.key == pygame.K_ESCAPE:
                    Menu2()
        screen.blit(Game_surf1, (x1, 0))
        screen.blit(Game_surf2, (x2, 0))
        screen.blit(Dino, (100, y_dino))
        if kaktus == 1:
            screen.blit(Kaktus1, (x1, 480))
            if x1 < -1280:
                kaktus = 0
        elif kaktus == 2:
            screen.blit(Kaktus2, (x1, 480))
            kaktus = 0
            if x1 < -1280:
                kaktus = 0
        elif kaktus == 3:
            screen.blit(Kaktus3, (x1, 480))
            if x1 < -1280:
                kaktus = 0
        score2 = Score_text.render(str(int(score//100)), True, color_light)
        screen.blit(score2, (height/2 + 800, width/2 - 600))
        # Реализация прыжка
        if flag != 0:
            if flag > 40:
                y_dino = y_dino - 4
            elif flag < 41:
                if y_dino > 480 or y_dino != 480:
                    y_dino = y_dino + 4
            flag = flag - 1
        if flag == 0:
            y_dino = 480
        if x1 < -1280:
            x1 = 1280
            # Надо стереть задний фон, чтобы убрать старые кактусы
            Game_surf1.blit(tmp, (x1, 0))
        if x2 < -1280:
            x2 = 1280
        x1 = x1 - speed
        x2 = x2 - speed
        score = score + speed
        if (130 == x1 - 25):
            print(1)
            print((175 == x1 - 25))
            print(y_dino <= 455)
            if y_dino >= 455:
                print("True, x1 - 25 = ", x1, "; y_dino =", y_dino)
                Loose()
        elif (60 <= x1 + 25) and (130 >= x1 - 25):
            print(2)
            print((60 <= x1 + 25))
            print(y_dino >= 455)
            if y_dino >= 455:
                print("True, x1 + 25 = ", x1, "; y_dino =", y_dino)
                Loose()
        if score % 1000 == 0:
            speed = speed + 0.5
        # Разобрать со спавном кактусов
        if (score + speed) % 500 == 0 or speed % 500 == 0 or score % 500 == 0 and kaktus == 0:
            kaktus = randint(1, 3)
            print("kaktus = ", kaktus)
        FPS.tick(fps)
        pygame.display.update()


def Loose():
    # загрузили изображение
    Menu1_surf = pygame.image.load('tiles\\Loose.png')
    # Передали изображение в дисплей
    screen.blit(Menu1_surf, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Завершаем работу модулей
                pygame.quit()
                # заврешаем работу программы
                sys.exit()
            if event.type == pygame.KEYDOWN:
                Menu1(width, height)


def Menu2():
    # загрузили изображение
    Menu1_surf = pygame.image.load('tiles\\Menu2.png')
    # Передали изображение в дисплей
    screen.blit(Menu1_surf, (0, 0))
    pygame.display.update()
    color_light = (170, 170, 170)
    # темный оттенок кнопки при нажатии
    color_dark = (100, 100, 100)
    smallfont = pygame.font.SysFont('Times New Roman', 35)
    mouse_pos = []
    while True:
        screen.blit(Menu1_surf, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (width/2 + 40 >= mouse_pos[0] >= width/2 - 80) and (height/2 - 90 >= mouse_pos[1] >= height/2 - 140):
                    return
                elif (width/2 + 50 >= mouse_pos[0] >= width/2 - 70) and (height/2 + 30 >= mouse_pos[1] >= height/2 -20):
                    Settings(width, height)
                elif (width/2 + 80 >= mouse_pos[0] >= width/2 - 40) and (height/2 + 150>=mouse_pos[1]>=height/2 + 100):
                    Menu1(width, height)
        if (width/2 + 40 >= mouse_pos[0] >= width/2 - 80) and (height/2 - 90 >= mouse_pos[1] >= height/2 - 140):
            color_continue = color_dark
        else:
            color_continue = color_light
        if (width/2 + 50 >= mouse_pos[0] >= width/2 - 70) and (height/2 + 30 >= mouse_pos[1] >= height/2 -20):
            color_setting = color_dark
        else:
            color_setting = color_light
        if (width/2 + 80 >= mouse_pos[0] >= width/2 - 40) and (height/2 + 150 >= mouse_pos[1] >= height/2 + 100):
            color_exit = color_dark
        else:
            color_exit = color_light
        Continue = smallfont.render("continue", True, color_continue)
        Setting = smallfont.render("settings", True, color_setting)
        Exit = smallfont.render("exit", True, color_exit)
        screen.blit(Setting, (width/2 - 70, height/2 - 20))
        screen.blit(Exit, (width/2 - 45, height/2 + 100))
        screen.blit(Continue, (width/2 - 80, height/2 - 140))
        pygame.display.update()


def Settings(width, height):
    # загрузили изображение
    Menu1_surf = pygame.image.load('tiles\\Settings.png')
    # Передали изображение в дисплей
    screen.blit(Menu1_surf, (0, 0))
    # светлый оттенок кнопки
    color_light = (170, 170, 170)
    # темный оттенок кнопки при нажатии
    color_dark = (100, 100, 100)
    smallfont = pygame.font.SysFont('Times New Roman', 35)
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
                if (width/2 - 600 <= mouse_pos[0] <= width/2 - 550) and (height/2 - 300 < mouse_pos[1] < height/2 - 250):
                    # загрузили изображение
                    tmp_surf = pygame.image.load('tiles\\tmp.png')
                    # Передали изображение в дисплей
                    screen.blit(tmp_surf, (0, 0))
                    return width, height
                elif (width/2 - 50 <= mouse_pos[0] <= width/2) and (height/2 - 100 < mouse_pos[1] < height/2 - 50):
                    pygame.display.set_mode((width, height), pygame.FULLSCREEN)
                    screen.blit(Menu1_surf, (0, 0))
                elif (width/2 + 85 <= mouse_pos[0] <= width/2 + 135) and (height/2 - 100 < mouse_pos[1] < height/2 - 50):
                    pygame.display.toggle_fullscreen()
                    screen.blit(Menu1_surf, (0, 0))
            if (width/2 - 600 <= mouse_pos[0] <= width/2 - 550) and (height/2 - 300 < mouse_pos[1] < height/2 - 250):
                color_back = color_dark
            else:
                color_back = color_light
            if (width/2 - 50 <= mouse_pos[0] <= width/2) and (height/2 - 100 < mouse_pos[1] < height/2 - 50):
                color_fullscreen_yes = color_dark
            else:
                color_fullscreen_yes = color_light
            if (width / 2 + 85 <= mouse_pos[0] <= width/2 + 135) and (height/2 - 100 < mouse_pos[1] < height/2 - 50):
                color_fullscreen_no = color_dark
            else:
                color_fullscreen_no = color_light
            # Рендеринг текста с параметрами, опсианными выше
            back_Menu1 = smallfont.render('<', True, color_back)
            Fullscreen = smallfont.render('Fullscreen:              \\', True, color_light)
            Fullscreen_yes = smallfont.render('yes', True, color_fullscreen_yes)
            Fullscreen_no = smallfont.render('no', True, color_fullscreen_no)
            # Кидаем текст на экран
            screen.blit(back_Menu1, (width/2 - 600, height/2 - 300))
            screen.blit(Fullscreen, (width / 2 - 250, height / 2 - 100))
            screen.blit(Fullscreen_yes, (width / 2 - 50, height / 2 - 100))
            screen.blit(Fullscreen_no, (width / 2 + 85, height / 2 - 100))
            # Обновили дисплей
            pygame.display.update()

# Создаем окно screen с разрешением - 1280х720
width = 1280
height = 720
# экран = pygame.display.set_mode((width, height), pygame.FULLSCREEN) - полноэкранный режим
# pygame.display.toggle_fullscreen() - меняет режим экрана на в окне / полноэкр.
screen = pygame.display.set_mode((width, height))

# ----------------------------------------------Задание текста----------------------------------------------------------
# Белый цвет
# color = (255, 255, 255)
# светлый оттенок кнопки
# color_light = (170, 170, 170)
# темный оттенок кнопки при нажатии
# color_dark = (100, 100, 100)
# Настройки шрифта кнопки
# smallfont = pygame.font.SysFont('Times New Roman', 35)
# Рендеринг текста с параметрами, опсианными выше
# text = smallfont.render('Mytext', True, color)
# Кидаем текст на экран
# screen.blit(text, (x, y))
# ----------------------------------------------------------------------------------------------------------------------
Menu1(width, height)