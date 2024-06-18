import unittest

from src.homework.d_repetition.repetition import get_factorial

from src.homework.d_repetition.repetition import sum_odd_numbers

class Test_Config(unittest.TestCase):

  def test_get_factorial(self):
    #tests the get_factorial function when user enters 4 and gets 24
    self.assertEqual(24, get_factorial(4))
  def test_get_factorial(self):
    #tests the get_factorial function when user enters 5 and gets 120
    self.assertEqual(120, get_factorial(5))
  def test_get_factorial(self):
    #tests the get_factorial function when user enters 6 and gets 720
    self.assertEqual(720, get_factorial(6))
  def test_sum_odd_numbers(self):
    #tests the sum_odd_numbers function when user enters 7 and gets 16
    self.assertEqual(16, sum_odd_numbers(7))
  def test_sum_odd_numbers(self):
    #tests the sum_odd_numbers function when user enters 9 and gets 25
    self.assertEqual(25, sum_odd_numbers(9))
  def test_sum_odd_numbers(self):
    #tests the sum_odd_numbers function when user enters 10 and gets 25
    self.assertEqual(25, sum_odd_numbers(10))