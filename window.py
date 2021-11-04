import arcade

class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400,200)

        arcade.set_background_color(arcade.color.AERO_BLUE)

        self.x = 100
        self.y = 100
        self.x_speed = 300
        self.y_speed = 150

        self.player_x = 100
        self.player_y = 100

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.x, self.y, 60, arcade.color.RED_DEVIL, 10)
        arcade.draw_circle_outline(self.player_x, self.player_y, 100, arcade.color.RED_DEVIL, 10)


    def on_update(self, delta_time):
        # Delta time is 1/60 = 0.01666 * 300 = 5 pixels
        self.x += self.x_speed * delta_time
        self.y += self.y_speed * delta_time

        if self.x > 1280 or self.x < 0:
            self.x_speed *= -1

        if self.y > 720 or self.y < 0:
            self.y_speed *= -1

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.player_x += 100
        if symbol == arcade.key.LEFT:
            self.player_x -= 100
        if symbol == arcade.key.UP:
            self.player_y += 100
        if symbol == arcade.key.DOWN:
            self.player_y -= 100
        
        

MyGameWindow(1280, 720, "My Game Window")
arcade.run()
