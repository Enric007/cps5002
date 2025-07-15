class SparePart:
    def __init__(self, part_id, x, y, size, enhancement, grid):
        self.part_id = part_id
        self.x = x
        self.y = y
        self.size = size.lower()  # "small", "medium", "large"
        self.enhancement = enhancement  # float, e.g., 5.0
        self.grid = grid
        self.health = 100  # Initial health at 100%

    def decay(self):
        """Simulates wear and tear over time."""
        self.health = max(0, self.health - 10)
        print(f"[DECAY] Part {self.part_id} ({self.size}) at ({self.x},{self.y}) → {self.health}% health")

    def recharge(self):
        """Simulates restoring energy or repairing the part."""
        self.health = min(100, self.health + 5)
        print(f"[RECHARGE] Part {self.part_id} ({self.size}) at ({self.x},{self.y}) → {self.health}% health")

    def __str__(self):
        """String shown when displaying on the grid."""
        return f"P{self.part_id}-{self.size[0].upper()}({self.health}%)"