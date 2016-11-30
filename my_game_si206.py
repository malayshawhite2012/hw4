import pygame
import pygame.sprite 
import random

display_width = 800
display_height = 600

redbg = (255, 0, 0)

class Drake(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("drake.bmp").convert_alpha()
        self.rect = self.image.get_rect()

    def move(self):
        randX = randint(0, 600)
        randY = randint(0, 400)
        self.rect.center = (randX,randY)

class HelloKitty(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("hellokitty.gif").convert()
        self.rect = self.image.get_rect()

    def hit(self, target):
        return self.rect.colliderect(target)

    def update(self):
        self.rect.center = mouse.get_pos()

pygame.init()

gameDisplay =pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('YOUR FAV PYGAME GAME EVER!')

clock = pygame.time.Clock()

mouse.set_visible(False)

f = font.Font(None, 25)

drake = Drake()
hellokitty = HelloKitty()
crashed = False

sprites = RenderPlain(drake, hellokitty)

hits = 0
time.set_timer(USEREVENT + 1, DELAY)

while True:
    e = event.poll()
    if e.type == QUIT:
        quit()
        break

    elif e.type == MOUSEBUTTONDOWN:
        if hellokitty.hit(drake):
            mixer.Sound("sorry.wav").play()
            drake.move()
            hits += 1

            time.set_timer(USEREVENT + 1, DELAY)
            
    elif e.type == USEREVENT + 1: 
    	drake.move()

    screen.fill(redbg)
    t = f.render("Jackpot = " + str(hits), False, (0,0,0))
    screen.blit(t, (320, 0))   

    sprites.update()
    sprites.draw(screen)
    display.update()

pygame.quit()
quit()
