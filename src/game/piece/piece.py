from abc import ABC, abstractmethod

class Piece(ABC):
    DIRECTIONS = ["up", "right", "down", "left"]

    def __init__(self, team, rotation=0,weakside=None, image=None):
        self.__team = team
        self.__rotation = rotation % 4 if team else (rotation + 2) % 4
        self._weakside = weakside
        self.image = image
    def __str__(self):
        return f"Piece(team={self.__team}, rotation={self.get_rotation()})"

# GET
    def get_rotation(self):
        return self.DIRECTIONS[self.__rotation]

    def get_team(self):
        return self.__team

    def get_piece(self):
        return self

    def get_weakside(self):
        return self._weakside

# SET
    def set_weakside(self, direction):
        if self._weakside is not None:
            for i in range(len(self._weakside)):
                current_index = self.DIRECTIONS.index(self._weakside[i])
                if direction == "left":
                    self._weakside[i] = self.DIRECTIONS[(current_index - 1) % 4]
                elif direction == "right":
                    self._weakside[i] = self.DIRECTIONS[(current_index + 1) % 4]

    def set_rotation(self, direction):
        if direction == "left":
            self.__rotation = (self.__rotation - 1) % 4
        elif direction == "right":
            self.__rotation = (self.__rotation + 1) % 4

# ROTATE
    def rotate_piece(self, direction):
        self.set_rotation(direction)
        self.set_weakside(direction)

# LASER
# TODO : need to be fix, some time take direction other take laser
    @abstractmethod
    def interact_with_laser(self, laser):
        pass