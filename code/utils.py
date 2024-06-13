import pygame
import random

black = 0, 0, 0
white = 255, 255, 255
red = 150, 0, 0
grey = 97, 97, 97
dark_grey = 48, 48, 48
gold = 240, 215, 48
navy_blue = 76, 72, 183

with open("./code/words.txt", 'r', encoding='utf-8') as arq:

    def L(lst):
        return list(map(lambda word: word.rstrip(), lst))
    
    words = {"3": L(arq.readline().split(",")), "4": L(arq.readline().split(",")), "5": L(arq.readline().split(",")),
             "6": L(arq.readline().split(",")), "7": L(arq.readline().split(",")), "8": L(arq.readline().split(",")),
             "9": L(arq.readline().split(",")), "10": L(arq.readline().split(","))}


def message_to_screen(surface, text, size, x, y, color, bckg_color=None, returning=False, alignment="center"):
    font = pygame.font.Font("freesansbold.ttf", size)
    text = font.render(text, True, color, bckg_color)

    textRect = text.get_rect()

    if alignment == "center":
        textRect.center = (x, y)
    elif alignment == "bottomleft":
        textRect.bottomleft = (x, y)
    elif alignment == "bottomright":
        textRect.bottomright = (x, y)

    if returning:
        return {"text": text, "text_rect": textRect}

    surface.blit(text, textRect)


def button(surface, text, text_size, rect, color, active_color):
    pygame.draw.rect(surface, color, rect, 3)
    message_to_screen(surface, text, text_size, rect.x + rect.w//2, rect.y + rect.h//2, color)
    
    # checking if the mouse is over the button
    mouse = pygame.mouse.get_pos()
    if rect.x < mouse[0] < rect.x + rect.w:
        if rect.y < mouse[1] < rect.y + rect.h:
            pygame.draw.rect(surface, active_color, rect, 3)
            if pygame.mouse.get_pressed()[0]:
                return 1

    return 0

def pick_word(dif):
    size = ["3", "4", "5", "6", "7", "8", "9", "10"]

    dif = dif // len(size)

    for c in range(min(dif, 5)):
        size.append(random.choice(size[3:]))

    return random.choice(words[random.choice(size)]).lstrip()

def rotateImage(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect