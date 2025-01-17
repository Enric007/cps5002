# Grid class definition
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]

    def __str__(self):
        return f"Grid({self.width}x{self.height})"

    def is_valid_position(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height


# Recharge Station class definition
class RechargeStation:
    def __init__(self, station_id, x, y, grid):
        self.station_id = station_id
        self.x = x
        self.y = y
        self.grid = grid
        self.capacity = 10
        self.parts = []

        # Add to the grid at the station's position
        if grid.is_valid_position(x, y):
            grid.grid[y][x] = self

    def __str__(self):
        return f"Recharge Station {self.station_id} at ({self.x}, {self.y})"

    def store_part(self, part):
        if len(self.parts) < self.capacity:
            self.parts.append(part)
            print(f"Part stored in Recharge Station {self.station_id} at ({self.x}, {self.y})")
        else:
            print(f"Recharge Station {self.station_id} at ({self.x}, {self.y}) is full.")


# Bot class definition
class Bot:
    def __init__(self, bot_id, x, y, energy, grid):
        self.bot_id = bot_id
        self.x = x
        self.y = y
        self.energy = energy
        self.grid = grid

    def __str__(self):
        return f"Bot {self.bot_id} at ({self.x}, {self.y}) with energy {self.energy}%"

    def move(self, x, y):
        if self.grid.is_valid_position(x, y):
            self.x = x
            self.y = y
            self.decrease_energy(10)  # Assume each move costs 10% energy
            print(f"Bot {self.bot_id} moved to ({self.x}, {self.y}).")
            print(f"Bot {self.bot_id} energy decreased to {self.energy}%.")
        else:
            print(f"Invalid move: ({x}, {y}) is out of bounds.")

    def decrease_energy(self, amount):
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0

    def collect_part(self, part):
        print(f"Bot {self.bot_id} collected part {part.part_id} at ({self.x}, {self.y}).")

    def deliver_part(self, recharge_station):
        if self.energy < 20:
            print(f"Bot {self.bot_id}'s energy is below threshold. Returning to base for recharge.")
            self.move(0, 0)  # Move back to spaceport for recharge
        else:
            recharge_station.store_part(self)


# Spare Part class definition
class SparePart:
    def __init__(self, part_id, x, y, size, enhancement, grid):
        self.part_id = part_id
        self.x = x
        self.y = y
        self.size = size
        self.enhancement = enhancement
        self.grid = grid

    def __str__(self):
        return f"Part {self.part_id} at ({self.x}, {self.y})"


# Spaceport class definition
class Spaceport:
    def __init__(self, port_id, x, y, grid):
        self.port_id = port_id
        self.x = x
        self.y = y
        self.grid = grid
        self.recharge_stations = []

    def __str__(self):
        return f"Spaceport {self.port_id} at ({self.x}, {self.y})"

    def add_recharge_station(self, recharge_station):
        self.recharge_stations.append(recharge_station)
        print(
            f"Recharge Station {recharge_station.station_id} added to Spaceport {self.port_id} at ({self.x}, {self.y})")


# Final Integration Test function
def run_final_integration_test():
    # Step 1: Create a grid with width and height
    grid = Grid(width=10, height=10)  # Create an instance of the grid

    # Step 2: Create Spaceport
    spaceport = Spaceport(port_id=1, x=0, y=0, grid=grid)
    print(f"{spaceport} initialized.")

    # Step 3: Create a recharge station
    recharge_station = RechargeStation(station_id=1, x=5, y=5, grid=grid)
    print(f"{recharge_station} initialized.")

    # Step 4: Add recharge station to spaceport
    spaceport.add_recharge_station(recharge_station)

    # Step 5: Create parts and store in recharge station
    part1 = SparePart(part_id=1, x=2, y=2, size="small", enhancement=5.0, grid=grid)
    print(f"Part {part1} created.")
    recharge_station.store_part(part1)

    part2 = SparePart(part_id=2, x=3, y=3, size="large", enhancement=10.0, grid=grid)
    print(f"Part {part2} created.")
    recharge_station.store_part(part2)

    # Step 6: Create Bot and collect parts
    bot = Bot(bot_id=101, x=2, y=2, energy=50, grid=grid)
    print(f"{bot} initialized.")

    bot.collect_part(part1)
    bot.move(5, 5)  # Move bot to recharge station
    bot.decrease_energy(10)  # Decrease energy after each move

    bot.collect_part(part2)
    bot.move(8, 8)  # Move to another location
    bot.decrease_energy(10)

    # Step 7: Bot delivers parts to recharge station
    bot.deliver_part(recharge_station)

    # Final output
    print(f"\n{spaceport} has the following:")
    print(f"  Recharge Stations: {len(spaceport.recharge_stations)}")
    print(f"  Stored Parts in Recharge Station: {len(recharge_station.parts)}")


# Run the final integration test
run_final_integration_test()