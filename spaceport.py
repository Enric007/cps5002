# spaceport.py

from recharge_station import RechargeStation  # Add this import

class Spaceport:
    def __init__(self, port_id, x, y, grid):
        self.port_id = port_id
        self.x = x
        self.y = y
        self.grid = grid  # The grid should be a dictionary
        self.recharge_stations = []

    def add_recharge_station(self, station):
        if isinstance(station, RechargeStation):
            self.recharge_stations.append(station)
            self.grid[(station.x, station.y)] = station  # Store station in grid
            print(f"Recharge Station {station.station_id} added to Spaceport {self.port_id} at ({station.x}, {station.y})")
        else:
            print("Invalid recharge station!")

    def __str__(self):
        return f"Spaceport {self.port_id} at location ({self.x}, {self.y})"