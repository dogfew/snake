import pygame


class Snake(pygame.sprite.Sprite):

    def __init__(self, size, coords):
        super().__init__()
        self.moving = (0, 0)
        self.size = size
        self.body = [(x, y) for x, y in coords]
        self.x, self.y = self.body[-1]

    def draw(self, screen):
        for i, j in self.body:
            pygame.draw.rect(screen, pygame.Color('green'), (i, j, 50, 50))

    def destroy(self, level):
        head = self.body[-1]
        if head in self.body[:-1] or head in level.map:
            self.__init__(len(level.snake), level.snake)

    def move(self):
        if any(pygame.mouse.get_pressed()):
            x, y = pygame.mouse.get_pos()
            dx = self.x - x
            dy = self.y - y
            if abs(dx) < abs(dy):
                if dy > 0 and not self.moving[1]:
                    self.moving = (0, -1)
                elif dy < 0 and not self.moving[1]:
                    self.moving = (0, 1)
            else:
                if dx < 0 and not self.moving[0]:
                    self.moving = (1, 0)
                elif dx > 0 and not self.moving[0]:
                    self.moving = (-1, 0)
            return

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and not self.moving[1]:
            self.moving = (0, -1)
        elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and not self.moving[1]:
            self.moving = (0, 1)
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and not self.moving[0]:
            self.moving = (1, 0)
        elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and not self.moving[0]:
            self.moving = (-1, 0)

    def update(self, level):
        self.move()
        if any(self.moving):
            self.x += self.moving[0] * 50
            self.y += self.moving[1] * 50
            if self.y < 0:
                self.y = level.height
            elif self.y == level.height:
                self.y = 0
            if self.x < 0:
                self.x = level.width
            elif self.x == level.width:
                self.x = 0
            self.body.append((self.x, self.y))
            self.body = self.body[-self.size:]
        self.destroy(level)
