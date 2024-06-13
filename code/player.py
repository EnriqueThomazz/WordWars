import pygame
from utils import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load("./graphics/spaceship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))

        self.rect = self.image.get_rect(topleft=(x, y))
        self.image_rect = self.rect
        
        self.lastAngle = 0

        self.currWord = ""

        self.life = 3

    def draw(self, surface):
        surface.blit(self.image, self.rect)

        for hp in range(self.life):
            pygame.draw.circle(surface, red, (30 * (hp + 1), surface.get_height() - 50), 10)

    def update(self, surface):
        self.draw(surface)

    def rotate(self, angle):
        # Bugged (!!!)
        return
        # Reseting the angle before rotatint again
        if angle != -self.lastAngle:
            self.rect = self.image_rect
            self.rotate(-self.lastAngle)

        rotated_image = pygame.transform.rotate(self.image, angle)

        new_rect = rotated_image.get_rect(center = self.image.get_rect(center = (self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h // 2)).center)


        self.image, self.rect = rotated_image, new_rect

        self.lastAngle = angle
