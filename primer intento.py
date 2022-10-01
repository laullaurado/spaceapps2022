import pygame, random

BLACK = (0, 0, 0)

class James(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor2.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor2.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.y += 1
        if self.rect.y > 600:
            self.rect.y = -10
            self.rect.x = random.randrange(900)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player2.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0]
        player.rect.y = 400

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 4


pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
done = False
score = 0

meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
james_list = pygame.sprite.Group()

player = Player()
all_sprite_list.add(player)

Tiempo = pygame.time.get_ticks()
tiempo_entre = 100
Life = 5;
esp = 50;
for i in range(0,5):
    james = James()
    james.rect.x = esp + i*180
    james.rect.y = 510 
    james_list.add(james)
    all_sprite_list.add(james)

while not done:
    Tiempo = pygame.time.get_ticks()
    #print(Tiempo)
    
    
    if(Tiempo % tiempo_entre == 0):
        meteor = Meteor()
        meteor.rect.x = random.randrange(SCREEN_WIDTH - 20)
        meteor.rect.y = 600 

        meteor_list.add(meteor)
        all_sprite_list.add(meteor)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        

        if event.type == pygame.MOUSEBUTTONDOWN:
            laser = Laser()
            laser.rect.x = player.rect.x + 45
            laser.rect.y = player.rect.y - 20

            laser_list.add(laser)
            all_sprite_list.add(laser)


    all_sprite_list.update() 

    for laser in laser_list:
        meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True)	
        for meteor in meteor_hit_list:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)
            score += 1
            print(score)
        if laser.rect.y < -20:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)

    for meteor in meteor_list:
        james_hit_list = pygame.sprite.spritecollide(meteor, james_list, True)	
        for james in james_hit_list:
            all_sprite_list.remove(meteor)
            james_list.remove(meteor)
            Life -= 1
            print(Life)

    screen.fill([255, 255, 255])

    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()