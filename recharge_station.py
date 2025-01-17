class RechargeStation:
    def __init__(self, station_id, x, y, capacity, grid):
        self.station_id = station_id
        self.x = x
        self.y = y
        self.capacity = capacity  # Add capacity as an attribute
        self.grid = grid
        self.parts_stored = []

        print(f"Recharge Station {self.station_id} initialized at location ({self.x}, {self.y}).")

    def store_part(self, part):
        """Store a part in the recharge station."""
        if len(self.parts_stored) < self.capacity:
            self.parts_stored.append(part)
            print(f"Part stored in Recharge Station {self.station_id} at ({self.x}, {self.y}).")
        else:
            print(f"Recharge Station {self.station_id} at ({self.x}, {self.y}) is full.")

    def __repr__(self):
        return f"RechargeStation(station_id={self.station_id}, x={self.x}, y={self.y}, capacity={self.capacity})"