import arcade
from dino import MyDino
from ground import Ground


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 250
SCREEN_TITLE = "Dino Game"


class MyGame(arcade.Window):
    
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Instantiate Objects
        self.dino = MyDino()
        self.ground = Ground()

        # Set up window
        self.setup_window()

    def setup_window(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_update(self, delta_time):
        # update ground
        self.ground.update()
        # update score
        

        # update endGame
        pass

    def on_key_press(self, key, modifiers):
        # dino jump
        pass
        
            
    def endGame(self):
        # if collisions
        
        #stops the movement
        #pauses the game
        #pauses the score 
        #displays end game text and restart game option
        pass

    def on_draw(self):
        self.ground.get_list().draw()   # must draw ground before dino
        self.dino.get_sprite().draw()
        

def main():
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
