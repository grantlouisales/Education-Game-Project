import arcade

class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400,200)

        arcade.set_background_color(arcade.color.AERO_BLUE)

        self.player_x = width / 2
        self.player_y = height / 2
        self.player_speed = 250

        self.sprite1 = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png")


    def on_draw(self):
        arcade.start_render()
        self.sprite1.draw()
        

    def on_update(self, delta_time):
        if self.player_y > 720:
            self.player_y = 10
        if self.player_y < 0:
            self.player_y = 720
        if self.player_x > 1280:
            self.player_x = 10
        if self.player_x < 0:
            self.player_x = 1270

        self.sprite1.set_position(self.player_x, self.player_y)


    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.D:
            self.player_x += 50
        if symbol == arcade.key.A:
            self.player_x -= 50
        if symbol == arcade.key.W:
            self.player_y += 50
        if symbol == arcade.key.S:
            self.player_y -= 50


        
        

MyGameWindow(1280, 720, "My Game Window")
arcade.run()