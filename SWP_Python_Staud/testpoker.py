import unittest
from poker import (
    is_pair, is_two_pair, is_drilling, is_straight, is_flush,
    is_full_house, is_vierling, is_straight_flush, is_royal_flush
)


class TestPokerHands(unittest.TestCase):
    def test_is_pair(self):
        hand = [('Herz', '2'), ('Karo', '2'), ('Pik', '3'), ('Kreuz', '4'), ('Herz', '5')]
        self.assertTrue(is_pair(hand))

    def test_is_two_pair(self):
        hand = [('Herz', '2'), ('Karo', '2'), ('Pik', '3'), ('Kreuz', '3'), ('Herz', '5')]
        self.assertTrue(is_two_pair(hand))

    def test_is_drilling(self):
        hand = [('Herz', '2'), ('Karo', '2'), ('Pik', '2'), ('Kreuz', '4'), ('Herz', '5')]
        self.assertTrue(is_drilling(hand))

    def test_is_straight(self):
        hand = [('Herz', '2'), ('Karo', '3'), ('Pik', '4'), ('Kreuz', '5'), ('Herz', '6')]
        self.assertTrue(is_straight(hand))

    def test_is_flush(self):
        hand = [('Herz', '2'), ('Herz', '3'), ('Herz', '4'), ('Herz', '5'), ('Herz', '6')]
        self.assertTrue(is_flush(hand))

    def test_is_full_house(self):
        hand = [('Herz', '2'), ('Karo', '2'), ('Pik', '2'), ('Kreuz', '3'), ('Herz', '3')]
        self.assertTrue(is_full_house(hand))

    def test_is_vierling(self):
        hand = [('Herz', '2'), ('Karo', '2'), ('Pik', '2'), ('Kreuz', '2'), ('Herz', '5')]
        self.assertTrue(is_vierling(hand))

    def test_is_straight_flush(self):
        hand = [('Herz', '2'), ('Herz', '3'), ('Herz', '4'), ('Herz', '5'), ('Herz', '6')]
        self.assertTrue(is_straight_flush(hand))

    def test_is_royal_flush(self):
        hand = [('Herz', '10'), ('Herz', 'Bube'), ('Herz', 'Dame'), ('Herz', 'König'), ('Herz', 'Ass')]
        self.assertTrue(is_royal_flush(hand))


if __name__ == "__main__":
    unittest.main()
