import pygame
import random

# [] lists NOTE! Ordered but modifiable, add/remove/reorder. Can index but not search directly by key (no key in a list)
# {} dictionaries NOTE! Not ordered and no duplicates - but you can search for the key
     # dictionary = {"apples": 3, "oranges": -2, "bananas": 90}
     # key = apples, 3 = values
     # e.g. print(dictionary["apples"]

# {} sets # NOTE! not ordered (like dictionaries), but no keys. Cannot contain duplicate
# () tuples NOTE! more permanent, cannot edit after creation. wipe and start over
# Start pygame
pygame.init()

# Setting up game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Squares all round")

# Global variables
colors = [] # list of colors to e added NOTE TO SELF: Still relevant?
target_index = 0 # defining the odd square out
lives = 3
score = 0
heart_symbol = "\u2665"  # Unicode character for heart symbol

# screen_color = (0, 0, 0) # Initial screen color
# Checkerboard pattern configuration
tile_size = 100

square_size = 100
square_distance = 60 # Distance between squares

def draw_random_colors(): # Generates four random colors with varying width
#add random seed for testing, add seed as optional argument for testing
    global colors, target_index

    colors = []
    target_index = random.randint(0, 3) #both inclusive in randint = 0, 1, 2, 3 NOTE TO self: usually 0 incl, second excl

    for i in range(4): # NOTE to self: 0-3, 0 incl
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        if i == target_index:
            width = random.randint(90, 110) #NOTE TO SELF - cannot include the width below
            colors.append((red, green, blue, width))
            # append(colors, width)
        else:
            width = 100 # random.randint(40, 80)
            colors.append((red, green, blue, width))

def check_guess(clicked_index):
    '''
    6he funsiton does htis
    :param clicked_index: do this for all aprameters
    :return:
    '''
    global lives, score
### add return statement to be tested
    if clicked_index == target_index:
        print("Congratulations! You guessed correctly")
        score += 1
        screen.fill((0, 255, 0))  # Set screen color to green
    else:
        print("Oops! That's not the correct color. Try again")
        lives -= 1
        screen.fill((255, 0, 0))  # Set screen color to red

    pygame.display.update()  # Update the screen to show the color change

    pygame.time.wait(500)  # Wait for 1 second

    if lives == 0:
        game_over()
        pygame.quit()
check_guess()
def game_over(): # Displays game over screen with the final score

    print("Game Over")
    print("Final Score:", score) #NOTE TO SELF NOT WORKING?

def generate_x_y(): # Position of squares on screen
    x = (screen_width - (square_size * 4 + square_distance * 3)) // 2  # / = normal division, // = no decimals (integer division)
    y = (screen_height - square_size) // 2
    return x, y

# Generate initial colors
draw_random_colors()
### make this into a function! look up if __name__ == "__main__" to start up game
# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            # Check if the player clicked on one of the color options
            mouse_pos = pygame.mouse.get_pos()
            x, y = generate_x_y()

            for i in range(4):
                option_rect = pygame.Rect(x, y, square_size, square_size) # Making "hit-boxes" for the squares
                if option_rect.collidepoint(mouse_pos):
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

    # Incorporate heart symbol as lives in the game
    # Drawing squares for lives
    life_square_size = 20 # width AND height
    life_square_distance = 10
    life_square_color = (255, 0, 0)
    life_square_x = 10 # Position x-axis
    life_square_y = 10 # Position y-axis

    for i in range(lives):
        life_square_rect = pygame.Rect(life_square_x, life_square_y, life_square_size, life_square_size)
        pygame.draw.rect(screen, life_square_color, life_square_rect)
        life_square_x += life_square_size + life_square_distance

    # Drawing color options
    x, y = generate_x_y()

    for i, color in enumerate(colors): # making the squares appear in a line
        width = color[3] #extracting the width from color and making it into its own variable
        option_rect = pygame.Rect(x + (square_size - width) // 2, y, width, square_size) #defines size of the square
        pygame.draw.rect(screen, color[:3], option_rect) # draws the square with the specified colors (:3 = all values before the third index, incl 0)
        x += square_size + square_distance

    # Update display
    pygame.display.update()

# Quit game
pygame.quit()


## your_package = name of package
## actual_app = name of app
# test_module 1 = if you call it test python will recognize
# requirement.txt tells you the packages that need to be installed to run your package
