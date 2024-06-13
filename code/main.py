import pygame
from utils import *
from player import Player
from enemy import Enemy
from math import degrees, atan2, pi
from random import randint, choice, uniform

window_width = 600
window_height = 900

class Game():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Word Wars")

        self.FPS = pygame.time.Clock()

    def menu(self):
        while True:
            self.screen.fill(black)

            message_to_screen(self.screen, "WordWars", 62, window_width//2, 200, white)

            button_rect = pygame.rect.Rect(window_width//2-100, 300, 200, 80)
            if button(self.screen, "Jogar!", 32, button_rect, white, grey):
                self.run()
            

            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


    def game_over(self, points):
        while True:
            self.screen.fill(black)

            message_to_screen(self.screen, "Game Over", 62, window_width//2, 200, white)
            message_to_screen(self.screen, f"Pontuação: {points}", 32, window_width//2, 280, white)

            menu_buton_rect = pygame.rect.Rect(window_width//2-100, 400, 200, 80)
            if button(self.screen, "Menu", 32, menu_buton_rect, white, grey):
                self.menu()
                return
            
            again_button_rect = pygame.rect.Rect(window_width//2-150, 500, 300, 80)
            if button(self.screen, "Tentar novamente", 32, again_button_rect, white, grey):
                self.run()
                return            

            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


    def run(self):
        level = 0

        # Sprites
        player = Player(window_width//2 - 30, window_height - 120)

        enemies = []

        # main loop
        while True:
            self.FPS.tick(60)

            self.screen.fill(grey)

            player.update(self.screen)

            for enemy in enemies:
                if enemy.update(self.screen, player) == "DESTROYED":
                    # Move player to that direction
                    dx = player.rect.x - enemy.rect.x
                    dy = player.rect.y - enemy.rect.y
                    rads = atan2(-dy,dx)
                    rads %= 2*pi
                    degs = degrees(rads)

                    angle = degs + 90

                    player.rotate(angle)

                    # Remove the enemy
                    enemies.remove(enemy)

            # Next Level
            if enemies == []:
                level += 1
                for c in range(1, min(1 + int(1 + level/3), 6)):

                    en = Enemy(randint(0, window_width), randint(-200, 0), level)
                    en.movSpeed["speedX"] *= choice([-1, 1]) * uniform(1, 1.5)
                    en.movSpeed["speedY"] *= uniform(1, 1.5)

                    enemies.append(en)

            if player.life <= 0:
                break

            message_to_screen(self.screen, player.currWord, 20, player.image_rect.x + player.image_rect.w//2, player.image_rect.y + player.image_rect.h + 20, white)

            # Diplay level
            message_to_screen(self.screen, f"Level: {level}", 20, window_width - 80, 40, white)

            # Damage line
            pygame.draw.line(self.screen, red, (0, player.rect.y - 10), (window_width, player.rect.y - 10))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Must be here, otherwise there will be input lag
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if len(player.currWord) != 0:
                            player.currWord = player.currWord[:-1]
                    elif event.key in [pygame.K_SPACE, 126]:
                        pass
                    else:
                        player.currWord += event.unicode
        
        self.game_over(level)
            

game = Game()
game.menu()