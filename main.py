import pygame
import sys

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
    x1 = 0
    x2 = 1280
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
        screen.blit(Game_surf1, (x1, 0))
        screen.blit(Game_surf2, (x2, 0))
        screen.blit(Dino, (100, y_dino))
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
        if x2 < -1280:
            x2 = 1280
        x1 = x1 - speed
        x2 = x2 - speed
        FPS.tick(fps)
        pygame.display.update()


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