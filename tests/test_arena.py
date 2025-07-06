# tests/test_arena.py
import unittest
from ..creature import Creature
from ..arena import Arena

class SimpleCreature(Creature):
    def attack(self, target):
        return target.take_damage(self._attack_power)

class TestArena(unittest.TestCase):
    def test_quick_battle(self):
        """Тест быстрого завершения боя"""
        strong = SimpleCreature("Strong", 100, 50, 0)
        weak = SimpleCreature("Weak", 10, 5, 0)
        arena = Arena(strong, weak)
        
        winner = arena.battle()
        self.assertEqual(winner.name, "Strong")