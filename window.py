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
from MenuView import *
from read_words_file import *
from spelling import *


class MyGame(arcade.View):
    """
    Main application class.
    """

    def __init__(self, difficulty):
        """ Initialize """

        # Call the parent class and set up the window
        super().__init__()

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
        
        # Get difficulty level from MainMenu
        self.diff_level = difficulty

        # Set up background music
        self.audio_name = arcade.sound.load_sound("audio/2021-09-08_-_Castle_Of_Fear_-_www.FesliyanStudios.com.mp3")
        arcade.sound.play_sound(self.audio_name,.2)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Setup the Cameras
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.gui_camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Name of map file to load
        map_name = self.diff_level

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

        self.spelling = Spelling(self.scene, self.player_sprite, map_name)


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

        if self.spelling.draw_word:
            arcade.draw_text(f'CURRENT WORD: {self.spelling.curr_word.upper()}', SCREEN_WIDTH/2, SCREEN_HEIGHT - 20, arcade.color.AMARANTH, 16, 100,"center","calibri", True)
            self.spelling.word_timer += 1
            if self.spelling.word_timer >= WORD_MAX_TIME:
                self.spelling.draw_word = False
        

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True
        elif (key == arcade.key.SPACE or key == arcade.key.UP or key == arcade.key.W) and self.physics_engine.can_jump():
            self.player_sprite.change_y = PLAYER_JUMP_SPEED
        # Yes, this is for cheating, I mean testing
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = PLAYER_JUMP_SPEED 
        elif key == arcade.key.C:
            self.spelling.clear_letters()
            self.spelling.start_word()
        

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

    def center_camera_to_player(self):
        """Ensures the camera is centered on the player."""

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

        for letter in check_for_collision_with_list(self.player_sprite, self.spelling.map_letters):
            self.spelling.collect_letter(letter)
              
