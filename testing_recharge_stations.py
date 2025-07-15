class RechargeStation:
    def __init__(self, station_id, x, y, capacity, grid):
        self.station_id = station_id
        self.x = x
        self.y = y
        self.capacity = capacity
        self.grid = grid
        self.stored_parts = []
        self.bots = []
        self.grid.add_entity(x, y, self)

    def store_part(self, spare_part):
        self.stored_parts.append(spare_part)
        print(f"[STATION] Stored part {spare_part.part_id} at Station {self.station_id}")

    def add_bot(self, bot):
        if len(self.bots) < self.capacity:
            self.bots.append(bot)
            print(f"[STATION] Bot {bot.bot_id} added to Station {self.station_id}")
        else:
            print(f"[STATION] Station {self.station_id} is at full capacity. Cannot add Bot {bot.bot_id}")

    def recharge_bots(self):
        if not self.stored_parts:
            print("[STATION] No spare parts available to recharge bots.")
            return

        for bot in self.bots:
            if bot.energy < bot.max_energy:
                bot.energy = min(bot.max_energy, bot.energy + 10)
                print(f"[RECHARGE] Bot {bot.bot_id} recharged to {bot.energy}%")
            else:
                print(f"[RECHARGE] Bot {bot.bot_id} is already fully charged.")

    def __str__(self):
        return f"Station{self.station_id}"