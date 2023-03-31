import pygame
import random
import time

pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Game")

# Set up the fonts
FONT_SIZE = 50
font = pygame.font.SysFont("comicsansms", FONT_SIZE)

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the variables
letter = chr(random.randint(65, 90))
letter_x = random.randint(0, WIDTH - FONT_SIZE)
letter_y = 0
speed = 0.01
start_time = time.time()
typing_speed = 0

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode == letter:
                letter = chr(random.randint(65, 90))
                letter_x = random.randint(0, WIDTH - FONT_SIZE)
                letter_y = 0
                speed += 0.001
                typing_speed = 1 / (time.time() - start_time)
                start_time = time.time()

    # Update the variables
    letter_y += speed

    # Check if the letter has reached the bottom of the screen
    if letter_y > HEIGHT:
        running = False

    # Draw the screen
    screen.fill(BLACK)
    letter_text = font.render(letter, True, WHITE)
    screen.blit(letter_text, (letter_x, letter_y))
    typing_speed_text = font.render(f"Typing Speed: {typing_speed:.2f}", True, RED)
    screen.blit(typing_speed_text, (0, HEIGHT - FONT_SIZE*3))

    # Update the display
    pygame.display.update()

# Show the "you lose" message
lose_text = font.render("You Lose!", True, RED)
screen.blit(lose_text, (WIDTH // 2 - FONT_SIZE * 2, HEIGHT // 2 - FONT_SIZE))
pygame.display.update()
# Set up the "restart" button
button_text = font.render("Restart", True, WHITE)
button_width, button_height = button_text.get_size()
button_x = (WIDTH - button_width) // 2
button_y = (HEIGHT - button_height) // 2 + FONT_SIZE * 2
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# Show the "you lose" message and restart button
lose_text = font.render("You Lose!", True, RED)
screen.blit(lose_text, (WIDTH // 2 - FONT_SIZE * 2, HEIGHT // 2 - FONT_SIZE))
screen.blit(button_text, (button_x, button_y))
pygame.display.update()

# Wait for a few seconds before allowing restart
time.sleep(1)

# Restart loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                letter = chr(random.randint(65, 90))
                letter_x = random.randint(0, WIDTH - FONT_SIZE)
                letter_y = 0
                speed = 0.01
                start_time = time.time()
                typing_speed = 0
                running = True

    # Start new game loop
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.unicode == letter:
                    letter = chr(random.randint(65, 90))
                    letter_x = random.randint(0, WIDTH - FONT_SIZE)
                    letter_y = 0
                    speed += 0.001
                    typing_speed = 1 / (time.time() - start_time)
                    start_time = time.time()

        # Update the variables
        letter_y += speed

        # Check if the letter has reached the bottom of the screen
        if letter_y > HEIGHT:
            running = False

        # Draw the screen
        screen.fill(BLACK)
        letter_text = font.render(letter, True, WHITE)
        screen.blit(letter_text, (letter_x, letter_y))
        typing_speed_text = font.render(f"Typing Speed: {typing_speed:.2f}", True, RED)
        screen.blit(typing_speed_text, (0, HEIGHT - FONT_SIZE*2))

        # Update the display
        pygame.display.update()

    # Show the "you lose" message and restart button again
    screen.blit(lose_text, (WIDTH // 2 - FONT_SIZE * 2, HEIGHT // 2 - FONT_SIZE))
    screen.blit(button_text, (button_x, button_y))
    pygame.display.update()

    # Wait for a few seconds before allowing restart
    time.sleep(0.1)

# Wait for a few seconds before quitting
time.sleep(1)


pygame.quit()
