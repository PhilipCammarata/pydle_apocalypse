import json
from functools import cached_property

class Creature:
    def __init__(self, id):
        self.id = id
        self.name = self.creature_data['name']
        self.spawn_time = self.creature_data['spawn_time']
        self.health = self.creature_data['health']

    @cached_property
    def creature_data(self):
        with open(f"data/creatures/{self.id}.json") as json_file:
            return json.load(json_file)

