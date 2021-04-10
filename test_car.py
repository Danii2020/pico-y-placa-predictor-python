import unittest
from car import Car as C

class TestOnTheRoad(unittest.TestCase):
    def setUp(self):
        self.car_1 = C('pdf121', '12/04/2021', '07:25')     
        self.car_2 = C('pdf121', '12/04/2021', '13:25')     
        self.car_3 = C('pdf121', '12/04/2021', '17:25')     

    def test_on_the_road(self):
       
        self.assertEqual(self.car_1.on_the_road(), True)
        self.assertEqual(self.car_2.on_the_road(), False)
        self.assertEqual(self.car_3.on_the_road(), True)
    


if __name__ == "__main__":
    unittest.main()