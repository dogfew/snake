import pygame
import sys
import os


def choose_level(screen, width, height):
    total = [pygame.K_0, pygame.K_1, pygame.K_2,
             pygame.K_3, pygame.K_4, pygame.K_5,
             pygame.K_6, pygame.K_7, pygame.K_8,
             pygame.K_9]
    font = pygame.font.SysFont('monospace', 30, True)
    length = len(os.listdir('levels'))
    surf = font.render(f"CHOOSE LEVEL NUMBER: {', '.join(map(str, range(length)))}", False, 'White')
    screen.blit(surf, surf.get_rect(midbottom=(width // 2, height // 2)))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        for num, key in enumerate(total[:length]):
            if keys[key]:
                return "{}.csv".format(num)
        screen.fill('#2a2e32')
        screen.blit(surf, surf.get_rect(midbottom=(width // 2, height // 2)))
        pygame.display.update()
