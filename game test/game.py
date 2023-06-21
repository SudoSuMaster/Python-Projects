import pygame
import random
import math

# Initialize pygame
pygame.init()

# Set up the game window
window_width = 1000  # Increased width
window_height = 800  # Increased height
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Arrow Shooting Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the player
player_size = 30  # Decreased player size
player_x = window_width // 2 - player_size // 2
player_y = window_height - player_size - 10
player_speed = 1  # Decreased player speed
player_facing = "up"  # Initial player facing direction

# Set up the bullet
bullet_size = 10
bullet_speed = 10
bullet_list = []

# Set up the zombie
zombie_size = 30  # Decreased zombie size
zombie_list = []
num_zombies = 5
zombies_per_wave = 5
zombie_speed = 0.1  # Decreased zombie speed even more
zombies_killed = 0
wave = 1
zombie_hit_delays = []
zombie_last_hit_times = []

# Set up the game state
running = True
game_over = False
play_again = False

# Set up the player health
player_health = 300

# Set up the score and kill count
score = 0
total_zombies_killed = 0

# Weapons information
weapons_text = "Beta Verion 1.0.2" 

# Available weapons
weapons = [
    {
        "name": "Pistol",
        "damage": 10000,
        "ammo": 9999999999999999999999999999,
        "reload_time": 0.1
    },
    {
        "name": "Shotgun",
        "damage": 50,
        "ammo": 2,
        "reload_time": 2000
    },
    {
        "name": "Machine Gun",
        "damage": 10,
        "ammo": 30,
        "reload_time": 3000
    },
    {
        "name": "Rocket Launcher",
        "damage": 100,
        "ammo": 1,
        "reload_time": 5000
    }
]

current_weapon_index = 0
current_weapon = weapons[current_weapon_index]
current_ammo = current_weapon["ammo"]
reload_time = current_weapon["reload_time"]
last_shot_time = 0

player_image = pygame.image.load("C:/Users/Royaxz/Documents/Py/images.png")  # Replace with the correct image path
player_image = pygame.transform.scale(player_image, (player_size, player_size))

def spawn_zombies():
    zombie_list.clear()
    zombie_hit_delays.clear()
    zombie_last_hit_times.clear()
    for _ in range(num_zombies):
        valid_spawn = False
        while not valid_spawn:
            zombie_x = random.randint(0, window_width - zombie_size)
            zombie_y = random.randint(0, window_height - zombie_size)
            valid_spawn = True

            # Check if the new spawn position is too close to existing zombies
            for other_zombie in zombie_list:
                distance = math.sqrt((zombie_x - other_zombie[0]) ** 2 + (zombie_y - other_zombie[1]) ** 2)
                if distance < zombie_size * 2:  # Adjust the value (zombie_size * 2) as needed
                    valid_spawn = False
                    break

        zombie_list.append([zombie_x, zombie_y, 200])  # Update zombie's health to 75
        zombie_hit_delays.append(random.randint(3000, 5000))
        zombie_last_hit_times.append(0)


def start_new_wave():
        global num_zombies, wave, player_health

        num_zombies += zombies_per_wave
        wave += 1
        player_health = 100
        spawn_zombies()


def shoot():
    global bullet_list, current_ammo, last_shot_time

    now = pygame.time.get_ticks()
    if now - last_shot_time > reload_time:
        if current_ammo > 0:
            bullet_x = player_x + player_size // 2 - bullet_size // 2
            bullet_y = player_y + player_size // 2 - bullet_size // 2

            mouse_x, mouse_y = pygame.mouse.get_pos()
            direction_x = mouse_x - bullet_x
            direction_y = mouse_y - bullet_y
            magnitude = math.sqrt(direction_x ** 2 + direction_y ** 2)

            if magnitude != 0:
                direction_x /= magnitude
                direction_y /= magnitude

            bullet_list.append([bullet_x, bullet_y, direction_x * bullet_speed, direction_y * bullet_speed])

            current_ammo -= 1
            last_shot_time = now


def update_player_position(keys_pressed):
    global player_x, player_y, player_facing

    if keys_pressed[pygame.K_w]:
        player_y -= player_speed
        player_facing = "up"
    if keys_pressed[pygame.K_s]:
        player_y += player_speed
        player_facing = "down"
    if keys_pressed[pygame.K_a]:
        player_x -= player_speed
        player_facing = "left"
    if keys_pressed[pygame.K_d]:
        player_x += player_speed
        player_facing = "right"

    # Keep the player inside the game window
    player_x = max(0, min(player_x, window_width - player_size))
    player_y = max(0, min(player_y, window_height - player_size))


def update_zombie_positions():
    for i, zombie in enumerate(zombie_list):
        zombie_x = zombie[0]
        zombie_y = zombie[1]

        # Calculate the distance between the zombie and the player
        distance = math.sqrt((player_x - zombie_x) ** 2 + (player_y - zombie_y) ** 2)

        # Skip calculations if distance is zero
        if distance == 0:
            continue

        # Calculate the direction vector from the zombie to the player
        dx = (player_x - zombie_x) / distance
        dy = (player_y - zombie_y) / distance

        # Update the zombie position based on the direction vector and speed
        new_x = zombie_x + dx * zombie_speed
        new_y = zombie_y + dy * zombie_speed

        # Check if the new position will cause a collision with other zombies
        collided = False
        for j, other_zombie in enumerate(zombie_list):
            if j != i and math.sqrt((new_x - other_zombie[0]) ** 2 + (new_y - other_zombie[1]) ** 2) < zombie_size:
                collided = True
                break

        if not collided:
            zombie_list[i][0] = new_x  # Update zombie's x position
            zombie_list[i][1] = new_y  # Update zombie's y position


