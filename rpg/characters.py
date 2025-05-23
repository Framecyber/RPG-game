class Character:
    def __init__(self, name, health, max_health, attack_power, defense_power):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack_power = attack_power
        self.defense_power = defense_power
        self.is_defending = False

    def is_alive(self):
        return self.health > 0

    def start_defense(self):
        self.is_defending = True
        print(f"{self.name} is defending!")

    def end_defense(self):
        self.is_defending = False
        # Optional: print(f"{self.name} is no longer defending.")

class Player(Character):
    def __init__(self, name, health, max_health, attack_power, defense_power):
        super().__init__(name, health, max_health, attack_power, defense_power)
        # Add player-specific attributes here if needed

class NPC(Character):
    def __init__(self, name, health, max_health, attack_power, defense_power):
        super().__init__(name, health, max_health, attack_power, defense_power)
        # Add NPC-specific attributes here if needed
