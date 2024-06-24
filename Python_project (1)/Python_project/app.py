import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Litter Legends")
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Load and scale images
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the image
image_path = os.path.join(current_dir, "static", "Assets", "player.png")

# Load the image
player_image = pygame.image.load(image_path)
player_image = pygame.transform.scale(player_image, (player_image.get_width() // 2, player_image.get_height() // 2))

# Load background image
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the background image
background_image_path = os.path.join(current_dir, "static", "Assets", "classic_background.png")

# Load the background image
background_image = pygame.image.load(background_image_path)

background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load recyclable trash images from the folder
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the recyclable_trash folder
recyclable_trash_folder = os.path.join(current_dir, "static", "Assets", "recyclable_trash")
recyclable_trash_images = []
for filename in os.listdir(recyclable_trash_folder):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        image_path = os.path.join(recyclable_trash_folder, filename)
        image = pygame.image.load(image_path)
        scaled_width = image.get_width() // 4
        scaled_height = image.get_height() // 4
        scaled_size = (int(scaled_width * 1.0), int(scaled_height * 1.0))
        image = pygame.transform.scale(image, scaled_size)
        recyclable_trash_images.append(image)

# Load non-recyclable trash images from the folder
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the non_recyclable_trash folder
non_recyclable_trash_folder = os.path.join(current_dir, "static", "Assets", "non_recyclable_trash")
non_recyclable_trash_images = []
for filename in os.listdir(non_recyclable_trash_folder):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        image_path = os.path.join(non_recyclable_trash_folder, filename)
        image = pygame.image.load(image_path)
        scaled_width = image.get_width() // 4
        scaled_height = image.get_height() // 4
        scaled_size = (int(scaled_width * 1.0), int(scaled_height * 1.0))
        image = pygame.transform.scale(image, scaled_size)
        non_recyclable_trash_images.append(image)

# Load and play background music
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the background music file
background_music_path = os.path.join(current_dir, "static", "Assets", "background_music.mp3")

# Load the background music
pygame.mixer.music.load(background_music_path)
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

# Define fonts
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)
button_font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 72)
name_font = pygame.font.Font(None, 48)
points_font = pygame.font.Font(None, 36)

# Define the player
player_rect = player_image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 10))

# Define the trash items
trash_items = [
    {"image": image, "points": 2, "type": "recyclable"} for image in recyclable_trash_images
] + [
    {"image": image, "points": 3, "type": "non_recyclable"} for image in non_recyclable_trash_images
] + [
    {"image": image, "points": 3, "type": "non_recyclable"} for image in non_recyclable_trash_images
]
random.shuffle(trash_items)

def populate_trash_items():
    global trash_items
    trash_items = [
        {"image": image, "points": 2, "type": "recyclable"} for image in recyclable_trash_images
    ] + [
        {"image": image, "points": 3, "type": "non_recyclable"} for image in non_recyclable_trash_images
    ] + [
        {"image": image, "points": 3, "type": "non_recyclable"} for image in non_recyclable_trash_images
    ]
    random.shuffle(trash_items)

if trash_items:
    current_trash = trash_items.pop(0)
else:
    populate_trash_items()
    current_trash = trash_items.pop(0)

trash_rect = current_trash["image"].get_rect(midtop=(random.randint(20, WIDTH - 20), 0))

# Initialize the score, level, and misses
score = 0
level = 1
misses = 0
max_misses = 3
level_targets = [5, 10, 15]

# Initialize recyclable and non-recyclable counts
recyclable_count = 0
non_recyclable_count = 0

# Points display variables
points_display_time = 30  # Time to display points on the screen
points_display_counter = 0
points_display_value = 0

# Initial trash fall speed
trash_fall_speed = 2

# Button dimensions
button_width = 200
button_height = 50
button_x = WIDTH // 2 - button_width // 2

# Game states
GET_NAME, START, PLAYING, GAME_OVER = 0, 1, 2, 3
game_state = GET_NAME

# Player name
player_name = ""

