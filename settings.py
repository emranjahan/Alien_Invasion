class Settings():
    """ A class to store all settings for alien invasion."""

    def __init__(self):

        """ Initialize the game's setting."""
        # Display setting.

        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # Ship settings
        self.ship_speed_factor = 1.5

