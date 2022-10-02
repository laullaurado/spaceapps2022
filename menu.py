import pygame, sys, random

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
  
	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

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
        velocidad = 10
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

def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("IMAGESGAME/font.ttf", size)

def instructions():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        BACKGROUND = pygame.image.load("IMAGESGAME/Background.png")
        screen.blit(BACKGROUND, (0, 0))

        OPTIONS_TEXT = get_font(65).render("INSTRUCTIONS", True, "#b68f40")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(450, 100))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(450, 550), 
                            text_input="BACK", font=get_font(65), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    break

        pygame.display.update()

pygame.init()

BLACK = (0, 0, 0)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

# x = 0
izquierda = False
derecha = False
cuentaPasos = 0

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
fondo =  pygame.image.load("james_webb_1.png")
pygame.display.set_caption("Saving James")

clock = pygame.time.Clock()
# done = False
# score = 0
icono = pygame.image.load('player3.png')
pygame.display.set_icon(icono)

meteor_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
james_list = pygame.sprite.Group()

player = Player()
all_sprite_list.add(player)

Tiempo = pygame.time.get_ticks()
tiempo_entre = 60
# Life = 5
esp = 50

# Background del menu, se carga con ese comando 
BG = pygame.image.load("IMAGESGAME/fondo_menu.jpg")

for i in range(0,5):
    james = James()
    james.rect.x = esp + i*180
    james.rect.y = 510 
    james_list.add(james)
    all_sprite_list.add(james)
    
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play()

while True:
    screen.blit(BG, (0, 0))

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    MENU_TEXT = get_font(80).render("MENU", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(450, 100))

    PLAY_BUTTON = Button(image=pygame.image.load("IMAGESGAME/Play Rect.png"), pos=(450, 250), 
                         text_input="PLAY", font=get_font(65), base_color="#d7fcd4", hovering_color="White")
    INSTRUCTIONS_BUTTON = Button(image=pygame.image.load("IMAGESGAME/Options Rect.png"), pos=(450, 400), 
                        text_input="INSTRUCTIONS", font=get_font(65), base_color="#d7fcd4", hovering_color="White")
    QUIT_BUTTON = Button(image=pygame.image.load("IMAGESGAME/Quit Rect.png"), pos=(450, 550), 
                         text_input="QUIT", font=get_font(65), base_color="#d7fcd4", hovering_color="White")

    screen.blit(MENU_TEXT, MENU_RECT)

    # al momento de seleccionar la opcion que cambie de color

    for button in [PLAY_BUTTON, INSTRUCTIONS_BUTTON, QUIT_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(screen)


    # Nuevamente me ayudo Stackoverflow JSJS
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                done = False
                Life = 5
                x = 0
                score = 0
                while True:
                    while not done:
                        Tiempo = pygame.time.get_ticks()
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
                        draw_text(screen, "Lives: " + str(Life), 25, SCREEN_WIDTH // 2, 35)
                        pygame.display.flip()
            
            if INSTRUCTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                instructions()
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                pygame.quit()
                sys.exit()

    pygame.display.update()

pygame.quit()
sys.exit()