import arcade


class Hero(arcade.Sprite):
    def __init__(self, id, x_position, y_position):
        super().__init__()
        self.id = id
        self.texture = arcade.load_texture(self.load_texture(id))
        self.center_x = x_position
        self.center_y = y_position

    def load_texture(self, id):
        if id == "tank":
            return ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
        if id == "dps":
            return ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        if id == "healer":
            return ":resources:images/animated_characters/robot/robot_idle.png"

    def attack_creature(self, creature):
        pass
