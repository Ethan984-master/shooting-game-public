import pygame
Black = (0, 0, 0)


class Portal(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(Black)
        self.image.set_colorkey(Black)
        pygame.draw.rect(self.image, color, (0, 0, width, height))
        self.rect = self.image.get_rect()

