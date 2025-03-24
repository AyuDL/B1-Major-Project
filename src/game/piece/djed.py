from piece import Piece

# Mirror
class Djed(Piece):
    DIRECTION_CW = ["up", "right", "down", "left"]

    def interact_with_laser(self, laser):
        index = self.DIRECTION_CW.index(laser.direction)
        if self.__rotation % 2 == 0:
            new_direction = self.DIRECTION_CW[(index + 1) % 4]
        else:
            new_direction = self.DIRECTION_CW[(index - 1) % 4]
        return new_direction