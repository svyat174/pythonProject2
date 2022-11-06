import unittest
from get_score import *


class ScoreTest(unittest.TestCase):

    # В начале игры счет 0:0
    def test_startgame_zero_score(self):
        res = get_score(game_stamps, 0)
        self.assertEqual(res, (0, 0))

    # На каждом шаге оффсет строго увеличивается не более чем на OFFSET_MAX_STEP
    def test_offset_increase(self):
        previous = -1
        for dict_ in game_stamps:
            current = dict_['offset']
            self.assertLess(previous, current)
            self.assertLessEqual(current - previous, OFFSET_MAX_STEP)
            previous = current

    # На каждом шаге домашний счет либо не меняется, либо растет на 1
    def test_home_score_non_decrease(self):
        previous = 0
        for dict_ in game_stamps:
            current = dict_['score']['home']
            self.assertLessEqual(previous, current)
            self.assertLessEqual(current - previous, 1)
            previous = current

    # На каждом шаге гостевой счет либо не меняется, либо растет на 1
    def test_away_score_non_decrease(self):
        previous = 0
        for dict_ in game_stamps:
            current = dict_['score']['away']
            self.assertLessEqual(previous, current)
            self.assertLessEqual(current - previous, 1)
            previous = current
