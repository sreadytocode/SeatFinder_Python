import unittest

from src.seatfinder import SeatFinder

class SeatFinderTest(unittest.TestCase):
    
    def test_prefer_near_the_front(self):
        finder = SeatFinder(available_seats={"A6", "B6", "C7"})
        seats = finder.find_seats(1)
        assert seats == {"A6"}

    

    