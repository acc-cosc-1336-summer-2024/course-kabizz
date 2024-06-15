#
import unittest
from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):

     def test_get_options_ratio(self):
        #tests that the function get_options_ratio returns .25
        self.assertEqual(.25, get_options_ratio(5, 20))
     def test_get_options_ratio(self):
        #tests that the function get_options_ratio returns .5
        self.assertEqual(.5, get_options_ratio(10, 20))
     def test_get_faculty_rating(self):
        #tests that the function get_faculty_ratio returns Excellent
        self.assertEqual('Excellent', get_faculty_rating(.91))
     def test_get_faculty_rating(self):
        #tests that the function get_faculty_ratio returns Very Good
        self.assertEqual('Very Good', get_faculty_rating(.85))
     def test_get_faculty_rating(self):
        #tests that the function get_faculty_ratio returns Good
        self.assertEqual('Good', get_faculty_rating(.71))
     def test_get_faculty_rating(self):
        #tests that the function get_faculty_ratio returns Needs Improvement
        self.assertEqual('Needs Improvement', get_faculty_rating(.66))
     def test_get_faculty_rating(self):   
        #tests that the function get_faculty_ratio returns Unacceptable
        self.assertEqual('Unacceptable', get_faculty_rating(.45))