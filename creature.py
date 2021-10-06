import arcade
import json
from functools import cached_property


class Creature(arcade.Sprite):
    def __init__(self, id, x_position=700, y_position=200):
        super().__init__()
        self.id = id
        self.name = self.creature_data["name"]
        self.spawn_time = self.creature_data["spawn_time"]
        self.health = self.creature_data["health"]
        self.texture = arcade.load_texture(
            ":resources:images/animated_characters/zombie/zombie_idle.png"
        )
        self.center_x = x_position
        self.center_y = y_position

    @cached_property
    def creature_data(self):
        with open(f"data/creatures/{self.id}.json") as json_file:
            return json.load(json_file)
