import arcade
import random

SPRITE_SCALING = 0.5


SCREEN_WIDTH = 1215
SCREEN_HEIGHT = 800
SCREEN_TITLE = "EDUCATIONAL GAME"


PLAYER_MOVEMENT_SPEED = 7
JUMP_SPEED = 15
GRAVITY = 1
WALL_FRICTION = 0.7


class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # if self.left < 0:
        #     self.left = 0
        # elif self.right > SCREEN_WIDTH - 1:
        #     self.right = SCREEN_WIDTH - 1

        # if self.bottom < 0:
        #     self.bottom = 0
        # elif self.top > SCREEN_HEIGHT - 1:
        #     self.top = SCREEN_HEIGHT - 1


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Our Scene Object
        self.scene = None

        arcade.set_background_color(arcade.color.AERO_BLUE)

        # Variables that will hold sprite list
        self.player_list = None

        # Set up player info
        self.player_sprite = None
        self.player_list = None
        self.ground_list = None
        self.physics_engine = None
        self.camera = None

    def setup(self):

        self.scene = arcade.Scene()
        # Sprite List
        # self.player_list = arcade.SpriteList()
        # self.ground_list = arcade.SpriteList()
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash = True)

        # Set up player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING * 2)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 130
        # self.player_list.append(self.player_sprite)
        self.scene.add_sprite("Player", self.player_sprite)

        # Set up camera
        self.camera = arcade.Camera(self.width, self.height)

        for x in range(32, SCREEN_WIDTH * 2, 64):
            # Bottom edge
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            # self.ground_list.append(wall)
            self.scene.add_sprite("Walls", wall)

        # Set up physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene["Walls"])
            
    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        # self.player_list.draw()
        # self.ground_list.draw()

        self.scene.draw()

        # Activate camera
        self.camera.use()


    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player
        # self.player_list.update()

        # Physics Update
        self.physics_engine.update()

        # Position Camera
        self.center_camera_to_player()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        if key == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        # If a player releases a key, zero out the speed.
        # This doesn't work well if multiple keys are pressed.
        # Use 'better move by keyboard' example if you need to
        # handle this.
        if key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def center_camera_to_player(self):
        
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)  

        player_centered = screen_center_x, screen_center_y
        self.camera.move_to(player_centered)

        
def main():
    window = MyGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
