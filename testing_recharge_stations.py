from Grid import Grid
from spare_part import SparePart
from recharge_station import RechargeStation

# Create a grid
grid = Grid(10, 10)

# Create a recharge station
station1 = RechargeStation(station_id=1, x=5, y=5, grid=grid)
grid.add_entity(5, 5, station1)

# Add spare parts
part1 = SparePart(part_id=1, x=2, y=2, size="small", grid=grid)
station1.store_part(part1)

# Simulate bots arriving
class Bot:
    def __init__(self, bot_id, energy=50, max_energy=100):
        self.bot_id = bot_id
        self.energy = energy
        self.max_energy = max_energy

bot1 = Bot(bot_id=101)
bot2 = Bot(bot_id=102)

station1.add_bot(bot1)
station1.add_bot(bot2)

# Simulate recharging
print("\nBefore Recharge:")
print(f"Bot1 Energy: {bot1.energy}%")
print(f"Bot2 Energy: {bot2.energy}%")

print("\nSimulating Recharge...")
for _ in range(5):
    station1.recharge_bots()

# After recharge
print("\nAfter Recharge:")
print(f"Bot1 Energy: {bot1.energy}%")
print(f"Bot2 Energy: {bot2.energy}%")