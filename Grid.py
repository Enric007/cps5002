class Grid:
    def __init__(self, width, height):
        # Initialize a 2D list (grid) with None values
        self.grid = [[None for _ in range(height)] for _ in range(width)]

    def __setitem__(self, position, value):
        # Allow assignment like grid[x, y] = value
        x, y = position
        self.grid[x][y] = value

    def __getitem__(self, position):
        # Allow retrieval like grid[x, y]
        x, y = position
        return self.grid[x][y]

    def __repr__(self):
        return f"Grid(width={len(self.grid)}, height={len(self.grid[0])})"