def display_weapon_info():
    font = pygame.font.Font(None, 20)
    weapon_name = current_weapon["name"]
    ammo_count = current_ammo
    weapon_text = f"Weapon: {weapon_name} (Ammo: {ammo_count})"
    text = font.render(weapons_text + weapon_text, True, BLACK)
    window.blit(text, (20, window_height - text.get_height() - 20))




while running:
    window.fill(WHITE)

    if zombies_killed == num_zombies:
        start_new_wave()

    if not game_over:
        keys_pressed = pygame.key.get_pressed()

        # Update player position based on arrow key presses
        if keys_pressed[pygame.K_UP]:
            player_y -= player_speed
            player_facing = "up"
        elif keys_pressed[pygame.K_DOWN]:
            player_y += player_speed
            player_facing = "down"
        elif keys_pressed[pygame.K_LEFT]:
            player_x -= player_speed
            player_facing = "left"
        elif keys_pressed[pygame.K_RIGHT]:
            player_x += player_speed
            player_facing = "right"

        window.blit(player_image, (player_x, player_y))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot()

        update_player_position(keys_pressed)


        def reload_weapon():
            global current_ammo, last_shot_time

            now = pygame.time.get_ticks()
            if now - last_shot_time > reload_time:
                current_ammo = current_weapon["ammo"]
                last_shot_time = now

        # Update bullet positions
        for bullet in bullet_list:
            bullet[0] += bullet[2]
            bullet[1] += bullet[3]

        # Remove bullets that have gone off-screen
        bullet_list = [bullet for bullet in bullet_list if
                       0 <= bullet[0] <= window_width and 0 <= bullet[1] <= window_height]

        # Draw bullets
        for bullet in bullet_list:
            pygame.draw.rect(window, BLACK, (bullet[0], bullet[1], bullet_size, bullet_size))

        # Draw player
        pygame.draw.rect(window, RED, (player_x, player_y, player_size, player_size))

        # Draw zombies
        for zombie in zombie_list:
            pygame.draw.rect(window, BLACK, (zombie[0], zombie[1], zombie_size, zombie_size))

        # Check if bullets hit zombies
        for bullet in bullet_list:
            bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_size, bullet_size)
            for i, zombie in enumerate(zombie_list):
                zombie_rect = pygame.Rect(zombie[0], zombie[1], zombie_size, zombie_size)
                if bullet_rect.colliderect(zombie_rect):
                    zombie[2] -= 25  # Decrease zombie health by 25 per hit
                    score += 25  # Increase score by 25 for each hit
                    if zombie[2] <= 0:
                        zombie_list.pop(i)
                        zombies_killed += 1  # Update the kill count
                        break

        # Check if zombies hit the player
        for i, zombie in enumerate(zombie_list):
            zombie_rect = pygame.Rect(zombie[0], zombie[1], zombie_size, zombie_size)
            player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
            if zombie_rect.colliderect(player_rect):
                now = pygame.time.get_ticks()
                if now - zombie_last_hit_times[i] > zombie_hit_delays[i]:
                    player_health -= 10
                    zombie_last_hit_times[i] = now

        # Draw player health bar
        pygame.draw.rect(window, RED, (20, 20, player_health, 10))

        # Draw score
        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(score), True, BLACK)
        window.blit(text, (20, 50))

        # Draw wave
        text = font.render("Wave: " + str(wave), True, BLACK)
        window.blit(text, (20, 80))

        # Draw zombies killed
        text = font.render("Zombies Killed: " + str(zombies_killed), True, BLACK)
        window.blit(text, (20, 110))

        update_zombie_positions()

        # Check if all zombies are killed
        if len(zombie_list) == 0:
            start_new_wave()

        # Check if player is dead
        if player_health <= 0:
            game_over = True

    # Display weapon info
    display_weapon_info()

    # Update the game display
    pygame.display.update()

# Game over screen
while game_over:
    window.fill(WHITE)

    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, BLACK)
    window.blit(text, (window_width // 2 - text.get_width() // 2, window_height // 2 - text.get_height() // 2))

    text = font.render("Score: " + str(score), True, BLACK)
    window.blit(text, (window_width // 2 - text.get_width() // 2, window_height // 2 + text.get_height() // 2 + 20))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            game_over = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_again = True
                running = False
                game_over = False

# Reset the game state if the player wants to play again
if play_again:
    bullet_list.clear()
    zombie_list.clear()
    num_zombies = 5
    zombies_per_wave = 5
    zombie_speed = 0.1
    zombies_killed = 0
    wave = 1
    zombie_hit_delays.clear()
    zombie_last_hit_times.clear()
    player_health = 100
    score = 0
    total_zombies_killed = 0
    spawn_zombies()
    running = True
    game_over = False
    play_again = False

# Quit the game
pygame.quit()
