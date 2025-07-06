import random
from abc import ABC, abstractmethod

class Creature(ABC):
    def __init__(self, name, health, attack_power, defense):
        self._name = name
        self._max_health = health
        self._health = health
        self._attack_power = attack_power
        self._defense = defense
        self._is_alive = True
    
    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
    
    @property
    def is_alive(self):
        return self._is_alive
    
    def take_damage(self, damage):
        actual_damage = max(0, damage - self._defense)
        self._health -= actual_damage
        if self._health <= 0:
            self._health = 0
            self._is_alive = False
        return actual_damage
    
    def heal(self, amount):
        self._health = min(self._max_health, self._health + amount)
    
    @abstractmethod
    def attack(self, target):
        pass
    
    def __str__(self):
        return f"{self._name} (HP: {self._health}/{self._max_health}, ATK: {self._attack_power}, DEF: {self._defense})"

class Warrior(Creature):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=15, defense=10)
        self._rage = 0
    
    def attack(self, target):
        base_damage = self._attack_power
        self._rage = min(100, self._rage + 10)
        
        if random.randint(1, 100) <= self._rage:
            damage = base_damage * 2
            self._rage = 0
            print(f"{self._name} lands a CRITICAL HIT!")
        else:
            damage = base_damage
        
        actual_damage = target.take_damage(damage)
        print(f"{self._name} attacks {target.name} for {actual_damage} damage!")
        return actual_damage

class Mage(Creature):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=25, defense=5)
        self._mana = 100
    
    def attack(self, target):
        if self._mana >= 20 and random.random() < 0.3:
            damage = int(self._attack_power * 1.5)
            self._mana -= 20
            print(f"{self._name} casts a powerful spell!")
        else:
            damage = self._attack_power
            self._mana = min(100, self._mana + 10)
        
        defense_ignored = target._defense // 2
        actual_damage = target.take_damage(damage + defense_ignored)
        print(f"{self._name} attacks {target.name} for {actual_damage} damage!")
        return actual_damage

class Archer(Creature):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=20, defense=7)
        self._critical_chance = 0.2
    
    def attack(self, target):
        base_damage = self._attack_power
        
        if random.random() < self._critical_chance:
            damage = base_damage * 3
            print(f"{self._name} hits a weak spot!")
        else:
            damage = base_damage
        
        actual_damage = target.take_damage(damage)
        print(f"{self._name} attacks {target.name} for {actual_damage} damage!")
        return actual_damage