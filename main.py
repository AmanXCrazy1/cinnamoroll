import pygame
import math
import random

pygame.init()
# Display shits
ribbon = pygame.image.load("scoree.png")
ribbon = pygame.transform.scale(ribbon, (270, 239))
ribbont = pygame.transform.scale(ribbon, (260, 239))


def rib(x, y):
    screen.blit(ribbon, (x, y))


def ribt(x, y):
    screen.blit(ribbont, (x, y))


# screen
width = 1100
height = 800
screen = pygame.display.set_mode((width, height))
surface = pygame.Surface((width, height), pygame.SRCALPHA)
pygame.display.set_caption("Go Cinnamoroll Go!")

iconp = pygame.image.load("Cinnamoroll.png")
iconp = pygame.transform.scale(iconp, (32, 32))
pygame.display.set_icon(iconp)

# Background
bg = pygame.image.load("bg.png").convert_alpha()

# loading all images


# EXTRA
up = 0
up1 = 0
current_time = 0
pstop = 0
ostop = 0
life = 0

# Score
score_value = 0
scorex = 905
scorey = 20

clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 36)
clockx = 40
clocky = 20


def score(x, y):
    score = font.render("Score: " + str(score_value), True, (190, 87, 0))
    screen.blit(score, (x, y))


# Player
pimg = pygame.image.load("icony1.png").convert_alpha()
pimg = pygame.transform.scale(pimg, (110, 110))
pX = 485
pY = 650
pXC = 0
pYC = 0


def player(x, y):
    screen.blit(pimg, (x, y))


# Objective1
cin = pygame.image.load("cinnamo.png")
o1x = 10
o1y = -150
o1yc = 4

# Objective2
o2x = 10
o2y = -150
o2yc = 4


def objective(x, y):
    screen.blit(cin, (x, y))


# defining the Death screen

death = pygame.image.load("gg.png")


def deathscreen():
    global pX
    global pY
    global score_value
    global up
    global up1
    global pXC

    pX = 485
    pY = 650
    score_value = 0
    up = 0
    up1 = 0
    pXC = 0

    screen.blit(death, (360, 150))


# Collision
def collision(pX, pY, o1x, o1y):
    distance = math.sqrt((math.pow(pX - o1x, 2)) + (math.pow(pY - o1y, 2)))
    if distance <= 120:
        return True
    else:
        return False


def pause():
    global up1
    global o1yc
    global pXC
    global pstop
    global ostop

    pstop = pXC
    ostop = o1yc + up1


def resume():
    global pstop
    global ostop

    pstop = 0
    ostop = 0


# Loop for screen
running = True
while running:
    screen.fill((40, 208, 245))
    screen.blit(surface, (0, 0))
    screen.blit(bg, (0, 0))
    pause()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # events in the game

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_UP:
            deathscreen()
            o1y = -150
            pX = 485
            pY = 650
            score_value = 0
            pXC = 0
            o1x = random.randint(10, 970)

        if event.key == pygame.K_LEFT:
            resume()
            pXC = -5 - int(up)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            resume()
            pXC = 5 + int(up)
        if event.key == pygame.K_p:
            pause()
        if event.key == pygame.K_r:
            resume()
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            pXC = -5 - int(up)
            resume()
        if event.key == pygame.K_RIGHT:
            pXC = 5 + int(up)
            resume()
        if event.key == pygame.K_UP:
            deathscreen()
            o1y = -150
            pX = 485
            pY = 650
            score_value = 0
            pXC = 0
            o1x = random.randint(10, 985)
            current_time = 0

        if event.key == pygame.K_p:
            pause()
        if event.key == pygame.K_r:
            resume()

    # making player move

    o1y = o1y + o1yc + up1 - ostop
    pX = pX + pXC - pstop
    if pX < -5:
        deathscreen()

    if pX >= 1005:
        deathscreen()

    if o1y > 750:
        deathscreen()

        # collision check

    col = collision(pX, pY, o1x, o1y)

    if col:
        score_value = score_value + 1
        up = up + 0.10
        up1 = up1 + 0.08

        o1y = -150
        o1x = random.randint(5, 920)

    if up >= 12:
        up = 12
    if up1 >= 9:
        up1 = 9


    ribt(clockx - 50, clocky - 100)
    rib(845, -79)
    # time(clockx, clocky)
    score(scorex, scorey)
    player(pX, pY)
    objective(o1x, o1y)
    clock.tick(60)
    pygame.display.update()
