class SurvivorBot:
    def __init__(self, bot_id, x, y, grid, energy=100, base_x=0, base_y=0, energy_threshold=20):
        self.bot_id = bot_id
        self.x = x
        self.y = y
        self.grid = grid
        self.energy = energy
        self.base_x = base_x
        self.base_y = base_y
        self.energy_threshold = energy_threshold  # Set a threshold for when the bot needs to recharge
        self.recharging = False  # Track if bot is recharging or not

    def move(self, target_x, target_y):
        # If bot is recharging, it should not move
        if self.recharging:
            print(f"Bot {self.bot_id} is recharging and cannot move.")
            return False

        # Check if the target position is within the grid bounds
        if not (0 <= target_x < len(self.grid) and 0 <= target_y < len(self.grid[0])):
            print(f"Invalid move: ({target_x}, {target_y}) is out of bounds.")
            return False

        # Check if bot has enough energy to move
        energy_required = abs(self.x - target_x) + abs(self.y - target_y)
        if self.energy < energy_required:
            print(f"Not enough energy to move to ({target_x}, {target_y}). Energy is {self.energy}%.")
            # If energy is low, return to base for recharge
            self.move_to_base()
            return False

        # Move the bot to the target position
        self.x, self.y = target_x, target_y
        self.energy -= energy_required
        print(f"Bot {self.bot_id} moved to ({self.x}, {self.y}). Energy decreased to {self.energy}%.")

        # If energy is below threshold, return to base to recharge
        if self.energy < self.energy_threshold:
            print(f"Bot {self.bot_id}'s energy is below threshold. Returning to base for recharge.")
            self.move_to_base()

        return True

    def move_to_base(self):
        # Check if bot is already at the base, if it is, don't move again
        if self.x == self.base_x and self.y == self.base_y:
            print(f"Bot {self.bot_id} is already at the base.")
            if self.energy == 0:
                self.recharge()  # Recharging when energy is 0
            return  # No need to move if already at the base

        # Move back to base (0, 0) if not already there
        print(f"Bot {self.bot_id} returning to base for recharge.")
        self.move(self.base_x, self.base_y)

    def recharge(self):
        # Recharging the bot by resetting energy to 100%
        self.energy = 100
        self.recharging = True
        print(f"Bot {self.bot_id} is recharging. Energy reset to {self.energy}%.")

        # After recharging, reset the recharging flag and allow movement again
        self.recharging = False