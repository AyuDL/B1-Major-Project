from piece import Piece

class Obelisk(Piece):
    team_mounted_status = {0: False, 1: False}

    def __init__(self, team, rotation, is_mounted=True):
        super().__init__(team, rotation)
        self.__is_mounted = is_mounted

#GET
    def get_is_mounted(self):
        return self.__is_mounted
#SET
    def set_is_mounted(self, status):
        self.__is_mounted = status
#STATIC
    @classmethod
    def has_team_mounted(cls, team):
        return cls.team_mounted_status.get(team, False)

    @classmethod
    def set_team_mounted(cls, team, status):
        cls.team_mounted_status[team] = status
#METHOD
    #not checking for team here since it is already checked by the is_legal_move function
    def can_mount_on_obelisk(self): 
        if not self.__is_mounted and not self.has_team_mounted(self.__team):
            self.set_is_mounted(True)
            Obelisk.set_team_mounted(self.__team, True)
        else:
            print("Mounting not allowed.")

    def interact_with_laser(self, _direction):
        if self.__is_mounted:
            self.set_is_mounted(False)
            print("Obélisque démonté.")
        else:

            print("Obélisque détruit.")
            return None