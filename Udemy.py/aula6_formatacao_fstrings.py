import pygame
import sys

# Inicializa o pygame
pygame.init()

# Tamanho da tela
largura, altura = 500, 500
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Mini Pac-Man")

# Cores
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)

# Relógio para controlar FPS
clock = pygame.time.Clock()

# Posição inicial do Pac-Man
x = 50
y = 50
velocidade = 5
raio = 20

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Captura teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    # Preenche a tela
    tela.fill(PRETO)

    # Desenha o "Pac-Man" (círculo amarelo)
    pygame.draw.circle(tela, AMARELO, (x, y), raio)

    # Atualiza a tela
    pygame.display.flip()

    # Controla o FPS (frames por segundo)
    clock.tick(60)