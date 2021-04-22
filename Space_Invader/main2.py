import pygame
import random
import math

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))


# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Images/ufo.png")
pygame.display.set_icon(icon)


# Background
background = pygame.image.load("Images/background.jpg")
gameoverbg = pygame.image.load("Images/gameover.jpg")

# Player
playerImg = pygame.image.load("Images/player.png")
playerX = 370
playerY= 480
playerX_change = 0

class player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change = 0

    def move(self, screen):
        self.x




# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = int(input("How many enemies you want:"))


class enemy(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("Images/alien(1).png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)


# Bullet
bulletImage = pygame.image.load("Images/bullet.png")
bulletX = 0
bulletY= 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

class bullet(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


score = 0
def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage, (x+16, y+10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance <27 and bullet_state == "fire":
        return True
    else:
        return False

# Score
score_value = 0
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 32)

textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))


# Game loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Spaceship boundary
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736





    # Enemy boundary
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            if enemyY[i] < 440:
                score_value += round(num_of_enemies*2/3)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

        if enemyY[i] > 600:
            for i in range(len(enemyY)):
                enemyY[i] = 1200
            screen.fill((0, 0, 0))
            #font1 = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 100)
            #gameover = font.render("Game Over", True, (255, 255, 255))
            screen.blit(gameoverbg, (0, 0))
            break




     # Bullet Movement
    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()

