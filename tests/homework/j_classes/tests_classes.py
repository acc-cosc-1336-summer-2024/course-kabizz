import unittest
from src.homework.j_classes.class_a import Die

class TestDie(unittest.TestCase):

    def test_roll_value_within_range(self):
        die = Die()
        for _ in range(3):
            die.roll()
            roll_value = die.get_rolled_value()
            self.assertTrue(1 <= roll_value <= 6, f"Roll value {roll_value} is out of range")

if __name__ == '__main__':
    unittest.main()
