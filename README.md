# color-matching
A color matching game where the player matches a target color using a selection of colors presented on the screen. The game starts with a simple interface that displays the target color on one side of the screen and a selection of colors on the other side of the screen. The player needs to click or tap on the color that matches the target color using a color palette. Color palette will be relatively close to the target color. Either options will be given as a palette of 4-6 colours, or maybe an entire color wheel where the score is calculated by the distance from the target color - however how this distance is calculated needs some Googling in the upcoming week. Ideas for scoring  / point deductions are welcome, e.g. time-constraints, incorrect choices etc. 

# Notes
- This game will be programmed in Python
- I have no experience with Python
- Should be fine

**DOCUMENTATION:**

draw_random_colors()
    
Generates a list of four random colors represented as RGB (red-green-blue) values.

    Returns:
    - colors: A list of four tuples, where each tuple represents an RGB color.
              The (integer) values for red, green, and blue range from 0 to 255.

    Example:
    draw_random_colors()
    [(45, 0, 128), (64, 193, 8), (128, 125, 36), (0, 0, 255)]
