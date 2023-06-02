import pygame
import random

# Start pygame
pygame.init()

# Setting up game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Squares all round")

# Global variables
colors = []  # List of colors to be added
target_index = 0  # The target square that will differ in width
lives = 3
score = 0
game_running = False
first_try = True
game_over_screen = False

# Checkerboard size configuration
tile_size = 100

# Game squares configuration
square_size = 100
square_distance = 60  # Distance between squares

# Generates four random colors with varying width
def draw_random_colors():
    global colors, target_index

    colors = []
    target_index = random.randint(0, 3)  # Picking which square will be the odd one (changes per round)

    for i in range(4):  # NOTE to self: 0-3, 0 incl
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        if i == target_index:
            if random.random() < 0.5:
                width = random.randint(80, 99)
            else:
                width = random.randint(101, 120)
            colors.append((red, green, blue, width))
        else:
            width = 100  # random.randint(40, 80) # OBS! If changed, make sure to not have an overlap with the target_index
            colors.append((red, green, blue, width))


def check_guess(clicked_index): ## add return statement to be tested
    global lives, score

    if clicked_index == target_index:
        #print("Congratulations! You guessed correctly")
        score += 1
        screen.fill((0, 255, 0))  # Set screen color to green
        text_object("Congratulations! You guessed correctly", (screen_width // 2, screen_height // 2))
        text_display()
    else:
        #print("Oops! That's not the correct color. Try again")
        lives -= 1
        screen.fill((255, 0, 0))  # Set screen color to red
        text_object("Oops! That's not the correct color. Try again", (screen_width // 2, screen_height // 2))
        text_display()

    if lives == 0:
        game_over()


def game_over():
    global game_over_screen
    game_over_screen = True


def restart_game():
    global lives, score, game_running, game_over_screen, first_try
    lives = 3
    score = 0
    game_running = False
    game_over_screen = False
    first_try = False
    draw_random_colors()


def quit_game():
    pygame.quit()


def retry_choice():
    global game_over_screen
    game_over_screen = False
    restart_game()


# Position of squares on screen
def generate_x_y():
    x = (screen_width - (square_size * 4 + square_distance * 3)) // 2  # // = no decimals (integer division)
    y = (screen_height - square_size) // 2
    return x, y


# Displaying text on the screen
def text_object(text_message, pos):
    font = pygame.font.Font(None, 48)
    text_surface = font.render(text_message, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=pos)
    screen.blit(text_surface, text_rect)


def text_display():
    pygame.display.update()  # Update the screen to show the change
    pygame.time.wait(500)  # Display the text for 1 second


# Defining the size and position of the start button
def button_start_object():
    button_width, button_height = 350, 100
    x = (screen_width - button_width) // 2
    y = (screen_height - button_height) // 2
    return pygame.Rect(x, y, button_width, button_height)


# Defining the size and position of the retry button
def button_retry_object():
    button_width, button_height = 150, 50
    x = (screen_width - 550) // 2
    y = (screen_height + 450) // 2
    return pygame.Rect(x, y, button_width, button_height)


# Defining the size and position of the quit button
def button_quit_object():
    button_width, button_height = 150, 50
    x = (screen_width + 250) // 2
    y = (screen_height + 450) // 2
    return pygame.Rect(x, y, button_width, button_height)


# Defining the size of the game-squares
def square_objects(x, y, width):
    return pygame.Rect(x + (square_size - width) // 2, y, width, square_size)


# Generate initial colors
draw_random_colors()

# Game loop OBSSSSSSSSSSS ## make this into a function! look up if __name__ == "__main__" to start up game
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if not game_running and not game_over_screen:
                button_rect = button_start_object()
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    game_running = True
            elif game_over_screen:
                retry_button_rect = button_retry_object()
                quit_button_rect = button_quit_object()
                mouse_pos = pygame.mouse.get_pos()
                if retry_button_rect.collidepoint(mouse_pos):
                    retry_choice()
                elif quit_button_rect.collidepoint(mouse_pos):
                    quit_game()
            else:
                # Check if the player clicked on one of the color options
                mouse_pos = pygame.mouse.get_pos()
                x, y = generate_x_y()

                for i, color in enumerate(colors):
                    width = color[3]  # Extracting the width from color tuples and making it into its own variable
                    option_object = square_objects(x, y, width)  # Making "hit-boxes" for the squares
                    if option_object.collidepoint(mouse_pos):
                        check_guess(i)
                        draw_random_colors()
                        break

                    x += square_size + square_distance

    # Draw checkerboard background
    for row in range(screen_height // tile_size):
        for col in range(screen_width // tile_size):
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, (100, 100, 100), (col * tile_size, row * tile_size, tile_size, tile_size))
            else:
                pygame.draw.rect(screen, (50, 50, 50), (col * tile_size, row * tile_size, tile_size, tile_size))

    if not game_running:
        # Draw "Start game" button
        button_rect = button_start_object()
        pygame.draw.rect(screen, (0, 0, 255), button_rect)
        if first_try:
            text_object("Start game", (screen_width // 2, screen_height // 2))
        else:
            text_object("Try again", (screen_width // 2, screen_height // 2))
    elif game_over_screen:
        # Draw "Retry" and "Quit" buttons
        retry_button_rect = button_retry_object()
        quit_button_rect = button_quit_object()

        pygame.draw.rect(screen, (0, 0, 255), retry_button_rect)
        pygame.draw.rect(screen, (255, 0, 0), quit_button_rect)
        end_button_x = screen_width // 2
        end_button_y = (screen_height + 500) // 2
        text_object("Retry", (end_button_x - 200, end_button_y))
        text_object("Quit", (end_button_x + 200, end_button_y))

    else:
        # Drawing squares for lives
        life_square_size = 20  # Note: width AND height
        life_square_distance = 10
        life_square_color = (255, 0, 0)
        life_square_x, life_square_y = 10, 10 # Position x-axis and y-axis

        for i in range(lives):
            life_square_rect = pygame.Rect(life_square_x, life_square_y, life_square_size, life_square_size)
            pygame.draw.rect(screen, life_square_color, life_square_rect)
            life_square_x += life_square_size + life_square_distance

        # Drawing color options
        x, y = generate_x_y()

        # Making the squares appear in a line
        for i in colors:
            width = i[3]  # Extracting the width from color and making it into its own variable
            option_object = square_objects(x, y, width)
            pygame.draw.rect(screen, i[:3], option_object)  # Draws the square with the specified colors
            x += square_size + square_distance

    # Update display
    pygame.display.update()

# Quit game
pygame.quit()