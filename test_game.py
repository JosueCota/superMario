import pygame
from spritesheet import Spritesheet
pygame.init()

displayw, displayh = 480,270
canvas = pygame.Surface((displayw, displayh))
window = pygame.display.set_mode((displayw, displayh))
running = True

spritesheet = Spritesheet('images/spritesheet.png')
images = [spritesheet.parse_sprite('block1.png'), spritesheet.parse_sprite('block2.png')]

mario = [spritesheet.parse_sprite('mario1.png'),spritesheet.parse_sprite('mario2.png'),spritesheet.parse_sprite('mario3.png')]
index = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                index = (index+1) % len(mario)

    canvas.fill((255,255,255))
    canvas.blit(mario[index], (0, displayh- 16))
    canvas.blit(images[0], (15, displayh- 16))
    canvas.blit(images[1], (30, displayh- 16))
    window.blit(canvas, (0,0))
    pygame.display.update()