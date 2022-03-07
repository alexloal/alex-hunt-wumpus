import unittest

from board import Board


class BoardTest(unittest.TestCase):

    def test_cave_is_created(self):
        my_board = Board()
        self.assertEqual(len(my_board.get_free_rooms()), 20) \
        and self.assertEqual(my_board.player_position, -1) \
        and self.assertEqual(my_board.rivals == [], True)

    def test_cave_fill_cave(self):
        my_board = Board()
        my_board.fill_cave()
        self.assertEqual(len(my_board.get_free_rooms()), 15) \
        and self.assertEqual(len(my_board.rivals), 5) \
        and self.assertNotEqual(my_board.player_position, -1)

    def test_search_1_depth(self):
        my_board = Board()
        # 1 -> 2,5,8
        found, depth = my_board.search(1, 2)
        assert found and depth == 1
        found, depth = my_board.search(1, 5)
        assert found and depth == 1
        found, depth = my_board.search(1, 8)
        assert found and depth == 1

    def test_free_rooms(self):
        my_board = Board()
        i = 0
        for rival in ['bat', 'bat', 'pit', 'pit', 'wumpus']:
            my_board.rivals[i] = rival
            i += 1
        free = my_board.get_free_rooms()
        assert free == list(range(5, 21))

    def test_get_number_of_pits(self):
        my_board = Board()
        my_board.fill_cave_game_option(['bat', 'pit', 'pit', 'pit', 'wumpus'], 5)
        assert my_board.get_number_of_pits() == 3

    def test_get_number_of_bats(self):
        my_board = Board()
        my_board.fill_cave_game_option(['bat', 'bat', 'pit', 'bat', 'wumpus'], 5)
        assert my_board.get_number_of_bats() == 3


if __name__ == '__main__':
    unittest.main()
