# arena.py
class Arena:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        self.round = 0
        self.max_rounds = 100  # Максимальное число раундов
    
    def battle_round(self):
        if self.round >= self.max_rounds:
            raise RuntimeError("Превышено максимальное число раундов")
        
        self.round += 1
        # Остальной код без изменений
        
        # Player attacks first
        if self.player.is_alive:
            self.player.attack(self.opponent)
        
        # Check if opponent is defeated
        if not self.opponent.is_alive:
            print(f"{self.opponent.name} has been defeated!")
            return False
        
        # Opponent attacks back
        if self.opponent.is_alive:
            self.opponent.attack(self.player)
        
        # Check if player is defeated
        if not self.player.is_alive:
            print(f"{self.player.name} has been defeated!")
            return False
        
        # Both survived
        print(f"Status: {self.player.name} - {self.player.health} HP, "
              f"{self.opponent.name} - {self.opponent.health} HP")
        return True
    
    def battle(self):
        print("\n=== BATTLE BEGINS ===")
        print(f"{self.player.name} vs {self.opponent.name}")
        
        while self.battle_round():
            continue
        
        winner = self.player if self.player.is_alive else self.opponent
        print(f"\n=== BATTLE ENDS ===")
        print(f"{winner.name} wins the battle!")
        return winner