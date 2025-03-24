from piece import Piece


class Pyramid(Piece):
    ROTATION = ["up", "right", "down", "left"]
    REFLECTION_RULES = {
        "up": {"left": "right", "right": "left"},
        "down": {"left": "right", "right": "left"},
        "left": {"up": "down", "down": "up"},
        "right": {"up": "down", "down": "up"},
    }

    def __init__(self, team, rotation):
        super().__init__(team, rotation)
        self.set_weakside(rotation)

#SET
    def set_weakside(self, rotation):
        weakside_mapping = [
            ["up", "right"],
            ["right", "down"],
            ["down", "left"],
            ["left", "up"]
        ]
        self._weakside = weakside_mapping[rotation % 4]

    def set_rotation(self, direction):
        if direction == "left":
            self.__rotation = (self.__rotation - 1) % 4
        elif direction == "right":
            self.__rotation = (self.__rotation + 1) % 4
        self.set_weakside(self.__rotation)


    def interact_with_laser(self, direction):
        #may be needed to change the direction of the laser (if direction is left then entry side is right)
        entry_side = direction
    
        # is weak side
        if entry_side in self._weakside:
            return None

        # Determine the reflection side
        new_direction = self.REFLECTION_RULES.get(entry_side, {}).get(self.ROTATION[self.get_rotation()], None)

        return new_direction
