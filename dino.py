import arcade

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 250
SCREEN_TITLE = "Dino Game"

class MyDino():

    def __init__(self):
        self.dino_list = arcade.SpriteList()
        self.dino_sprite = arcade.Sprite("./dino.png", scale=0.2, center_x=SCREEN_WIDTH/8, center_y=SCREEN_HEIGHT/5)
        self.dino_list.append(self.dino_sprite)
        print("dino init")

    def get_sprite(self):
        return self.dino_sprite

    def jump(self):
        #implement gravity and make the dino jump 
        pass