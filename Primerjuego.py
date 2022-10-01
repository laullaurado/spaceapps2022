import pygame

# Iniciación de Pygame
pygame.init()

# Pantalla - ventana
W, H = 1000, 400
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption('Nave')
icono=pygame.image.load('player3.png')
pygame.display.set_icon(icono)

# Fondo del juego
fondo = pygame.image.load('estrellas.png')

quieto = pygame.image.load('player3.png')

caminaDerecha = [pygame.image.load('player2.png'),
				 pygame.image.load('player4.png'),
                 pygame.image.load('player2.png'),
				 pygame.image.load('player4.png'),
				 pygame.image.load('player5.png')]

caminaIzquierda = [pygame.image.load('player5.png'),
				 pygame.image.load('player4.png'),
				 pygame.image.load('player4.png'),
				 pygame.image.load('player2.png'),
				 pygame.image.load('player2.png')]


x = 0
px = 50
py = 200
ancho = 40
velocidad = 10

# Control de FPS
reloj = pygame.time.Clock()

# Variables dirección
izquierda = False
derecha = False

# Pasos
cuentaPasos = 0

# Movimiento
def recarga_pantalla():
	# Variables globales
	global cuentaPasos
	global x

	# Fondo en movimiento
	x_relativa = x % fondo.get_rect().width
	PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
	if x_relativa < W:
		PANTALLA.blit(fondo, (x_relativa, 0))
	x -= 5
	# Contador de pasos
	if cuentaPasos + 1 >= 6:
		cuentaPasos = 0
	# Movimiento a la izquierda
	if izquierda:
		PANTALLA.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1

		# Movimiento a la derecha
	elif derecha:
		PANTALLA.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1

	else:
		PANTALLA.blit(quieto,(int(px), int(py)))

ejecuta = True

# Bucle de acciones y controles
while ejecuta:
	# FPS
	reloj.tick(18)

	# Bucle del juego
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			ejecuta = False

	# Opción tecla pulsada
	keys = pygame.key.get_pressed()

	# Tecla A - Moviemiento a la izquierda
	if keys[pygame.K_a] and px > velocidad:
		px -= velocidad
		izquierda = True
		derecha = False

	# Tecla D - Moviemiento a la derecha
	elif keys[pygame.K_d] and px < 900 - velocidad - ancho:
		px += velocidad
		izquierda = False
		derecha = True

	# Personaje quieto
	else:
		izquierda = False
		derecha = False
		cuentaPasos = 0

	# Tecla W - Moviemiento hacia arriba
	if keys[pygame.K_w] and py > 100:
		py -= velocidad

	# Tecla S - Moviemiento hacia abajo
	if keys[pygame.K_s] and py < 300:
		py += velocidad
	# Tecla SPACE - Salto

	#else:
		#if cuentaSalto >= -10:
		#	py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
		#	cuentaSalto -= 1
		#else:
		#	cuentaSalto = 10
		#	salto = False

	# Actualización de la ventana
	pygame.display.update()
	#Llamada a la función de actualización de la ventana
	recarga_pantalla()

# Salida del juego
pygame.quit()