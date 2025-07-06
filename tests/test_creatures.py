import unittest
from unittest.mock import MagicMock
from creature import Creature, Warrior, Mage, Archer

class TestCreatureConcrete(Creature):
    def attack(self, target):
        return target.take_damage(self._attack_power)

class TestCreature(unittest.TestCase):
    def setUp(self):
        self.creature = TestCreatureConcrete("Test", 100, 10, 5)
    
    def test_initial_state(self):
        self.assertEqual(self.creature.name, "Test")
        self.assertEqual(self.creature.health, 100)
        self.assertTrue(self.creature.is_alive)
    
    def test_take_damage(self):
        damage_taken = self.creature.take_damage(10)
        self.assertEqual(damage_taken, 5)  # 10 damage - 5 defense
        self.assertEqual(self.creature.health, 95)
        
        self.creature.take_damage(200)
        self.assertEqual(self.creature.health, 0)
        self.assertFalse(self.creature.is_alive)
    
    def test_heal(self):
      self.creature.take_damage(30)  # 100 - 30 = 70
      self.creature.heal(20)         # 70 + 20 = 90
      self.assertEqual(self.creature.health, 95)

class TestWarrior(unittest.TestCase):
    def setUp(self):
        self.warrior = Warrior("Conan")
        # Используем тестовый класс как цель
        self.target = TestCreatureConcrete("Dummy", 200, 0, 0)
    
    def test_attack_rage_mechanic(self):
        #ульта
        self.warrior.attack(self.target)
        self.assertEqual(self.warrior._rage, 10)
        
        #критикал шот
        with unittest.mock.patch('random.randint', return_value=1):  
            self.warrior._rage = 100
            self.warrior.attack(self.target)
            self.assertEqual(self.warrior._rage, 0)

class TestMage(unittest.TestCase):
    def setUp(self):
        self.mage = Mage("Gandalf")
        self.target = TestCreatureConcrete("Target", 200, 0, 10)
    
    def test_initial_stats(self):
        self.assertEqual(self.mage.health, 80)
        self.assertEqual(self.mage._mana, 100)
    
    def test_mana_regen(self):
        self.mage._mana = 0
        self.mage.attack(self.target)
        self.assertEqual(self.mage._mana, 10)
    
    def test_spell_attack(self):
        with unittest.mock.patch('random.random', return_value=0.1): 
            self.mage.attack(self.target)
            self.assertEqual(self.mage._mana, 80)

class TestArcher(unittest.TestCase):
    def setUp(self):
        self.archer = Archer("Legolas")
        self.target = TestCreatureConcrete("Target", 200, 0, 0)
    
    def test_critical_hit(self):
        with unittest.mock.patch('random.random', return_value=0.1):  # Всегда крит
            damage = self.archer.attack(self.target)
            self.assertEqual(damage, 60)  # 20 * 3