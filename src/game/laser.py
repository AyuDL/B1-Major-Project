class Laser: 
    DIRECTION_VECTOR = {
        "up": (0, 1),
        "right": (-1, 0),
        "down": (0, -1),
        "left": (1, 0)
    }

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        
    def __string__(self):
        return self.direction
    
    def next_position(self):
        dx, dy = Laser.DIRECTION_VECTOR[self.direction]
        self.x += dx
        self.y += dy
        return self.x, self.y

    def reflect(self, new_direction):
        self.direction = new_direction
