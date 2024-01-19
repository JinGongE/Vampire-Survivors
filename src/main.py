import pygame

WIDTH = 1080
HEIGHT = 720

FPS = 60

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


#pygame.display.set_icon()
pygame.display.set_caption("Math Survivors")

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill("green")

    #디스플레이 업데이트
    pygame.display.update()

pygame.quit()