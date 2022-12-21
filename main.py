import pygame
import time

fps = 60
pygame.init()
screen = pygame.display.set_mode((600, 300))
running = True
clock = pygame.time.Clock()
screen.fill("#0000ff")


def load_image(name):
    import os
    print(os.getcwd() + name)
    if os.path.isfile(name):
        return pygame.image.load(name)
    else:
        raise "Adslkjsjdfos;jdt"


class Car(pygame.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.p = 1
        self.norm = load_image("data/game over.png")
        self.image = self.norm
        self.mod = 1.1
        self.rect = self.image.get_rect()
        self.not_norm = pygame.transform.flip(self.norm, True, False)
        self.rect.x = -600

    def update(self, *args, **kwargs) -> None:
        self.rect.x += self.p * 1 * self.mod
        x = self.rect.x
        if x == 0:
            self.p = 0

cursor = Car()
sprites = pygame.sprite.Group()
sprites.add(cursor)
while running:
    screen.fill("#000000")
    sprites.update()
    sprites.draw(screen)
    clock.tick(fps)
    pygame.display.flip()
