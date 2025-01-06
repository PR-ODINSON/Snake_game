#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Clock and FPS
clock = pygame.time.Clock()

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Enhanced Snake Game")

# Load sounds
eat_sound = pygame.mixer.Sound("Snake_bite.mp3")  # Replace with the correct file path
pygame.mixer.music.load("BG_snake_sound.mp3")  # Replace with the correct file path

def show_score(score):
    value = score_font.render(f"Score: {score}", True, YELLOW)
    screen.blit(value, [10, 10])

def draw_snake(block_size, snake_list):
    for index, block in enumerate(snake_list):
        color = GREEN if index == 0 else (BLUE if index % 2 == 0 else GREEN)  # Snake tail color alternating
        pygame.draw.rect(screen, color, [block[0], block[1], block_size, block_size])

def message(msg, color, position):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, position)

def home_screen():
    home = True
    difficulty = "Medium"
    speed = 15
    walls_enabled = False

    while home:
        screen.fill(BLACK)
        message("Welcome to Enhanced Snake Game", YELLOW, [SCREEN_WIDTH // 6, SCREEN_HEIGHT // 4])
        message("Select Difficulty:", WHITE, [SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2 - 50])
        message("1. Easy", GREEN, [SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2])
        message("2. Medium", YELLOW, [SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2 + 30])
        message("3. Hard", RED, [SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2 + 60])
        message(f"Wall {'ON' if walls_enabled else 'OFF'}", WHITE, [SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2 + 90])
        message("Press SPACE to Start", WHITE, [SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2 + 150])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = "Easy"
                    speed = 10
                elif event.key == pygame.K_2:
                    difficulty = "Medium"
                    speed = 15
                elif event.key == pygame.K_3:
                    difficulty = "Hard"
                    speed = 20
                elif event.key == pygame.K_w:  # Toggle wall on/off
                    walls_enabled = not walls_enabled
                elif event.key == pygame.K_SPACE:
                    home = False
                    game_loop(speed, walls_enabled)

def game_loop(speed, walls_enabled):
    # Game variables
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH // 2
    y1 = SCREEN_HEIGHT // 2

    x1_change = 0
    y1_change = 0

    snake_block = 20
    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 20.0) * 20.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 20.0) * 20.0

    score = 0

    # Track last speed-up threshold
    last_threshold = 0

    # Play background music
    pygame.mixer.music.play(-1, 0.0)  # Loop the music indefinitely

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED, [SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3])
            show_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        home_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Check for collision with walls
        if walls_enabled:
            if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
                game_close = True
        else:
            # Wraparound if walls are off
            if x1 >= SCREEN_WIDTH:
                x1 = 0
            elif x1 < 0:
                x1 = SCREEN_WIDTH - snake_block
            if y1 >= SCREEN_HEIGHT:
                y1 = 0
            elif y1 < 0:
                y1 = SCREEN_HEIGHT - snake_block

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        show_score(score)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 20.0) * 20.0
            food_y = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 20.0) * 20.0
            length_of_snake += 1
            score += 10
            eat_sound.play()  # Play sound when food is eaten

        # Increase speed every 50 points, but avoid exponential increase
        if score >= last_threshold + 50:
            last_threshold += 50
            speed += 1

        clock.tick(speed)

    pygame.mixer.music.stop()  # Stop background music
    pygame.quit()
    quit()

# Start the game
home_screen()


# ## 
