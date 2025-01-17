import random
from Bot import Bot
class MalfunctioningDrone(Bot):
    """
    Represents a malfunctioning drone in the simulation.
    Inherits from Bot and adds malfunctioning behavior.
    """
    def __init__(self, bot_id, x, y, energy=50, max_energy=100):
        super().__init__(bot_id, x, y, energy, max_energy)
        self.is_malfunctioning = False  # Drone can malfunction randomly

    def move(self, new_x, new_y):
        """
        Override move function to add malfunctioning behavior.
        If the drone is malfunctioning, it can't move temporarily.
        """
        if self.is_malfunctioning:
            print(f"Bot {self.bot_id} is malfunctioning and cannot move!")
            return
        super().move(new_x, new_y)

    def trigger_malfunction(self):
        """
        Randomly triggers a malfunction, affecting the drone's movement and energy.
        """
        # Simulate a malfunction with a random chance
        if random.random() < 0.3:  # 30% chance to malfunction
            self.is_malfunctioning = True
            print(f"Bot {self.bot_id} has malfunctioned and cannot move temporarily!")
        else:
            print(f"Bot {self.bot_id} is functioning normally.")

    def repair(self):
        """
        Repairs the drone, restoring its functionality.
        """
        self.is_malfunctioning = False
        print(f"Bot {self.bot_id} has been repaired and is now functional.")

    def recharge(self):
        """
        Override recharge function to allow recharge even during malfunction.
        """
        super().recharge()