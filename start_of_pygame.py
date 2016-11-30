#required 
# import pygame
# pygame.init();

# #create a surface
# gameDisplay = pygame.display.set_mode((800,600)) #initialize with a tuple

# #lets add a title, aka "caption"
# pygame.display.set_caption("Events")

# #pygame.display.flip() 		#similar to a flip book, updates entire surface
# pygame.display.update()		#only updates portion specified


# gameExit = False
# while not gameExit:
# 	for event in pygame.event.get():
# 		print(event)

# # Dig for gold
# # Based on Whack-a-mole game using pygame by Kimberly Todd

from pygame import *
from pygame.sprite import *
from random import *

DELAY = 1000;            #Seed a timer to move sprite

bgcolor = (255,192,203)    #Color taken from background of sprite

class Drake(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("drake.bmp").convert()
        self.image = transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

    # move gold to a new random location
    def move(self):
        randX = randint(0, 600)
        randY = randint(0, 400)
        self.rect.center = (randX,randY)

class Poop(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("poop.bmp")
        self.rect = self.image.get_rect()

    # move gold to a new random location
    def move(self):
        randX = randint(0, 600)
        randY = randint(0, 400)
        self.rect.center = (randX,randY)

class HelloKitty(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("hellokitty.bmp").convert()
        self.image = transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()

    # Di shovel/cursor collide the gold?
    def hit(self, target):
        return self.rect.colliderect(target)

    #The shovel sprite will move with the mousepointer
    def update(self):
        self.rect.center = mouse.get_pos()

#main
init()

screen = display.set_mode((640, 480))
display.set_caption('Yo fav game ever!')

# hide the mouse cursor so we only see shovel
mouse.set_visible(False)

f = font.Font(None, 25)

# create the mole and shovel using the constructors
drake = Drake()
hellokitty = HelloKitty()
poop = Poop()
# creates a group of sprites so all can be updated at once
sprites = RenderPlain(drake, hellokitty)
poop_sprite = RenderPlain(poop)

hits = 0
level = 1
score_to_next_level = 5
time.set_timer(USEREVENT + 1, DELAY)

# loop until user quits
while True:
    e = event.poll()
    if e.type == QUIT:
        quit()
        break
    elif e.type == MOUSEBUTTONDOWN:
        if hellokitty.hit(drake):
            mixer.Sound("cha-ching.wav").play()
            drake.move()
            hits += 1

            # reset timer
            time.set_timer(USEREVENT + 1, DELAY)
            
    elif e.type == USEREVENT + 1: # TIME has passed
        drake.move()


    elif e.type == MOUSEBUTTONDOWN:
        if hellokitty.hit(drake):
            drake.move()
            hits += 1

            # reset timer
            time.set_timer(USEREVENT + 1, DELAY)
            
    elif e.type == USEREVENT + 1: # TIME has passed
        drake.move()

    if(level ==2):
        bgcolor = (255,255,255)
    elif(level == 3):
        bgcolor = (0,0,0)
    elif(level ==4):
        bgcolor = (0,255,0)
    elif (level> 4):
        bgcolor = (0,0,255)


    if(hits >= score_to_next_level):
        level +=1
        score_to_next_level = score_to_next_level*2

    # refill background color so that we can paint sprites in new locations
    screen.fill(bgcolor)
    t = f.render("Current Score = " + str(hits) + " Level = " + str(level), False, (0,0,0))
    screen.blit(t, (320, 0))        # draw text to screen.  Can you move it?

    # update and redraw sprites
    sprites.update()
    sprites.draw(screen)
    display.update()

#required
pygame.quit()
quit()				#exits python