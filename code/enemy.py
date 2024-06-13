import pygame
from utils import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, dif):
        self.image = pygame.image.load("./graphics/meteor.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect(topleft=(x, y))

        #self.wordLight = ""
        self.word = pick_word(dif)
        self.movSpeed = {"speedX": 1 + dif/50, "speedY": 1 + dif/50}


    def draw(self, surface):
        surface.blit(self.image, self.rect)
        message_to_screen(surface, self.word, 20, self.rect.x + self.rect.w//2, self.rect.y + 50, white)

    def update(self, surface, player):
        # Moving
        self.rect.x, self.rect.y = self.rect.x + self.movSpeed["speedX"], self.rect.y + self.movSpeed["speedY"]

        # Color of the letters, change color based on how much the player has gotten correct

        # Destroying if word is equal
        if player.currWord == self.word:
            player.currWord = ""

            pygame.mixer.music.load("./sounds/meteor_destroy.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.02)

            return "DESTROYED"

        # Screen boundaries
        if self.rect.x + self.rect.w > surface.get_width():
            self.rect.x = surface.get_width() - self.rect.w - 1
            self.movSpeed["speedX"] *= -1
        elif  self.rect.x < 0:
            self.rect.x = 0
            self.movSpeed["speedX"] *= -1

        # Bellow player Y = damge
        if self.rect.y + self.rect.h > player.rect.y:
            player.life -= 1

            # Damage sound
            pygame.mixer.music.load("./sounds/damage.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.02)

            player.currWord = ""
            return "DESTROYED"

        self.draw(surface)
        