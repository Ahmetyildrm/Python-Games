import pygame
import random

## Press space to Jump

pygame.init()

score = 0
score_value = 0
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 20)
font2 = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 40)


class BizimOyunumuz(object):
    def __init__(self):
        self.pencere_yuksekligi = 512
        self.pencere_genisligi = 288
        self.Pencere = pygame.display.set_mode((self.pencere_genisligi, self.pencere_yuksekligi))
        pygame.display.set_caption("Flappy Bird")
        self.Clock = pygame.time.Clock()
        self.GameStatus = "Start"

        ####### Background ########
        self.BackgroundDay = pygame.image.load("Resimler/sprites/background-day.png").convert_alpha()
        self.BackgroundNight = pygame.image.load("Resimler/sprites/background-night.png").convert_alpha()
        self.BackgroundList = [self.BackgroundDay, self.BackgroundNight]
        self.Background = self.BackgroundList[random.randint(0, 1)]
        self.GameStartImage = pygame.image.load("Resimler/sprites/message.png").convert_alpha()
        self.GameOverImage = pygame.image.load("Resimler/sprites/gameover.png").convert_alpha()

        ###### Ground #######
        self.Ground = pygame.image.load("Resimler/sprites/base.png").convert_alpha()
        self.GroundX = 0
        self.GroundY = 400
        self.GroundChange = 1
        self.GroundX2 = self.GroundX + 336
        self.GroundY2 = self.GroundY

        #### Yem ####
        self.yem_x = 1000
        self.yem_y = 1000
        self.yem_img = pygame.image.load("Resimler/sprites/yem.png").convert_alpha()

        ####### Bird #########
        BirdColors = ["bluebird", "redbird", "yellowbird", "blackbird"]
        chosenbird = BirdColors[random.randint(0, len(BirdColors) - 1)]
        Birdfilename = ['Resimler/sprites/' + chosenbird + '-downflap.png',
                        'Resimler/sprites/' + chosenbird + '-midflap.png',
                        'Resimler/sprites/' + chosenbird + '-upflap.png']
        self.BirdUp = pygame.image.load(Birdfilename[2]).convert_alpha()
        self.BirdMid = pygame.image.load(Birdfilename[1]).convert_alpha()
        self.BirdDown = pygame.image.load(Birdfilename[0]).convert_alpha()
        self.BirdList = [self.BirdMid, self.BirdUp, self.BirdMid, self.BirdDown]
        self.BirdMaskList = [
            pygame.mask.from_surface(self.BirdMid),
            pygame.mask.from_surface(self.BirdUp),
            pygame.mask.from_surface(self.BirdMid),
            pygame.mask.from_surface(self.BirdDown),

        ]
        self.BirdAnimation = 0
        self.BirdAnimationDelay = 95
        self.BirdAnimationTime = pygame.time.get_ticks()
        self.BirdX = 50
        self.BirdY = 50
        self.BirdRight = 3

        self.Gravity = 0.75
        self.acc = 0.075

        ###### Boru #####
        self.borulist = []
        # self.boruresimleri = pygame.image.load("Resimler/sprites/pipe1.png")
        self.boruIMG = pygame.image.load("Resimler/sprites/pipe-green.png").convert_alpha()
        self.PipeAnimationTime = pygame.time.get_ticks()
        self.PipeAnimationDelay = 2200

    def MaskCollision(self, Masked_Image1, Image1_X, Image1_Y, Masked_Image2, Image2_X, Image2_Y):
        offset = (round(Image2_X - Image1_X), round(Image2_Y - Image1_Y))
        result = Masked_Image1.overlap(Masked_Image2, offset)
        return result

    class Boru():
        def __init__(self, boruX, boruY, boruimg):
            self.boruX = boruX
            self.boruY = boruY
            self.boruimg = boruimg
            self.boruhiz = 1
            self.lowerpipe = boruimg
            self.upperpipe = pygame.transform.flip(self.boruimg, False, True)

            self.lower_pipe_mask = pygame.mask.from_surface(self.lowerpipe)
            self.upper_pipe_mask = pygame.mask.from_surface(self.upperpipe)

        def BoruCiz(self, pencere):
            pencere.blit(self.lowerpipe, (self.boruX, self.boruY))  # Alt boru
            # ustboru = random.randint(300, 480)
            pencere.blit(self.upperpipe, (self.boruX, self.boruY - 420))  # Üst boru

        def boruhareket(self):
            self.boruX -= self.boruhiz

    def Cizim(self):
        pipe_number2 = font.render("Pipe Passed: " + str(score), True, (10, 0, 0))
        pipe_number = font2.render("Score: " + str(score), True, (255, 0, 0))
        self.Pencere.blit(self.Background, (0, 0))

        if self.GameStatus == "Start":
            self.Pencere.blit(self.GameStartImage, (53, 100))
        if self.GameStatus == "GameOver":
            self.Pencere.blit(self.GameOverImage, (55, 100))
            self.Pencere.blit(pipe_number, (75, 200))
        if self.GameStatus == "Game":
            for pipe in self.borulist:
                pipe.BoruCiz(self.Pencere)
            self.Pencere.blit(self.BirdList[self.BirdAnimation], (self.BirdX, self.BirdY))
            self.Pencere.blit(pipe_number2, (10, 10))
        self.Pencere.blit(self.Ground, (self.GroundX, self.GroundY))
        self.Pencere.blit(self.Ground, (self.GroundX2, self.GroundY2))
        self.Clock.tick(60)
        pygame.display.update()

    def Oyun(self):

        global score
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Son"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.GameStatus == "Start":
                        score = 0
                        self.GameStatus = "Game"
                    if self.GameStatus == "Game":
                        self.Gravity = -2
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound("Resimler/audio/wing.ogg"))
                    if self.GameStatus == "GameOver":
                        self.GameStatus = "Start"

        self.Tus = pygame.key.get_pressed()
        if self.Tus[pygame.K_ESCAPE]:
            return "Son"

        if self.GameStatus == "Game":
            ##### Sağa Hareket Ve Yer Çekimi ##########
            self.BirdY += self.Gravity
            self.Gravity += self.acc

            if self.BirdY >= self.GroundY - 24:
                self.BirdY = self.GroundY - 24

            ###### Ground Control #####
            self.GroundX -= self.GroundChange
            self.GroundX2 -= self.GroundChange
            if self.GroundX == -336:
                self.GroundX = 336
            if self.GroundX2 == -336:
                self.GroundX2 = 336

            ####### Bird Animation #########
            if pygame.time.get_ticks() - self.BirdAnimationTime > self.BirdAnimationDelay:
                self.BirdAnimation += 1
                if self.BirdAnimation == 4:
                    self.BirdAnimation = 0
                self.BirdAnimationTime = pygame.time.get_ticks()

            ###### Boru ######
            if pygame.time.get_ticks() - self.PipeAnimationTime > self.PipeAnimationDelay:
                self.borulist.append(self.Boru(300, random.randint(200, 350), self.boruIMG))
                self.PipeAnimationTime = pygame.time.get_ticks()

            for pipe in self.borulist:
                pipe.boruhareket()

                collision_lower = self.MaskCollision(self.BirdMaskList[self.BirdAnimation], self.BirdX, self.BirdY,
                                                     pipe.lower_pipe_mask, pipe.boruX, pipe.boruY
                                                     )
                collision_upper = self.MaskCollision(self.BirdMaskList[self.BirdAnimation], self.BirdX, self.BirdY,
                                                     pipe.upper_pipe_mask, pipe.boruX, pipe.boruY - 420
                                                     )

                if pipe.boruX <= -52:
                    self.borulist.remove(pipe)

                if collision_lower != None or collision_upper != None:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Resimler/audio/hit.ogg"))
                    self.GroundChange = 0
                    for pipe in self.borulist:
                        pipe.boruX += 1
                    self.borulist.clear()
                    self.GameStatus = "GameOver"

            #### Sayma ####

            for tmp in self.borulist:
                if self.BirdX > tmp.boruX + 15 and self.BirdX < tmp.boruX + 17:
                    score = score + 1
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Resimler/audio/point.ogg"))
                    self.PipeAnimationDelay -= 1




        self.Cizim()


Oyun = BizimOyunumuz()

while True:
    Durum = Oyun.Oyun()
    if Durum == "Son":
        break

pygame.quit()