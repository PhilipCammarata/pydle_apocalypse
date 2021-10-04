import json
from functools import cached_property

class Creature:
    def __init__(self, id):
        self.id = id
        self.name = self.load_json['name']
        self.spawn_time = self.load_json['spawn_time']
        self.health = self.load_json['health']

    @cached_property
    def load_json(self):
        with open(f"data/creatures/{self.id}.json") as json_file:
            return json.load(json_file)

