class Bot:
    """
    Represents a survivor bot in the simulation.
    """

    def __init__(self, bot_id, x, y, energy=50, max_energy=100):
        """
        Initializes the bot with its ID, initial position (x, y), energy level, and max energy capacity.
        """
        self.bot_id = bot_id
        self.x = x
        self.y = y
        self.energy = energy
        self.max_energy = max_energy
        self.carrying_part = None  # The part the bot is currently carrying

    def move(self, new_x, new_y):
        """
        Moves the bot to a new position, reducing energy in the process.
        :param new_x: New x-coordinate
        :param new_y: New y-coordinate
        """
        # If bot moves, its energy decreases (e.g., 5% per move)
        self.x = new_x
        self.y = new_y
        self.energy -= 5  # Energy cost for movement
        print(f"Bot {self.bot_id} moved to ({self.x}, {self.y}). Energy: {self.energy:.2f}%.")

    def collect_part(self, part):
        """
        Collects a spare part and stores it in the bot's inventory.
        :param part: The part to be collected by the bot
        """
        self.carrying_part = part
        print(f"Bot {self.bot_id} collected part {part.part_id} (Enhancement: {part.enhancement:.2f}%).")

    def deliver_part(self, station):
        """
        Delivers the spare part to a recharge station.
        :param station: The recharge station where the part will be delivered
        """
        if self.carrying_part:
            # Deliver the part to the recharge station
            station.store_part(self.carrying_part)
            self.carrying_part = None  # Bot no longer carries the part
            print(f"Bot {self.bot_id} delivered the part to station {station.station_id}.")

    def recharge(self):
        """
        Recharges the bot's energy at a recharge station.
        """
        if self.energy < self.max_energy:
            self.energy += 1  # Energy increases by 1% per recharge step
            print(f"Bot {self.bot_id} recharged. Current energy: {self.energy:.2f}%.")