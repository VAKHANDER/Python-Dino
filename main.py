import pygame
import sys
# Обязательная строчка во всех программах - играх, для подготовки модулей к работе
pygame.init()

# Создаем окно screen с разрешением - 1280х720
screen = pygame.display.set_mode((1280, 720))
# загрузили изображение
Menu1_surf = pygame.image.load('tiles\\Menu1.png')
# Передали изображение в дисплей
screen.blit(Menu1_surf, (0,0))

while True:
    # Обновили дисплей
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Завершаем работу модулей
            pygame.quit()
            # заврешаем работу программы
            sys.exit()
