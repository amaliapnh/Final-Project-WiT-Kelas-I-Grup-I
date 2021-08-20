import pygame
import time
import random
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()

#Display
display_width = 600
display_height = 650
window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Catch the Bread")

#Background
backgroundImg = pygame.image.load('background.jpg')
backgroundImg = pygame.transform.scale(backgroundImg, (600,750))

#Constant
black = (0, 0, 0)
fps = 60
vel = 5
bread_vel = 7
baker_width, baker_height = 100, 100
bread_width, bread_height = 40, 40

#Background Music
mixer.music.load('backsound.mp3')
mixer.music.play(-1)

#Player(Baker)
bakerImg = pygame.image.load('baker.png')
bakerImg = pygame.transform.scale(bakerImg, (baker_width, baker_height))

#Bread
breadImg = pygame.image.load('slicebread.png')
breadImg = pygame.transform.scale(breadImg, (bread_width, bread_height))


class Baker(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 10
        self.hitbox = (self.x, self.y + 20, 150, 80)
    def draw(self, window):
        window.blit(bakerImg, (self.x, self.y))
        self.hitbox = (self.x, self.y + 20, 150, 80)
    
class Breads(object):
    def __init__(self, x, y, f_type):
        self.x = x
        self.y = y
        self.f_type = f_type
        self.hitbox = (self.x, self.y, 100, 100)
    def draw(self, window):
        if self.f_type == 0:
            bread = pygame.image.load('slicebread.png')
            self.vel = 10
        bread = pygame.transform.scale(bread, (40, 40))
        window.blit(bread, (self.x, self.y))
        self.hitbox = (self.x, self.y, 40, 40)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, x, y, size):
    regText = pygame.font.Font("freesansbold.ttf", size)
    textSurf, textRect = text_objects(msg, regText)
    textRect.center = (x, y)
    window.blit(textSurf, textRect)

def main():
    score = 0
    breads = []
    bread_add_counter = 0
    add_bread_rate = 30
    baker = Baker(display_width * 0.35, display_height - 160)
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False      
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and baker.x > baker.vel - 5:
            baker.x -= baker.vel
        elif keys[pygame.K_RIGHT] and baker.x < 600 - 100 - baker.vel:
            baker.x += baker.vel  
        window.blit(backgroundImg, (0,0))
        bread_add_counter += 1
        if bread_add_counter == add_bread_rate:
            bread_add_counter = 0
            f_startx = random.randrange(100, display_width - 100)
            f_starty = 0
            f_type = 0 # change to random later
            new_bread = Breads(f_startx, f_starty, f_type)
            breads.append(new_bread)
        for item in breads:
            item.draw(window)
            item.y += item.vel
        for item in breads[:]:
            if (item.hitbox[0] >= baker.hitbox[0] - 20) and (item.hitbox[0] <= baker.hitbox[0] + 70):
                if baker.hitbox[1] - 120 <= item.hitbox[1] <= baker.hitbox[1] - 40:
                    breads.remove(item)
                    score += 1
                    if item.f_type == 0: 
                        score += 0
                    print("Score:", score)
        message_to_screen("Score: "+str(score), 50, 30, 20)        
        baker.draw(window)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

main()





























 
