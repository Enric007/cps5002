# grid_entity.py
class GridEntity:
    def __init__(self, x, y, grid):
        """
        Initialize a generic grid entity.

        Args:
            x (int): X-coordinate of the entity.
            y (int): Y-coordinate of the entity.
            grid (Grid): Reference to the grid object.
        """
        self.x = x
        self.y = y
        self.grid = grid

    def move(self, new_x, new_y):
        """
        Move the entity to a new position on the grid.

        Args:
            new_x (int): New X-coordinate.
            new_y (int): New Y-coordinate.
        """
        self.grid.update_entity_position(self, new_x, new_y)
        self.x = new_x
        self.y = new_y

    def __str__(self):
        return f"Entity at ({self.x}, {self.y})"