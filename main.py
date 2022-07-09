import pygame
import sys
from apple import Apple
from snake import Snake
from level import Level
from choose_level import choose_level


def main(name):
    pygame.init()
    clock = pygame.time.Clock()
    level = Level(name)
    screen = pygame.display.set_mode((level.width, level.height))
    snake = Snake(len(level.snake), level.snake)
    apple = Apple(level)
    font = pygame.font.SysFont('monospace', 30, True)
    directions = {(0, 1): 'DOWN', (0, -1): 'UP', (1, 0): 'RIGHT', (-1, 0): 'LEFT', (0, 0): ''}
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                main(choose_level(screen, level.width, level.height))
                pygame.quit()
        snake.update(level)
        apple.update(snake, level)

        screen.fill('#2a2e32')
        level.draw(screen)
        apple.draw(screen)
        snake.draw(screen)

        surf = font.render(f"X:{snake.x:>3}, Y:{snake.y:>3}, MOVE:{directions[snake.moving]}", False, 'White')
        screen.blit(surf, surf.get_rect(topleft=(5, 5)))

        surf = font.render(f"SCORE:{snake.size}", False, 'White')
        screen.blit(surf, surf.get_rect(topright=(950, 5)))

        pygame.display.update()
        clock.tick(min(5 + snake.size // 3, 60))


if __name__ == '__main__':
    number = sys.argv[1] if len(sys.argv) > 1 else 1
    name_level = '{}.csv'.format(number)
    main(name_level)
