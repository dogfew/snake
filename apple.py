import pygame
from random import randrange, choice


class Apple(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.x, self.y = randrange(0, level.width, 50), randrange(0, level.height, 50)
        self.type = choice([0, 0, 0, 1])

    def draw(self, screen):
        pygame.draw.rect(screen, pygame.Color('yellow' if self.type else 'red'), (self.x, self.y, 50, 50))

    def update(self, snake, level):
        if (snake.x, snake.y) == (self.x, self.y):
            snake.size += 1 + self.type
            self.__init__(level)
        while (self.x, self.y) in level.map:
            self.__init__(level)

