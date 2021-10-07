import arcade
import json
import random
from functools import cached_property


class Creature(arcade.Sprite):
    def __init__(self, id, x_position, y_position):
        super().__init__()
        self.id = id
        self.name = self.creature_data["name"]
        self.spawn_time = self.creature_data["spawn_time"]
        self.health = self.creature_data["health"]
        self.texture = self.load_texture()
        self.scale = 0.5
        self.center_x = x_position
        self.center_y = y_position

    @cached_property
    def creature_data(self):
        with open(f"data/creatures/{self.id}.json") as json_file:
            return json.load(json_file)

    def load_texture(self):
        suite = random.choice(["Clubs", "Diamonds", "Hearts", "Spades"])
        value = random.choice(["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"])
        return arcade.load_texture(f":resources:images/cards/card{suite}{value}.png")
