import random
from creature import Warrior, Mage, Archer
from arena import Arena

class Game:
    CREATURE_TYPES = {
        '1': ('Warrior', Warrior),
        '2': ('Mage', Mage),
        '3': ('Archer', Archer)
    }
    
    OPPONENT_NAMES = [
        "Gorgon", "Dark Knight", "Shadow Assassin", 
        "Necromancer", "Troll", "Dragonkin"
    ]
    
    def __init__(self):
        self.player = None
        self.opponent = None
    
    def select_character(self):
        print("=== SELECT YOUR CHARACTER ===")
        for key, (name, _) in self.CREATURE_TYPES.items():
            print(f"{key}. {name}")
        
        while True:
            choice = input("Enter your choice (1-3): ")
            if choice in self.CREATURE_TYPES:
                name = input("Enter your character's name: ")
                cls = self.CREATURE_TYPES[choice][1]
                self.player = cls(name)
                break
            print("Invalid choice. Please try again.")
    
    def generate_opponent(self):
        cls = random.choice([Warrior, Mage, Archer])
        name = random.choice(self.OPPONENT_NAMES)
        self.opponent = cls(name)
    
    def start(self):
        print("=== BATTLE ARENA ===")
        self.select_character()
        self.generate_opponent()
        
        print(f"\nYour character: {self.player}")
        print(f"Your opponent: {self.opponent}")
        
        input("\nPress Enter to begin the battle...")
        
        arena = Arena(self.player, self.opponent)
        arena.battle()
        
        print("\nGame over. Thanks for playing!")

if __name__ == "__main__":
    game = Game()
    game.start()