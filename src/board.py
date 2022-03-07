import random
from random import choice


class Board:
    # board constructor
    def __init__(self):
        # initialize the cave
        self.cave = {1: [2, 5, 8], 2: [1, 3, 10], 3: [2, 4, 12], 4: [3, 5, 14], 5: [1, 4, 6],
                     6: [5, 7, 15], 7: [6, 8, 17], 8: [1, 7, 9], 9: [8, 10, 18], 10: [2, 9, 11],
                     11: [10, 12, 19], 12: [3, 11, 13], 13: [12, 14, 20], 14: [4, 13, 15], 15: [6, 14, 16],
                     16: [15, 17, 20], 17: [7, 16, 18], 18: [9, 17, 19], 19: [11, 18, 20], 20: [13, 16, 19]}
        # initialize available arrows
        self.arrows = 5
        # initial position for the player
        self.player_position = -1
        # here I am going to store all the rivals
        self.rivals = {}
        self.arrow_travel_distance = 1

    def get_free_rooms(self):
        """ Return a list with all numbers of rooms that do not contain any rivals"""
        return list(set(self.cave.keys()).difference(self.rivals.keys()))

    def get_number_of_pits(self):
        """Return the number of pits in the board"""
        return sum(map(lambda x: x == 'pit', self.rivals.values()))

    def get_number_of_bats(self):
        """Return the number of bats in the board"""
        return sum(map(lambda x: x == 'bat', self.rivals.values()))

    def fill_cave_game_option(self, rivals_selected, number_of_arrows):
        for rival in rivals_selected:
            self.rivals[choice(self.get_free_rooms())] = rival

        self.player_position = random.choice(self.get_free_rooms())
        self.arrows = number_of_arrows

    def fill_cave(self):
        """ Fill the cave with all the rivals"""
        self.fill_cave_game_option(['bat', 'bat', 'pit', 'pit', 'wumpus'], 5)

    def search(self, source, target, max_depth=5):
        """Search using a recursive graph"""
        current_depth = 0
        graph = self.cave

        def recursive_search(stack, visited, my_target, depth):
            if not stack:
                return False, -1
            if my_target in stack:
                return True, depth
            visited = visited + stack
            stack = list(set([graph[v][i] for v in stack for i in range(len(graph[v]))]).difference(visited))
            depth += 1
            if depth > max_depth:
                return False, depth
            else:
                return recursive_search(stack, visited, my_target, depth)

        return recursive_search([source], [], target, current_depth)
