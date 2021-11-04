import arcade

MOVEMENT_SPEED = 5

class Player(arcade.Sprite):
    

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > 1280 - 1:
            self.right = 1280 - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > 720 - 1:
            self.top = 720 - 1

class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AERO_BLUE)

        # Variables that will hold sprite list
        self.player_list = None

        # Set up player info
        self.player_sprite = None

    def setup(self):
        # Sprite List
        self.player_list = arcade.SpriteList()

        # Set up player
        self.player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png", 1)

        self.player_sprite.center_x = self.width / 2
        self.player_sprite.center_y = self.height / 2
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.player_list.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        # If the player presses a key, update the speed
        if key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        # If a player releases a key, zero out the speed.
        # This doesn't work well if multiple keys are pressed.
        # Use 'better move by keyboard' example if you need to
        # handle this.
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0
        

def main():
    window = MyGameWindow(1280, 720, "My Game Window")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
