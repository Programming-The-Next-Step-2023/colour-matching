import random

# Function =  Generating four random colors
colors = []
def draw_random_colors():
    for rgb in range(4):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        colors.append((red, green, blue))
    return(colors)


# Test
def test_draw_random_colors():
    test_cols = draw_random_colors()

    # Check if the length of colors is 4
    assert len(test_cols) == 4

    # Check if all colors are unique
    assert len(set(tuple(color) for color in test_cols)) == 4

    # Check if all RGB values are between 0 and 255
    for color in test_cols:
        for value in color:
            assert 0 <= value <= 255

    print("Test passed!")

test_draw_random_colors()