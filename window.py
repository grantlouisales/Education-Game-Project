"""
Platformer Game
"""
import arcade
from arcade.camera import Camera
from arcade.scene import Scene
from arcade.sprite import Sprite
from arcade.sprite_list.spatial_hash import check_for_collision_with_list

import random
import string
import threading
import time
from constants import *
# from MenuView import *
class Spelling():
    
    class Letter(arcade.Sprite):
        def __init__(self, letter, x, y):
            super().__init__(f'resources/letters/letter{str.upper(letter)}.png', center_x=x, center_y=y, scale=.1)
            self.letter = letter

    def __init__(self, scene : Scene, player : Sprite):
        self.collection = []
        self.letter_list = arcade.SpriteList()
        self.scene = scene
        self.curr_word = 'dragon'
        self.curr_letter = 'd'
        self.player = player

    def create_letter(self, letter : str, position):
        letter_sprite = self.Letter(letter, position[0], position[1])
        self.letter_list.append(letter_sprite)
        self.scene.add_sprite(f'Letter', letter_sprite)

    def collect_letter(self, letter : Letter):
        self.clear_letters()
        self.next_letter()

        self.generate_letters(LOCATIONS, prev_location=letter.position)

        self.collection.append(letter)
        index = self.collection.index(letter) + 1
        letter.center_x, letter.center_y = (index * 50, 50)


    def draw_gui(self):
        for letter in self.collection:
            letter.draw()

    def get_new_word(self):
        pass

    def generate_letters(self, pos_list, prev_location=None):
        while True:
            locations = random.sample(pos_list, 3)
            if not prev_location in locations:
                break
        letters = random.sample(string.ascii_lowercase, 2)
        self.create_letter(self.curr_letter, locations.pop())
        for place in locations:
            self.create_letter(letters.pop(), place)

    def clear_letters(self):
        self.scene.remove_sprite_list_by_name('Letter')
        self.letter_list = arcade.SpriteList()

    def next_letter(self):
        index = self.curr_word.index(self.curr_letter)
        # if index == len(self.curr_word - 1):
        #     test for correct word
        self.curr_letter = self.curr_word[index + 1]



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

        self.spelling = Spelling(self.scene, self.player_sprite)
        self.spelling.generate_letters(LOCATIONS)




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

        self.spelling.draw_gui()
        arcade.draw_text(f'({self.player_sprite.center_x}, {self.player_sprite.center_y})', 10, SCREEN_HEIGHT - 20)

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

        for letter in check_for_collision_with_list(self.player_sprite, self.spelling.letter_list):
            self.spelling.collect_letter(letter)         


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
