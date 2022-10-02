import pygame, random

BLACK = (0, 0, 0)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

pygame.display.set_caption("Salvando a James")
x = 0
izquierda = False
derecha = False
cuentaPasos = 0

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
fondo =  pygame.image.load("james_webb_1.png")


def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

class James(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("james.png").convert()
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
        # mouse_pos = pygame.mouse.get_pos()
        ancho = 40
        velocidad = 8
        player.rect.y = 400
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and player.rect.x < 900 - velocidad - ancho:
                all_sprite_list.remove(player)
                player.rect.x += velocidad
                all_sprite_list.add(player)
                izquierda = False
                derecha = True
            if event.key == pygame.K_LEFT and player.rect.x > velocidad:
        	    player.rect.x -= velocidad
        	    izquierda = True
        	    derecha = False
            else:
        	    izquierda = False
        	    derecha = False
        	    cuentaPasos = 0

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 4

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
done = False
score = 0
icono = pygame.image.load('player3.png')
pygame.display.set_icon(icono)

meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
james_list = pygame.sprite.Group()

player = Player()
all_sprite_list.add(player)

Tiempo = pygame.time.get_ticks()
tiempo_entre = 65
Life = 5;
esp = 50;
for i in range(0,5):
    james = James()
    james.rect.x = esp + i*180
    james.rect.y = 510 
    james_list.add(james)
    all_sprite_list.add(james)
    
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play()
    
while not done:
    Tiempo = pygame.time.get_ticks()
    #print(Tiempo)
    sound = pygame.mixer.Sound("laser5.ogg")
    
    x_relativa = x % fondo.get_rect().width
    screen.blit(fondo,(x_relativa - fondo.get_rect().width,0))
    if x_relativa < SCREEN_WIDTH:
        screen.blit(fondo,(x_relativa,0))
    x -= 1
    
    if(Tiempo % tiempo_entre == 0):
        meteor = Meteor()
        meteor.rect.x = random.randrange(SCREEN_WIDTH - 20)
        meteor.rect.y = 600 

        meteor_list.add(meteor)
        all_sprite_list.add(meteor)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                laser = Laser()
                laser.rect.x = player.rect.x + 45
                laser.rect.y = player.rect.y - 20
                laser_list.add(laser)
                all_sprite_list.add(laser)
                sound.play()


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


    all_sprite_list.draw(screen)

    clock.tick(60)
    draw_text(screen, "Score: " + str(score), 25, SCREEN_WIDTH // 2, 10)
    draw_text(screen, "Lifes: " + str(Life), 25, SCREEN_WIDTH // 2, 35)
    pygame.display.flip()

pygame.quit()