import arcade

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 250
SCREEN_TITLE = "Dino Game"

class Ground:

    def __init__(self):
        self.cactus_list = arcade.SpriteList()
        self.ground_list = arcade.SpriteList()

        self.ground = arcade.Sprite(filename="./dion gif.jpg", scale=1.7, center_x=SCREEN_WIDTH/2, center_y=125)
        self.ground_list.append(self.ground)

    def get_list(self):
        return self.ground_list

    def get_cacti(self):
        return self.cactus_list

    def update():
        # remove cacti off the screen 
        # generate new cacti if there is space
        # move all cacti in the cactus list 
        pass
    
    def generate_cactus():
        #generates a cactus sprite
        #draws
        #returns the sprite
        pass