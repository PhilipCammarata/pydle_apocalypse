import arcade
from creature import Creature
from hero import Hero

DEBUG = True

CREATURE_SPEED = 1

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
        self.hero_list = arcade.SpriteList()
        self.creature_list = arcade.SpriteList()

        self.hero_list.append(Hero("healer", 50, 200))
        self.hero_list.append(Hero("dps", 125, 200))
        self.hero_list.append(Hero("tank", 200, 200))

        self.creature_sprite = Creature("gremlin")
        self.creature_list.append(self.creature_sprite)

        arcade.schedule(self.add_creature, 2)

    def on_draw(self):
        arcade.start_render()
        self.hero_list.draw()
        self.creature_list.draw()
        if DEBUG:
            self.hero_list.draw_hit_boxes()
            self.creature_list.draw_hit_boxes()

    def on_update(self, delta_time):
        self.creature_list.update()
        for creature in self.creature_list:
            creature.change_x = -CREATURE_SPEED
            if arcade.check_for_collision_with_lists(
                creature, [self.hero_list, self.creature_list]
            ):
                creature.change_x = 0

    def add_creature(self, delta_time):
        if len(self.creature_list) >= 7:
            return
        creature_sprite = Creature("gremlin")
        self.creature_list.append(creature_sprite)


def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
