import pygame
import time
import random

pygame.init()

# Define some colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set the size of the grid
GRIDSIZE = 20

# Set the size of the window
WINDOWSIZE = 800
window = pygame.display.set_mode((WINDOWSIZE, WINDOWSIZE))

# Set the title of the window
pygame.display.set_caption('Snake Game')

snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_speed = [10, 0]

food_pos = [random.randrange(1, WINDOWSIZE//GRIDSIZE)*GRIDSIZE, random.randrange(1, WINDOWSIZE//GRIDSIZE)*GRIDSIZE]
food_spawn = True

def draw_objects():
    window.fill(BLACK)
    for pos in snake_pos:
        pygame.draw.rect(window, GREEN, pygame.Rect(pos[0], pos[1], GRIDSIZE, GRIDSIZE))
    pygame.draw.rect(window, WHITE, pygame.Rect(food_pos[0], food_pos[1], GRIDSIZE, GRIDSIZE))

def snake_move():
    for i in range(len(snake_pos)-1, 0, -1):
        snake_pos[i] = list(snake_pos[i-1])
    snake_pos[0][0] += snake_speed[0]
    snake_pos[0][1] += snake_speed[1]

def check_game_over():
    if snake_pos[0][0] not in range(0, WINDOWSIZE) or snake_pos[0][1] not in range(0, WINDOWSIZE):
        return True
    for pos in snake_pos[1:]:
        if pos == snake_pos[0]:
            return True
    return False

def run_game():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            snake_speed[0], snake_speed[1] = 0, -10
        if keys[pygame.K_DOWN]:
            snake_speed[0], snake_speed[1] = 0, 10
        if keys[pygame.K_LEFT]:
            snake_speed[0], snake_speed[1] = -10, 0
        if keys[pygame.K_RIGHT]:
            snake_speed[0], snake_speed[1] = 10, 0

        draw_objects()

        snake_move()

        if snake_pos[0] == food_pos:
            food_spawn = False
        else:
            snake_pos.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, WINDOWSIZE//GRIDSIZE)*GRIDSIZE, random.randrange(1, WINDOWSIZE//GRIDSIZE)*GRIDSIZE]
        food_spawn = True

        pygame.display.update()

        if check_game_over():
            pygame.quit()

        clock.tick(20)

run_game()