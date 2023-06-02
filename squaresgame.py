import pygame
import random

class SquaresAllaRound:
    def __init__(self):
        # Setting up game window
        self.screen_width, self.screen_height = 800, 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Squares All aRound")

        # Global variables
        self.colors = []  # List of colors and widths of the game squares
        self.target_index = 0  # The target square that will differ in width
        self.lives = 3
        self.score = 0
        self.level = 1
        self.game_running = False  # When false, you see the introduction screen
        self.game_over_screen = False

        # Defines the limits for each level
        self.level_narrow = {1: (80, 85), 2: (85, 90), 3: (90, 93), 4: (93, 96), 5: (96, 97), 6: (97, 98), 7: (98, 99)}
        self.level_wide = {1: (115, 120), 2: (110, 115), 3: (107, 110), 4: (104, 107), 5: (103, 104), 6: (102, 103), 7: (101, 102)}

        # Game objects configuration
        self.center_x = self.screen_width // 2
        self.center_y = self.screen_height // 2
        self.screen_center = (self.center_x, self.center_y)

        self.buttons_y_pos = self.center_y + 225
        self.button_width, self.button_height = 150, 50

        self.square_size = 100
        self.square_distance = 60  # Distance between squares
        self.square_x = (self.screen_width - (self.square_size * 4 + self.square_distance * 3)) // 2  # // = no decimals (integer division)
        self.square_y = (self.screen_height - self.square_size) // 2

        self.life_square_size = 30  # Note: width AND height
        self.life_square_distance = 15
        self.life_square_color = (255, 56, 152)
        self.life_square_x, self.life_square_y = 20, 20  # Position x-axis and y-axis

    def square_lvl_progression(self, seed=None):
        """Generates four squares with random colors and with varying width.

        One square will have a different width, and the width is determined by the current level.
        """
        self.colors = []
        self.target_index = random.randint(0, 3)  # Picking which square will be the odd one (changes per round)
        random.seed(seed)

        for i in range(4):
            red = random.randint(50, 255)
            green = random.randint(50, 255)
            blue = random.randint(50, 255)

            if i == self.target_index:
                if random.random() < 0.5:  # If smaller, it is going to be narrow. If larger, the difference is wider. This if-else statement is necessary in order to prevent overlap in square sizes = no difference between squares
                    width = random.randint(self.level_narrow[self.level][0], self.level_narrow[self.level][-1])  # in the dictionary, there's tuples. here it says first and the last of the tuples
                else:  # [-1 = last value]
                    width = random.randint(self.level_wide[self.level][0], self.level_wide[self.level][-1])
                self.colors.append((red, green, blue, width))
            else:
                width = 100
                self.colors.append((red, green, blue, width))

    def check_guess(self, clicked_index):
        """Checks the player's guess and updates the game state accordingly.

        Args:
            clicked_index (int): The index of the color option that the player clicked.
        """
        if clicked_index == self.target_index:
            self.score += 1
            self.screen.fill((0, 100, 0))  # Set screen color to green
            self.text_object("Correct!", self.screen_center)
            self.text_display(500)
        else:
            self.lives -= 1
            self.screen.fill((100, 0, 0))  # Set screen color to red
            self.text_object("Incorrect! Try again", self.screen_center)
            self.text_display(500)

        self.screen.fill((0, 0, 0))
        self.text_object(f'Score: {self.score}', self.screen_center)
        self.text_display(500)

        if self.lives == 0:
            self.screen.fill((0, 0, 0))
            self.text_object("Game Over", self.screen_center)
            self.text_display(1000)
            self.game_over_screen = True

    def restart_game(self):
        """Restarts the game by resetting the game state and generating new colors."""
        self.lives = 3
        self.score = 0
        self.level = 1
        self.game_running = False
        self.game_over_screen = False
        self.square_lvl_progression()

    def text_object(self, text_message, pos):
        """Displays text on the screen at the specified position.

        Args:
            text_message (str): The text to be displayed.
            pos (tuple): The position (x, y) of the text surface center.
        """
        font = pygame.font.Font(None, 48)
        text_surface = font.render(text_message, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=pos)
        self.screen.blit(text_surface, text_rect)

    def text_display(self, ms):
        """Updates the screen and displays the text for the specified duration.

        Args:
            ms (int): The duration in milliseconds to display the text.
        """
        pygame.display.update()  # Update the screen to show the change
        pygame.time.wait(ms)  # Display the text for 'ms' milliseconds

    def button_object(self, x_diff):
        """Creates a button rectangle object at the specified x-axis offset.

        Args:
            x_diff (int): The x-axis offset from the center of the screen.

        Returns:
            pygame.Rect: The button rectangle object.
        """
        x_pos = (self.screen_width - self.button_width + x_diff) // 2
        return pygame.Rect(x_pos, self.buttons_y_pos, self.button_width, self.button_height)

    def square_objects(self, x, y, width):
        """Creates a square rectangle object at the specified position and width.

        Args:
            x (int): The x-coordinate of the square's top-left corner.
            y (int): The y-coordinate of the square's top-left corner.
            width (int): The width of the square.

        Returns:
            pygame.Rect: The square rectangle object.
        """
        return pygame.Rect(x + (self.square_size - width) // 2, y, width, self.square_size)

    def run_game(self):
        """Starts the game loop."""
        # Start pygame
        pygame.init()

        # Generate initial colors
        self.square_lvl_progression()

        self.running = True
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    # If not true, then do this
                    if not self.game_running and not self.game_over_screen:
                        button_rect = self.button_object(0)
                        mouse_pos = pygame.mouse.get_pos()
                        if button_rect.collidepoint(mouse_pos):
                            self.game_running = True
                    elif self.game_over_screen:
                        retry_button_rect = self.button_object(-400)
                        quit_button_rect = self.button_object(400)
                        mouse_pos = pygame.mouse.get_pos()
                        if retry_button_rect.collidepoint(mouse_pos):
                            self.restart_game()
                        if quit_button_rect.collidepoint(mouse_pos):
                            pygame.quit()
                    else:
                        # Check if the player clicked on one of the color options
                        mouse_pos = pygame.mouse.get_pos()
                        x = self.square_x
                        y = self.square_y
                        for i, color in enumerate(self.colors):
                            width = color[3] # Extracting the width from color tuples and making it into its own variable
                            option_object = self.square_objects(x, y, width) # Making "hit-boxes" for the squares
                            if option_object.collidepoint(mouse_pos):
                                self.check_guess(i)
                                self.square_lvl_progression()
                                break
                            x += self.square_size + self.square_distance

            # Update level
            if self.level < 7:
                self.level = 1 + int(abs(self.score / 3))

            self.screen.fill((0, 0, 0))

            if not self.game_running:
                # Displaying start message and draw "Start game" button
                button_rect = self.button_object(0)
                pygame.draw.rect(self.screen, (0, 100, 0), button_rect)
                self.text_object("Start", (self.center_x, self.center_y + 250))
                self.text_object('Welcome to Squares All aRound!', (self.center_x, self.center_y - 200))
                self.text_object('1. Indicate the most wide or narrow square', (self.center_x, self.center_y - 100))
                self.text_object('2. The pink squares represent your lives', self.screen_center)
                self.text_object('Good luck!', (self.center_x, self.center_y + 100))

            elif self.game_over_screen:
                # Display game over message
                self.text_object(f"Final Score: {self.score}", (self.center_x, self.center_y - 100))
                if self.level < 7:
                    self.text_object(f'Progressed to level: {self.level}', self.screen_center)
                else:
                    self.text_object('You reached the final level!', self.screen_center)

                # Draw "Retry" and "Quit" buttons
                retry_button_rect = self.button_object(-400)
                quit_button_rect = self.button_object(400)
                pygame.draw.rect(self.screen, (0, 100, 0), retry_button_rect)
                pygame.draw.rect(self.screen, (100, 0, 0), quit_button_rect)
                self.text_object("Retry", (self.center_x - 200, self.center_y + 250))
                self.text_object("Quit", (self.center_x + 200, self.center_y + 250))

            else:
                # Drawing squares for lives
                life_square_x_pos = self.life_square_x
                for i in range(self.lives):
                    life_square_rect = pygame.Rect(life_square_x_pos, self.life_square_y, self.life_square_size, self.life_square_size)
                    pygame.draw.rect(self.screen, self.life_square_color, life_square_rect)
                    life_square_x_pos += self.life_square_size + self.life_square_distance

                if self.level < 7:
                    self.text_object(f'Level: {self.level}', (80, self.screen_height - 30))
                else:
                    self.text_object('Final level!', (105, self.screen_height - 30))

                # Making the squares appear in a line
                x = self.square_x
                y = self.square_y
                for color in self.colors:
                    width = color[3]  # Extracting the width from color and making it into its own variable
                    option_object = self.square_objects(x, y, width)
                    pygame.draw.rect(self.screen, color[:3], option_object) # Draws the square with the specified colors
                    x += self.square_size + self.square_distance

            # Update display
            pygame.display.update()

        # Quit game
        pygame.quit()

# Run the game
game = SquaresAllaRound()
game.run_game()