import pygame
import csv


class Level(pygame.sprite.Sprite):
    def __init__(self, file):
        super().__init__()
        path = 'levels/{}'.format(file)
        self.array = [[int(j) for j in i] for i in csv.reader(open(path))]
        self.width, self.height = len(self.array[0]) * 50, len(self.array) * 50
        self.map = [(x * 50, y * 50)
                    for x in range(len(self.array[0]))
                    for y in range(len(self.array))
                    if self.array[y][x] == 1]
        self.snake = [(x * 50, y * 50)
                      for x in range(len(self.array[0]))
                      for y in range(len(self.array))
                      if self.array[y][x] == 5]

    def draw(self, screen):
        for x, y in self.map:
            pygame.draw.rect(screen, pygame.Color('#ffaa81'), (x, y, 50, 50))
