import pygame
import random
from constants import TRAY_WIDTH, TRAY_HEIGHT, PIXEL_SIZE

def export_trays(trays, number_of_shapes):

    screen = pygame.display.set_mode((TRAY_WIDTH*PIXEL_SIZE, TRAY_HEIGHT*PIXEL_SIZE))

    colors = color_generator(number_of_shapes)
    BLACK = (0, 0, 0)
    WHITE = (255,255,255)

    pygame.init()

    def draw_square(leftF, topF, color):
        pygame.draw.rect(screen, color, pygame.Rect(leftF*PIXEL_SIZE, topF*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
        pygame.draw.rect(screen, BLACK, pygame.Rect(leftF*PIXEL_SIZE, topF*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE), 1)

    font = pygame.font.SysFont('Consolas', 10)
    def draw_text(leftF, topF, id):
        screen.blit(font.render(str(id), True, WHITE), (leftF*PIXEL_SIZE + 5, topF*PIXEL_SIZE + 5))

    screen.fill((255, 255, 255))

    export_counter = 0

    left, top = 0, 0

    while export_counter != len(trays):
        for y in range(TRAY_HEIGHT):
            for x in range(TRAY_WIDTH):
                draw_square(left, top, colors[int(trays[export_counter])])
                draw_text(left, top, trays[export_counter])
                pygame.display.update()
                left += 1
            top += 1
            left = 0
        pygame.image.save(screen, str(export_counter) + '.png')
        screen.fill((255, 255, 255))
        export_counter += 1
        top = 0
        left = 0

def color_generator(number_of_shapes):
    colors = []
    for i in range(0, number_of_shapes):
        random.seed(i*i*i)
        colors.append((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        colors[0] = (255, 255, 255)
    return colors