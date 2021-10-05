import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pydle Apocalypse"

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        self.hero_list = None
        self.creature_list = None

    def setup(self):
        self.scene = arcade.Scene()
        self.creature_list = arcade.SpriteList()

        self.creature_sprite = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_idle.png")
        self.creature_sprite.center_x = 700
        self.creature_sprite.center_y = 200
        self.creature_list.append(self.creature_sprite)

    def on_draw(self):
        arcade.start_render()
        self.creature_list.draw()

    def on_update(self, delta_time):
        self.creature_list.update()
        for creature in self.creature_list:
            creature.change_x -= .1



def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
