import pygame
import random

def generate_game_colors():
    colors = []
    target_index = random.randint(0, 3)

    for _ in range(4):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        # Increase saturation for the target color
        if _ == target_index:
            saturation = random.randint(200, 255)
            colors.append((red + saturation, green + saturation, blue + saturation))
        else:
            saturation = random.randint(0, 100)
            colors.append((red + saturation, green + saturation, blue + saturation))

    return colors, target_index


def draw_colors(colors):
    screen.fill((255, 255, 255))  # Clear the screen with white color

    # Calculate the size and position of each color box
    box_size = 100
    box_margin = 50
    total_width = (box_size + box_margin) * 4
    start_x = (screen_width - total_width) // 2
    start_y = (screen_height - box_size) // 2

    # Draw each color box
    for i, color in enumerate(colors):
        rect = pygame.Rect(start_x + (i * (box_size + box_margin)), start_y, box_size, box_size)
        pygame.draw.rect(screen, color, rect)

    pygame.display.update()  # Update the display
    return screen


def play_game():
    pygame.init()
    global screen, screen_width, screen_height
    screen_width, screen_height = 600, 200
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Saturation Game")

    clock = pygame.time.Clock()

    colors, target_index = generate_game_colors()
    draw_colors(colors)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

            if event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                box_size = 100
                box_margin = 50
                start_x = (screen_width - ((box_size + box_margin) * 4)) // 2
                start_y = (screen_height - box_size) // 2

                for i in range(4):
                    box_x = start_x + (i * (box_size + box_margin))
                    box_y = start_y
                    if box_x <= mouse_x <= box_x + box_size and box_y <= mouse_y <= box_y + box_size:
                        if i == target_index:
                            print("Congratulations! You guessed correctly.")
                        else:
                            print("Oops! That's not the correct color. Try again.")
                        pygame.quit()
                        return

        clock.tick(30)  # Limit frame rate to 30 fps


# Run the game
play_game()
