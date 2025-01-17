class SparePart:
    def __init__(self, part_id, x, y, size, enhancement, grid):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            raise ValueError(f"Invalid coordinates ({x}, {y}) for the grid.")
        self.part_id = part_id
        self.x = x
        self.y = y
        self.size = size
        self.enhancement = enhancement
        self.grid = grid