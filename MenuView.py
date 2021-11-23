import arcade
import window
# import InstructionView
import arcade.gui
from constants import *

class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()
        
        self.diff_level = None

        # Create the buttons
        easy_button = arcade.gui.UIFlatButton(text="Easy", width=200)
        self.v_box.add(easy_button.with_space_around(bottom=20))

        medium_button = arcade.gui.UIFlatButton(text="Medium", width=200)
        self.v_box.add(medium_button.with_space_around(bottom=20))

        hard_button = arcade.gui.UIFlatButton(text="Hard", width=200)
        self.v_box.add(hard_button.with_space_around(bottom=20))

        # Use a child class to handle quit event.
        # kept here for reference
        quit_button = QuitButton(text="Quit", width=200)
        self.v_box.add(quit_button)

        # Assign callbacks
        easy_button.on_click = self.on_click_easy
        medium_button.on_click = self.on_click_medium
        hard_button.on_click = self.on_click_hard

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_easy(self, _event: arcade.gui.UIOnClickEvent):
        game_view = window.MyGame()
        self.window.show_view(game_view)

    def on_click_medium(self, _event: arcade.gui.UIOnClickEvent):
        game_view = window.MyGame()
        self.window.show_view(game_view)

    def on_click_hard(self, _event: arcade.gui.UIOnClickEvent):
        self.diff_level = "Map1Hard.json"
        game_view = window.MyGame()
        self.window.show_view(game_view)
        
    def get_level(self):
        return self.diff_level

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Educational Education Game of Learning", SCREEN_WIDTH / 2, SCREEN_HEIGHT -150,
                         arcade.color.BLACK, font_size=40, anchor_x="center")
        self.manager.draw()
