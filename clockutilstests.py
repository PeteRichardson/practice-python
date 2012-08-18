#!/usr/bin/env python

'''Tests for ClockUtils module'''

import unittest
from clockutils import hand_angle
from clockutils import minute_angle
from clockutils import hour_angle
from clockutils import integer_hour_angle
from clockutils import hour_delta_caused_by_minute

class ClockUtilsTests(unittest.TestCase):
    def test_minutes(self):
        self.assertEqual(0, minute_angle(0))
        self.assertEqual(90, minute_angle(15))
        self.assertEqual(180, minute_angle(30))
        self.assertEqual(270, minute_angle(45))
        self.assertEqual(0, minute_angle(60))
        self.assertEqual(90, minute_angle(75))
        
    def test_hours(self):
        self.assertEqual(0, integer_hour_angle(0))
        self.assertEqual(30, integer_hour_angle(1))
        self.assertEqual(60, integer_hour_angle(2))
        self.assertEqual(90, integer_hour_angle(3))
        self.assertEqual(180, integer_hour_angle(6))
        self.assertEqual(240, integer_hour_angle(8))
        self.assertEqual(0, integer_hour_angle(12))
        self.assertEqual(30, integer_hour_angle(13))
        
    def test_hour_delta_caused_by_minute(self):
        self.assertEqual(0, hour_delta_caused_by_minute(0))
        self.assertEqual(7.5, hour_delta_caused_by_minute(15))
        self.assertEqual(15, hour_delta_caused_by_minute(30))
        self.assertEqual(22.5, hour_delta_caused_by_minute(45))
        self.assertEqual(0, hour_delta_caused_by_minute(60))
        self.assertEqual(7.5, hour_delta_caused_by_minute(75))
        
    def test_hour_angle(self):
        self.assertEqual(0, hour_angle(12, 0))
        self.assertEqual(97.5, hour_angle(3, 15))
        
    
    def test_0315(self):
        self.assertEqual(7.5, hand_angle(3,15))
        
    def test_1200(self):
       self.assertEqual(0, hand_angle(12,00))

    def test_0630(self):
       self.assertEqual(15, hand_angle(06,30))
         
if __name__ == "__main__":
    unittest.main()