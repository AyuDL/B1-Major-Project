from piece import Piece

class Pharaon(Piece):

    def __init__(self, team, rotation):
        super().__init__(team, rotation,["up", "right", "down", "left"])

    def interact_with_laser(self, _direction):
        print("👑 Le pharaon est mort ! Partie terminée.")
        # end of the game
        return None
    
    


