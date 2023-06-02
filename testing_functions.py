import pygame
import random
from squaresgame import SquaresAllaRound

def test_square_lvl_progression(seed_number=None):
    """
    Test function for the square_lvl_progression method of the SquaresAllAround class.

    This test verifies that the colors generated for each level are within the proper range (50-255) and that the target color's width falls within the correct range for each level.

    Parameters:
        seed_number (int): Optional seed number for random generation. If provided, the test will be reproducible.

    Output:
        Prints the level ranges for the target width and verifies their correctness.

    Raises:
        AssertionError: If any of the color components (red, green, blue) are outside the range (50-255) or if the target width is outside the correct range for a level.
    """

    game = SquaresAllaRound()
    seed = seed_number  # Set a specific seed for reproducibility

    # Generate colors with the specified seed
    game.square_lvl_progression(seed)

    # Verify that the colors are within the proper range (50-255)
    for color in game.colors:
        red, green, blue, _ = color
        assert 50 <= red <= 255
        assert 50 <= green <= 255
        assert 50 <= blue <= 255

    for lvl in range(1, 8):
        game.level = lvl
        game.square_lvl_progression(seed)

        # Verify that the target color has the correct width range
        target_width = game.colors[game.target_index][3]

        print(f"Level {lvl}:")
        print("Target Width Range (Narrow):", game.level_narrow[lvl][0], "-", game.level_narrow[lvl][-1])
        print("Target Width Range (Wide):", game.level_wide[lvl][0], "-", game.level_wide[lvl][-1])
        print("Target Width:", target_width)
        print()

        assert (game.level_narrow[lvl][0] <= target_width <= game.level_narrow[lvl][-1]) or \
               (game.level_wide[lvl][0] <= target_width <= game.level_wide[lvl][-1])

        # Verify that the non-target colors have a width of 100
        for i, color in enumerate(game.colors):
            if i != game.target_index:
                assert color[3] == 100

    print("square_lvl_progression function passed the test!")

def test_squares_all_around():
    """
        Test function for the SquaresAllaRound class.

        This test function covers multiple methods of the SquaresAllaRound class and prints relevant information for interpretation.

        Output:
            - Score and lives after testing the check_guess method with correct and incorrect guesses.
            - Lives, score, level, game_running, and game_over_screen attributes after testing the restart_game method.
            - Information about the text_object, button_object, and square_objects methods.
    """
    pygame.init()

    game = SquaresAllaRound()

    # Test check_guess()
    game.target_index = 0  # Set target index for testing
    game.check_guess(0)  # Correct guess
    print("Score:", game.score)
    print("Lives:", game.lives)

    game.target_index = 1  # Set target index for testing
    game.check_guess(2)  # Incorrect guess
    print("Score:", game.score)
    print("Lives:", game.lives)

    # Test restart_game()
    game.restart_game()
    print("Lives:", game.lives)
    print("Score:", game.score)
    print("Level:", game.level)
    print("Game Running:", game.game_running)
    print("Game Over Screen:", game.game_over_screen)

    # Test text_object()
    game.text_object("Test Message", (game.center_x, game.center_y))

    # Test button_object()
    button_rect = game.button_object(0)
    print("Button Rectangle:", button_rect)

    # Test square_objects()
    square_rect = game.square_objects(game.square_x, game.square_y, 80)
    print("Square Rectangle:", square_rect)

    pygame.quit()


# Run the tests
test_square_lvl_progression(42)
test_square_lvl_progression()
test_squares_all_around()