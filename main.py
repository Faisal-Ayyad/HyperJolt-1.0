import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set the width and height of the screen
WIDTH = 700
HEIGHT = 500

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Set the caption of the screen
pygame.display.set_caption("My Game")

# Set up the player
player_width = 50
player_height = 50
player_x = 50
player_y = 50
player_speed = 5

# Set up the obstacles
obstacles = [
    (200, 200, 100, 100),
    (400, 300, 50, 50),
    (500, 100, 75, 75)
]

# Set up the levels
levels = [
    obstacles,
    [(100, 100, 75, 75)],
    [(400, 200, 50, 50), (200, 300, 100, 100)],
    [(300, 100, 50, 50), (100, 300, 75, 75)],
    [(100, 200, 75, 75), (400, 300, 50, 50)],
    [(200, 100, 100, 100), (500, 300, 75, 75)],
    [(100, 300, 75, 75), (400, 200, 50, 50), (500, 100, 75, 75)],
    [(200, 200, 100, 100), (400, 300, 50, 50), (500, 100, 75, 75), (300, 400, 75, 75)],
    [(100, 100, 75, 75), (500, 400, 100, 100)],
    [(50, 50, 50, 50)]
]

# Set up the current level
current_level = 0

# Set up the clock
clock = pygame.time.Clock()

# Set up the game loop
done = False

while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Check for collisions with obstacles
    for obstacle in levels[current_level]:
        if player_x < obstacle[0] + obstacle[2] and player_x + player_width > obstacle[0] and player_y < obstacle[1] + \
                obstacle[3] and player_y + player_height > obstacle[1]:
            player_x = 50
            player_y = 50

    # Check if the player has reached the end of the level
    if player_x > WIDTH - player_width:
        if current_level == len(levels) - 1:
            print("You win!")
            done = True
        else:
            current_level += 1
            player_x = 50

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, BLUE, [player_x, player_y, player_width, player_height])

    # Draw the obstacles
    for obstacle in levels[current_level]:
        pygame.draw.rect(screen, BLACK, obstacle)

    # Update the screen
    pygame.display.update()

    # Set the game's frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
