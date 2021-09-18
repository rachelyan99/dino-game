import arcade

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 300
SCREEN_TITLE = "Dino Game"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.dino_list = None
        self.cactus_list = None
        self.ground_list = None

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):

        self.dino_list = arcade.SpriteList()
        self.cactus_list = arcade.SpriteList()
        self.ground_list = arcade.SpriteList()

        dino = arcade.Sprite("./dino.png", scale=0.2,
                             center_x=SCREEN_WIDTH/2, center_y=SCREEN_HEIGHT/2)
        self.dino_list.append(dino)

        ground = arcade.Sprite(filename="./ground.gif",
                               scale=1.5, center_x=SCREEN_WIDTH/2, center_y=50)
        self.ground_list.append(ground)

    def on_draw(self):
        self.ground_list.draw()
        self.dino_list.draw()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
