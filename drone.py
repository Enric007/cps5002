class Drone:
    def __init__(self, drone_id, x, y, grid, is_malfunctioning=False):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            raise ValueError(f"Invalid coordinates ({x}, {y}) for the grid.")
        self.drone_id = drone_id
        self.x = x
        self.y = y
        self.grid = grid
        self.is_malfunctioning = is_malfunctioning

    def repair(self):
        if self.is_malfunctioning:
            self.is_malfunctioning = False
            print(f"Drone {self.drone_id} has been repaired.")
        else:
            print(f"Drone {self.drone_id} is not malfunctioning and does not need repairs.")