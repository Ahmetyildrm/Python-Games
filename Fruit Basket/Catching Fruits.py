import pygame
import random

pygame.init()


score = 0
faul = 0
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 20)

class BizimOyunumuz(object):

    def __init__(self):
        self.pencere_yuksekligi = 512
        self.pencere_genisligi = 1024
        self.Pencere = pygame.display.set_mode((self.pencere_genisligi, self.pencere_yuksekligi))
        pygame.display.set_caption("Fruit Basket")
        self.Clock = pygame.time.Clock()
        self.GameStatus = "Start"

        #### Background ####
        self.background = pygame.image.load("background.png").convert_alpha()
        self.Start_img = pygame.image.load("click.png").convert_alpha()
        self.Gameover_img = pygame.image.load("game-over.png").convert_alpha()

        #### ScoreBoard ####
        self.Scoreboard_img = pygame.image.load("scoreboard.png").convert_alpha()
        self.watermelon_board = pygame.image.load("watermelon_board.png").convert_alpha()

        #### Sepet ####
        self.sepet_w = 64
        self.sepet_h = 64
        self.sepet_x = 200
        self.sepet_y = 400
        self.sepet_img = pygame.image.load("basket.png").convert_alpha()
        self.sepet_move = 1

        #### Fruit ####
        self.watemelon_img = pygame.image.load("watermelon.png").convert_alpha()
        self.watemelon_score = 0
        self.lemon_img = pygame.image.load("lemon.png").convert_alpha()
        self.lemon_score = 0
        self.cheery_img = pygame.image.load("cherry.png").convert_alpha()
        self.cheery_score = 0

        self.fruit_img_list = [self.watemelon_img, self.lemon_img, self.cheery_img]
        self.fruit_x = random.randint(0, self.pencere_genisligi - 32)
        self.fruit_y = -32
        self.fruit_vel = 0.3
        self.picked_fruit = self.fruit_img_list[random.randint(0, len(self.fruit_img_list)-1)]

    def Cizim(self):
        self.Pencere.blit(self.background, (0, 0))
        if self.GameStatus == "Game":
            self.Pencere.blit(self.picked_fruit, (self.fruit_x, self.fruit_y))
            self.Pencere.blit(self.sepet_img, (self.sepet_x, self.sepet_y))
            watermelon_skor = font.render("" + str(self.watemelon_score), True, (0, 128, 0))
            lemon_skor = font.render("" + str(self.lemon_score), True, (255, 255, 0))
            cherry_skor = font.render("" + str(self.cheery_score), True, (255, 0, 0))

            fault = font.render("Fault: " + str(faul), True, (255, 0, 0))
            self.Pencere.blit(watermelon_skor, (30, 11))
            self.Pencere.blit(lemon_skor, (84, 11))
            self.Pencere.blit(cherry_skor, (138, 11))

            self.Pencere.blit(fault, (950, 10))
            self.Pencere.blit(self.watemelon_img, (0, 10))
            self.Pencere.blit(self.lemon_img, (54, 10))
            self.Pencere.blit(self.cheery_img, (108, 10))


        if self.GameStatus == "Start":
            self.Pencere.blit(self.Start_img, (448, 192))

        if self.GameStatus == "GameOver":

            self.Pencere.blit(self.Scoreboard_img, (128, 28))
            self.Pencere.blit(self.watermelon_board, (160, 65))

            #self.Pencere.blit(self.Gameover_img, (384, 300))
        
        pygame.display.update()





    def Oyun(self):
        global score
        global faul

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Son"

        self.Tus = pygame.key.get_pressed()
        if self.Tus[pygame.K_ESCAPE]:
            return "Son"
        if self.Tus[pygame.K_RIGHT]:
            self.sepet_x += self.sepet_move
        if self.Tus[pygame.K_LEFT]:
            self.sepet_x -= self.sepet_move
        if self.GameStatus == "Start" and self.Tus[pygame.K_SPACE]:
            score = 0
            faul = 0
            self.fruit_vel = 0.3
            self.cheery_score = 0
            self.watemelon_score = 0
            self.lemon_score = 0
            self.sepet_w = 64
            self.sepet_img = pygame.image.load("basket.png").convert_alpha()
            self.GameStatus = "Game"
        if self.GameStatus == "GameOver" and self.Tus[pygame.K_SPACE]:
            self.GameStatus = "Start"


        if self.GameStatus == "Game":
            #### Fruit Fall ####
            self.fruit_y += self.fruit_vel
            if score%5 == 0 and score != 0:
                self.fruit_vel += 0.0001


            #### Puan ####

            if self.fruit_x > self.sepet_x-12  and self.fruit_x < self.sepet_x + self.sepet_w-12 and self.fruit_y > self.sepet_y and self.fruit_y < self.sepet_y + 5 :
                score = score+1
                self.fruit_y = 0
                self.fruit_x = random.randint(0, 1000)

                if self.picked_fruit == self.watemelon_img: self.watemelon_score +=1
                if self.picked_fruit == self.lemon_img: self.lemon_score +=1
                if self.picked_fruit == self.cheery_img: self.cheery_score +=1
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("point.ogg"))



                self.picked_fruit = self.fruit_img_list[random.randint(0, len(self.fruit_img_list)-1)]

            if self.fruit_y >= 515:
                self.fruit_y = 0
                self.fruit_x = random.randint(0, 1000)
                faul +=1
                self.sepet_w += score * 2
                self.sepet_img = pygame.transform.scale(self.sepet_img, (self.sepet_w, self.sepet_h))
                self.picked_fruit = self.fruit_img_list[random.randint(0, len(self.fruit_img_list)-1)]

            if faul >= 3:
                self.GameStatus = "GameOver"
                dosya = open("Rekorlar.txt","a")
                # dosya.readlines()
                # dosya.write(str(self.watemelon_score)+"\n")
                # dosya.write(str(self.lemon_score)+"\n")
                # dosya.write(str(self.cheery_score)+"\n")





            #### Sepet ####
            if self.sepet_x > 1024:
                self.sepet_x = -64

            if self.sepet_x < -64:
                self.sepet_x = 1024


        self.Cizim()




Oyun = BizimOyunumuz()

while True:
    Durum = Oyun.Oyun()
    if Durum == "Son":
        break



pygame.quit()