def draw_get_name_screen():
    window.blit(background_image, (0, 0))
    prompt_text = font.render("Let's see how much trash you collect!!", True, GREEN)
    prompt_rect = prompt_text.get_rect(center=(WIDTH // 2, HEIGHT // 9 ))
    window.blit(prompt_text, prompt_rect)

    title_text = title_font.render("Enter Your Name", True, GREEN)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT * 5 // 6.4))
    window.blit(title_text, title_rect)

    name_text = name_font.render(player_name, True, BLACK)
    name_rect = name_text.get_rect(center=(WIDTH // 2, HEIGHT * 5 // 5.8))
    window.blit(name_text, name_rect)

    prompt_text = font.render("Press Enter Now", True, GRAY)
    prompt_rect = prompt_text.get_rect(center=(WIDTH // 2, HEIGHT * 5 // 5.3))
    window.blit(prompt_text, prompt_rect)

    pygame.display.update()

def draw_start_screen():
    window.blit(background_image, (0, 0))

    title_text = title_font.render("Litter ", True, GREEN)  # Green color for "Litter"
    title_text2 = title_font.render("Legends", True, RED)   # Red color for "Legends"
    title_rect = title_text.get_rect(midtop=(WIDTH // 2 - 140, HEIGHT // 9))  # Move up and reduce spacing
    title_rect2 = title_text2.get_rect(midtop=(WIDTH // 2 + 80, HEIGHT // 9))  # Move up and reduce spacing
    window.blit(title_text, title_rect)
    window.blit(title_text2, title_rect2)

    # Start button
    start_button_text = button_font.render("Start Game", True, BLACK)
    start_button_rect = pygame.Rect(button_x, HEIGHT // 2 + 120, button_width, button_height)  # Move down
    pygame.draw.rect(window, GRAY,
                     start_button_rect)
    start_button_text_rect = start_button_text.get_rect(center=start_button_rect.center)
    window.blit(start_button_text, start_button_text_rect)

    
    # Recyclable count
    recyclable_text = font.render(f"Recyclable: {recyclable_count}", True, GREEN)
    recyclable_rect = recyclable_text.get_rect(midleft=(20, HEIGHT - 100))  # Adjusted position

    # Non-recyclable count
    non_recyclable_text = font.render(f"Non-Recyclable: {non_recyclable_count}", True, RED)
    non_recyclable_rect = non_recyclable_text.get_rect(midleft=(20, HEIGHT - 50))  # Adjusted position

    window.blit(recyclable_text, recyclable_rect)
    window.blit(non_recyclable_text, non_recyclable_rect)
 

    pygame.display.update()

def draw_game_over_screen():
    window.blit(background_image, (0, 0))

    game_over_text = game_over_font.render("Great Game! Game Over", True, BLACK)
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(game_over_text, game_over_rect)

    score_text = font.render(f"{player_name}'s Score is: {score}", True, GRAY)
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 10 ))
    window.blit(score_text, score_rect)

    fact_text = font.render("Fact:Recycling one ton of plastic saves 5,774 kWh of energy", True, GREEN)
    fact_rect = fact_text.get_rect(center=(WIDTH // 2, HEIGHT // 7))
    window.blit(fact_text, fact_rect)

    button_text = button_font.render("New Game?", True, BLACK)
    button_rect = pygame.Rect(button_x, HEIGHT // 1.8 + 100, button_width, button_height)

    pygame.draw.rect(window, GRAY, button_rect)
    button_text_rect = button_text.get_rect(center=button_rect.center)
    window.blit(button_text, button_text_rect)

    pygame.display.update()

def display_level_up_message(new_level):
    level_up_text = font.render(f"Level increased to {new_level}!", True, BLACK)
    level_up_rect = level_up_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    window.blit(level_up_text, level_up_rect)
    pygame.display.update()
    pygame.time.delay(500)  # Display the message for 1 second

def check_level_up():
    global level, trash_fall_speed
    if level <= len(level_targets) and score >= level_targets[level - 1]:
        previous_level = level
        level += 1
        trash_fall_speed += 1  # Increase the fall speed for the next level
        display_level_up_message(level)  # Display the level-up message

def reset_game():
    global score, level, trash_fall_speed, misses, current_trash, trash_rect, recyclable_count, non_recyclable_count
    score = 0
    level = 1
    trash_fall_speed = 3
    misses = 0
    recyclable_count = 0
    non_recyclable_count = 0
    if trash_items:
        random.shuffle(trash_items)
        current_trash = trash_items.pop(0)
    else:
        # Handle the case when trash_items is empty
        populate_trash_items()
        current_trash = trash_items.pop(0)
    trash_rect = current_trash["image"].get_rect(midtop=(random.randint(20, WIDTH - 20), 0))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_state == GET_NAME:
                    game_state = START
                elif game_state == GAME_OVER:
                    player_name = ""
                    reset_game()
                    game_state = GET_NAME
            elif event.key == pygame.K_BACKSPACE:
                if game_state == GET_NAME:
                    player_name = player_name[:-1]
            else:
                if game_state == GET_NAME:
                    player_name += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if game_state == START:
                if button_x <= mouse_pos[0] <= button_x + button_width and HEIGHT // 2 <= mouse_pos[1] <= HEIGHT // 2 + button_height:
                    game_state = PLAYING
            elif game_state == GAME_OVER:
                if button_x <= mouse_pos[0] <= button_x + button_width and HEIGHT // 2 + 150 <= mouse_pos[1] <= HEIGHT // 2 + 150 + button_height:
                    player_name = ""
                    reset_game()
                    game_state = GET_NAME

    if game_state == GET_NAME:
        draw_get_name_screen()
    elif game_state == START:
        draw_start_screen()
    elif game_state == PLAYING:
        # Move the trash
        trash_rect.y += trash_fall_speed
        if trash_rect.top > HEIGHT:
            misses += 1
            if misses >= max_misses:
                game_state = GAME_OVER
            else:
                if not trash_items:
                    populate_trash_items()
                current_trash = trash_items.pop(0)
                trash_rect = current_trash["image"].get_rect(midtop=(random.randint(20, WIDTH - 20), 0))

        # Move the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= 5
        if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
            player_rect.x += 5

        # Check for collision
        if player_rect.colliderect(trash_rect):
            if current_trash["type"] == "recyclable":
                score += 2  # Increase score for recyclable items
                points_display_value = 2
                points_color = GREEN
            else:
                score += 3  # Increase score for non-recyclable items
                points_display_value = 3
                points_color = RED

            points_display_counter = points_display_time  # Reset the display counter

            if current_trash["type"] == "recyclable":
                recyclable_count += 1
            else:
                non_recyclable_count += 1

            if not trash_items:
                populate_trash_items()
            current_trash = trash_items.pop(0)
            trash_rect = current_trash["image"].get_rect(midtop=(random.randint(20, WIDTH - 20), 0))
            check_level_up()  # Check if the player has leveled up

        # Clear the window
        window.blit(background_image, (0, 0))

        # Draw the player
        window.blit(player_image, player_rect.topleft)

        # Draw the trash
        window.blit(current_trash["image"], trash_rect.topleft)

        # Draw the score, level, and misses
        score_text = font.render(f"Score: {score}", True, BLACK)
        window.blit(score_text, (10, 10))
        level_text = font.render(f"Level: {level}", True, BLACK)
        window.blit(level_text, (WIDTH - 150, 10))
        misses_text = font.render(f"Misses: {misses}/{max_misses}", True, BLACK)
        window.blit(misses_text, (WIDTH // 2 - 75, 10))

        # Draw the recyclable and non-recyclable counts
        recyclable_text = font.render(f"Recyclable: {recyclable_count}", True, GREEN)
        window.blit(recyclable_text, (10, 50))
        non_recyclable_text = font.render(f"Non-Recyclable: {non_recyclable_count}", True, RED)
        window.blit(non_recyclable_text, (10, 90))

        # Display points on catching an item
        if points_display_counter > 0:
            points_text = points_font.render(f"+{points_display_value}", True, points_color)
            window.blit(points_text, (player_rect.centerx - points_text.get_width() // 2, player_rect.top - 30))
            points_display_counter -= 1

        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 FPS

    elif game_state == GAME_OVER:
        draw_game_over_screen()

# Quit
pygame.quit()
        