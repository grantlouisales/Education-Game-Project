"""
Platformer Game
"""
import arcade
from arcade.camera import Camera
from arcade.scene import Scene
from arcade.sprite import Sprite
from arcade.sprite_list.spatial_hash import check_for_collision_with_list

from constants import *
# from MenuView import *
class Letters():
    
    class Letter(arcade.Sprite):
        def __init__(self, letter, x, y):
            super().__init__(f'resources/letters/letter{letter}.png', center_x=x, center_y=y, scale=.1)
            self.letter = letter

    def __init__(self, scene : Scene):
        self.collection = []
        self.letters = arcade.SpriteList()
        self.scene = scene

    def create_letter(self, letter : str, x, y):
        letter_sprite = self.Letter(letter, x, y)
        self.letters.append(letter_sprite)
        self.scene.add_sprite(f'Letter{letter}', letter_sprite)

    def collect_letter(self, letter : Letter):
        self.collection.append(letter)
        index = self.collection.index(letter) + 1
        letter.center_x, letter.center_y = (index * 50, 50)
        
        self.letters.remove(letter)
        self.scene.remove_sprite_list_by_name(f'Letter{letter.letter}')

    def draw(self, camera : Camera):
        cam_x, cam_y = camera.position
        screen_bot = cam_y - camera.viewport_height / 2
        screen_left = cam_x - camera.viewport_width / 2
        for letter in self.collection:
            
            letter.draw()


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Our TileMap Object
        self.tile_map = None

        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # A Camera that can be used for scrolling the screen
        self.camera = None

        self.left_pressed = False
        self.right_pressed = False

        

    # def setup(self):
    #     # Sprite List
    #     self.player_list = arcade.SpriteList()
    #     self.ground_list = arcade.SpriteList()

    #     # Set up player
    #     self.player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING * 2)
    #     self.player_sprite.center_x = 32
    #     self.player_sprite.center_y = 130
    #     self.player_list.append(self.player_sprite)

    #     # Set up physics engine
    #     self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.ground_list, gravity_constant=GRAVITY)
 
    #     # Set up camera
    #     self.camera = arcade.Camera(self.width, self.height)

    #     arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Setup the Cameras
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)

        # Name of map file to load
        map_name = "Map1Hard.json"

        # Layer specific options are defined based on Layer names in a dictionary
        # Doing this will make the SpriteList for the platforms layer
        # use spatial hashing for detection.
        layer_options = {
            "Platforms": {
                "use_spatial_hash": True,
            },
        }

        # Read in the tiled map
        self.tile_map = arcade.load_tilemap(
            map_name, TILE_SCALING, layer_options)

        # Initialize Scene with our TileMap, this will automatically add all layers
        # from the map as SpriteLists in the scene in the proper order.
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Set up the player, specifically placing it at these coordinates.
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 150
        self.player_sprite.center_y = 150
        self.scene.add_sprite("Player", self.player_sprite)

        # --- Other stuff
        # Set the background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene["Platforms"]
        )

        self.letters = Letters(self.scene)
        self.letters.create_letter('A', 100, 100)
        self.letters.create_letter('B', 200, 100)
        self.letters.create_letter('C', 100, 200)




    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        arcade.start_render()

        # Activate the game camera
        self.camera.use()
        # Draw our Scene
        self.scene.draw()

        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()

        self.letters.draw(self.camera)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True
        elif key == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - \
            (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def on_update(self, delta_time):
        """Movement and game logic"""

        if self.left_pressed:
            self.player_sprite.center_x -= PLAYER_MOVEMENT_SPEED
        if self.right_pressed:
            self.player_sprite.center_x += PLAYER_MOVEMENT_SPEED
        # Move the player with the physics engine
        self.physics_engine.update()

        # Position the camera
        self.center_camera_to_player()

        for letter in check_for_collision_with_list(self.player_sprite, self.letters.letters):
            self.letters.collect_letter(letter)         


def main():
    
    # """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()
    
    # Send users to main menu.
    # Commented out to avoid errors before seperating classes more professionally.
    # window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    # window.show_view(MenuView.MenuView())
    # arcade.run()


if __name__ == "__main__":
    main()
