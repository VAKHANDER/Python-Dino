import pygame
import sys
# Обязательная строчка по всех программах - играх, для подготовки модулей к работе
pygame.init()

# Создаем окно screen с разрешением - 1280х720
screen = pygame.display.set_mode((1280, 720))
# загрузили изображение
Menu1_surf = pygame.image.load('tiles\\Menu1.png')
# Передали изображение в дисплей
screen.blit(Menu1_surf, (0,0))

while True:
    for event in pygame.event.get():
        # Обновили дисплей
        pygame.display.update()
        if event.type == pygame.QUIT:
            # Завершаем работу модулей
            pygame.quit()
            # заврешаем работу программы
            sys.exit()