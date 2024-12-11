import pygame
import random

# init
pygame.init()
size = (width, height) = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snow')

# constants
WHITE = (255, 255, 255)
BACKGROUND = (30,63,102)
SNOWFLAKE_SIZE = 32
SNOWFLAKE_SPEED = 1
SNOWFLAKE_CHANCE = 0.02

# state
done = False
game_over = False
clock = pygame.time.Clock()
snowflakes = []

while not done:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_pos = pygame.mouse.get_pos()

            snowflakes_copy = snowflakes[:]
            for flake in snowflakes_copy:
                flake_rect = pygame.Rect(
                    flake[0] - SNOWFLAKE_SIZE // 2, 
                    flake[1] - SNOWFLAKE_SIZE // 2,
                    SNOWFLAKE_SIZE, 
                    SNOWFLAKE_SIZE
                )
                if flake_rect.collidepoint(mouse_pos):
                    snowflakes.remove(flake)

	# update game state
    if not game_over:
        if random.random() < SNOWFLAKE_CHANCE:
            snowflakes.append([random.randint(0, width), 0])

        for flake in snowflakes[:]:
            flake[1] += SNOWFLAKE_SPEED;
            if flake[1] >= height:
                game_over = True
                break
        
    # draw background
    screen.fill(BACKGROUND)
    # draw snowflakes
    for flake in snowflakes:
        pygame.draw.circle(screen, WHITE, (int(flake[0]), int(flake[1])), SNOWFLAKE_SIZE//2)
    # draw game over message
    if game_over:
        font = pygame.font.Font(None, 74)
        text = font.render('Game Over!', True, WHITE)
        text_rect = text.get_rect(center=(width//2, height//2))
        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()