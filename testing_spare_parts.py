from Grid import Grid
from spare_part import SparePart

# Create a 10x10 grid
grid = Grid(10, 10)

# Add spare parts of different sizes
part1 = SparePart(part_id=1, x=2, y=2, size="small", grid=grid)
part2 = SparePart(part_id=2, x=4, y=4, size="medium", grid=grid)
part3 = SparePart(part_id=3, x=6, y=6, size="large", grid=grid)

# Add spare parts to the grid
grid.add_entity(2, 2, part1)
grid.add_entity(4, 4, part2)
grid.add_entity(6, 6, part3)

print("\nInitial Grid:")
grid.display_grid()

# Simulate decay over 5 steps
print("\nSimulating Decay:")
for _ in range(5):
    part1.decay()
    part2.decay()
    part3.decay()

# Print grid state after decay
print("\nGrid After Decay:")
grid.display_grid()

# Simulate recharging of parts
print("\nSimulating Recharge:")
for _ in range(10):
    part1.recharge()
    part2.recharge()
    part3.recharge()

# Print final state
print("\nFinal Grid State After Recharge:")
grid.display_grid()