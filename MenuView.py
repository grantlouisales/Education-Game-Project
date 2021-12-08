import arcade
import window
# import InstructionView
import arcade.gui
from constants import *

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Create a horizontal BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout(vertical=False)

        # Create a second row for buttons
        self.v_box2 = arcade.gui.UIBoxLayout(vertical=True)
        
        self.diff_level = None

        # Create the buttons
        easy_button = arcade.gui.UIFlatButton(text="Easy", width=200)
        self.v_box.add(easy_button.with_space_around(right=20, left=20, bottom=20))

        medium_button = arcade.gui.UIFlatButton(text="Medium", width=200)
        self.v_box.add(medium_button.with_space_around(right=20, left=20, bottom=20))

        hard_button = arcade.gui.UIFlatButton(text="Hard", width=200)
        self.v_box.add(hard_button.with_space_around(right=20, left=20, bottom=20))

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box2.add(quit_button.with_space_around(right=20, left=20, top=200))

        # Assign callbacks
        easy_button.on_click = self.on_click_easy
        medium_button.on_click = self.on_click_medium
        hard_button.on_click = self.on_click_hard
        quit_button.on_click = self.on_click_quit

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box2)
        )

    def on_click_easy(self, _event: arcade.gui.UIOnClickEvent):
        self.diff_level = "Map1Easy.json"
        game_view = window.MyGame(self.diff_level)
        game_view.setup()
        self.window.show_view(game_view)

    def on_click_medium(self, _event: arcade.gui.UIOnClickEvent):
        self.diff_level = "Map1Medium.json"
        game_view = window.MyGame(self.diff_level)
        game_view.setup()
        self.window.show_view(game_view)

    def on_click_hard(self, _event: arcade.gui.UIOnClickEvent):
        self.diff_level = "Map1Hard.json"
        game_view = window.MyGame(self.diff_level)
        game_view.setup()
        self.window.show_view(game_view)

    def on_click_quit(self, _event: arcade.gui.UIOnClickEvent):
        arcade.close_window()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Educational Education Game", SCREEN_WIDTH / 2, SCREEN_HEIGHT -150,
                         arcade.color.DEEP_SAFFRON, font_size=80, anchor_x="center", font_name="Kenney Pixel")
        arcade.draw_text("of Learning", SCREEN_WIDTH / 2, SCREEN_HEIGHT -220,
                         arcade.color.DEEP_SAFFRON, font_size=80, anchor_x="center", font_name="Kenney Pixel")
        self.manager.draw()
