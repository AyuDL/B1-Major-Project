from laser import Laser
from piece.piece import Piece
from piece.pyramid import Pyramid
from piece.obelisk import Obelisk
from piece.djed import Djed


class Board:
    def __init__(self):
        self.grid = self.__init_grid()

    def __init_grid(self):
        return [[None for _ in range(8)] for _ in range(10)]

    def place_piece(self, piece, x, y):
        self.grid[x][y] = piece

    def get_piece(self, x: int, y: int) -> Piece | None:
        return self.grid[x][y]

    def remove_piece(self, x, y):
        self.grid[x][y] = None


    def fire_laser(self, x, y, direction):
        laser = Laser(x, y, direction)

        while True:
            x, y = laser.next_position()

            if not (0 <= x < 8 and 0 <= y < 10):
                break

            piece = self.get_piece(x, y)

            if not piece:
                continue

            laser = piece.interact_with_laser(laser)

            if laser is None:
                break     
    
    # maybe not needed in board but in utils function
    def is_legal_move(self,  x, y, new_x, new_y):

        if abs(new_x - x) > 1 or abs(new_y - y) > 1:
            return False

        target_piece = self.get_piece(new_x, new_y)

        if target_piece is None:
            return True
        
        if isinstance(target_piece, Djed):
            if isinstance(target_piece, (Pyramid, Obelisk)) and target_piece.get_team() != self.get_piece(x, y).get_team():
                return True

        elif isinstance(target_piece, Obelisk):
            if isinstance(target_piece, Obelisk) and target_piece.get_team() == self.get_piece(x, y).get_team() and not target_piece.get_is_mounted():
                return True
        
        return False
